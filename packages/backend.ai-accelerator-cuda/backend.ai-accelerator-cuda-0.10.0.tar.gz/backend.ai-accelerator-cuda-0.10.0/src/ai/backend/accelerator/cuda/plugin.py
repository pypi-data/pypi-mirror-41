import subprocess
import logging
from pathlib import Path
from pprint import pformat
import re
from typing import Collection, Mapping, Sequence

import attr
import aiohttp

from ai.backend.agent.resources import (
    AbstractComputeDevice, AbstractComputePlugin, AbstractAllocMap,
    DiscretePropertyAllocMap,
)
from ai.backend.common.logging import BraceStyleAdapter
from ai.backend.common.types import BinarySize
from .nvidia import libcudart

log = BraceStyleAdapter(logging.getLogger('ai.backend.accelerator.cuda'))


async def init(etcd):
    try:
        ret = subprocess.run(['nvidia-docker', 'version'],
                             stdout=subprocess.PIPE)
    except FileNotFoundError:
        log.warning('nvidia-docker is not installed.')
        log.info('CUDA acceleration is disabled.')
        return 0
    rx = re.compile(r'^NVIDIA Docker: (\d+\.\d+\.\d+)')
    for line in ret.stdout.decode().strip().splitlines():
        m = rx.search(line)
        if m is not None:
            CUDAPlugin.nvdocker_version = tuple(map(int, m.group(1).split('.')))
            break
    else:
        log.error('could not detect nvidia-docker version!')
        log.info('CUDA acceleration is disabled.')
        return
    detected_devices = await CUDAPlugin.list_devices()
    log.info('detected devices:\n' + pformat(detected_devices))
    log.info('nvidia-docker version: {}', CUDAPlugin.nvdocker_version)
    log.info('CUDA acceleration is enabled.')
    return CUDAPlugin


@attr.s(auto_attribs=True)
class CUDADevice(AbstractComputeDevice):
    pass


class CUDAPlugin(AbstractComputePlugin):

    key = 'cuda'
    slot_types = (
        ('cuda.device', 'count'),  # provided for legacy (not allocatable!)
    )

    nvdocker_version = (0, 0, 0)

    @classmethod
    async def list_devices(cls) -> Collection[CUDADevice]:
        all_devices = []
        num_devices = libcudart.get_device_count()
        for dev_idx in range(num_devices):
            raw_info = libcudart.get_device_props(dev_idx)
            sysfs_node_path = "/sys/bus/pci/devices/" \
                              f"{raw_info['pciBusID_str'].lower()}/numa_node"
            try:
                node = int(Path(sysfs_node_path).read_text().strip())
            except OSError:
                node = None
            dev_info = CUDADevice(
                device_id=dev_idx,
                hw_location=raw_info['pciBusID_str'],
                numa_node=node,
                memory_size=raw_info['totalGlobalMem'],
                processing_units=raw_info['multiProcessorCount'],
            )
            all_devices.append(dev_info)
        return all_devices

    @classmethod
    async def available_slots(cls) -> Mapping[str, str]:
        devices = await cls.list_devices()
        slots = {
            'cuda.smp': sum(dev.processing_units for dev in devices),
            'cuda.mem': f'{BinarySize(sum(dev.memory_size for dev in devices)):g}',
            # TODO: fractional alloc map
            'cuda.device': len(devices),
        }
        return slots

    @classmethod
    async def create_alloc_map(cls) -> AbstractAllocMap:
        devices = await cls.list_devices()
        # TODO: fractional alloc map
        return DiscretePropertyAllocMap(
            devices=devices,
            prop_func=lambda dev: 1)

    @classmethod
    async def get_hooks(cls, distro: str, arch: str) -> Sequence[Path]:
        return []

    @classmethod
    async def generate_docker_args(cls, docker, per_device_alloc):
        if cls.nvdocker_version[0] == 1:
            timeout = aiohttp.Timeout(total=3)
            async with aiohttp.ClientSession(raise_for_status=True,
                                             timeout=timeout) as sess:
                try:
                    nvdocker_url = 'http://localhost:3476/docker/cli/json'
                    async with sess.get(nvdocker_url) as resp:
                        nvidia_params = await resp.json()
                except aiohttp.ClientError:
                    raise RuntimeError('NVIDIA Docker plugin is not available.')

            volumes = await docker.volumes.list()
            existing_volumes = set(vol['Name'] for vol in volumes['Volumes'])
            required_volumes = set(vol.split(':')[0]
                                   for vol in nvidia_params['Volumes'])
            missing_volumes = required_volumes - existing_volumes
            binds = []
            for vol_name in missing_volumes:
                for vol_param in nvidia_params['Volumes']:
                    if vol_param.startswith(vol_name + ':'):
                        _, _, permission = vol_param.split(':')
                        driver = nvidia_params['VolumeDriver']
                        await docker.volumes.create({
                            'Name': vol_name,
                            'Driver': driver,
                        })
            for vol_name in required_volumes:
                for vol_param in nvidia_params['Volumes']:
                    if vol_param.startswith(vol_name + ':'):
                        _, mount_pt, permission = vol_param.split(':')
                        binds.append('{}:{}:{}'.format(
                            vol_name, mount_pt, permission))
            devices = []
            for dev in nvidia_params['Devices']:
                m = re.search(r'^/dev/nvidia(\d+)$', dev)
                if m is None:
                    # Always add non-GPU device files required by the driver.
                    # (e.g., nvidiactl, nvidia-uvm, ... etc.)
                    devices.append(dev)
                    continue
                dev_idx = int(m.group(1))
                if dev_idx not in per_device_alloc:
                    continue
                devices.append(dev)
            devices = [{
                'PathOnHost': dev,
                'PathInContainer': dev,
                'CgroupPermissions': 'mrw',
            } for dev in devices]
            return {
                'HostConfig': {
                    'Binds': binds,
                    'Devices': devices,
                },
            }
        elif cls.nvdocker_version[0] == 2:
            gpus = []
            num_devices = libcudart.get_device_count()
            for dev_idx in range(num_devices):
                if dev_idx in per_device_alloc:
                    gpus.append(dev_idx)
            return {
                'HostConfig': {
                    'Runtime': 'nvidia',
                },
                'Env': [
                    f"NVIDIA_VISIBLE_DEVICES={','.join(map(str, gpus))}",
                ],
            }
        else:
            raise RuntimeError('BUG: should not be reached here!')

    @classmethod
    async def restore_from_container(cls, container, alloc_map):
        # TODO: implement!
        pass
