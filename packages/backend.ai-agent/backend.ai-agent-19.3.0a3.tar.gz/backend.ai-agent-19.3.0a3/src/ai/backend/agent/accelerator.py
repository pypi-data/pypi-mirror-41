from abc import abstractmethod, ABCMeta
import decimal
from pathlib import Path
from typing import (
    Any, Collection, Container, Hashable,
    Mapping, Sequence, TypeVar, Optional,
)

import aiodocker
import attr

ProcessorIdType = TypeVar('ProcessorIdType', int, str, Hashable)


accelerator_types = {}


@attr.s(auto_attribs=True)
class AbstractAcceleratorInfo(metaclass=ABCMeta):
    device_id: ProcessorIdType
    hw_location: str            # either PCI bus ID or arbitrary string
    numa_node: Optional[int]    # NUMA node ID (None if not applicable)
    memory_size: int            # bytes of available per-accelerator memory
    processing_units: int       # number of processing units (e.g., cores, SMP)

    @abstractmethod
    def is_fractional(self) -> bool:
        return False

    @abstractmethod
    def max_share(self) -> decimal.Decimal:
        '''
        Calculates the amount of available shares for this accelerator.
        '''
        return decimal.Decimal('0')

    @abstractmethod
    def share_to_spec(self, share: decimal.Decimal) -> (int, int):
        '''
        Calculates the amount of memory and processing units
        corresponding to the given share.
        '''
        return 0, 0

    @abstractmethod
    def spec_to_share(self, requested_memory: int,
                      requested_proc_units: int) -> decimal.Decimal:
        '''
        Calculates the minimum required share to guarantee the given
        requested resource specification (memory in bytes and the number
        of processing units).
        '''
        return decimal.Decimal('0')


class AbstractAccelerator(metaclass=ABCMeta):

    slot_key = 'accelerator'

    @classmethod
    @abstractmethod
    def list_devices(cls) -> Collection[AbstractAcceleratorInfo]:
        '''
        Return a collection of processors.
        '''
        return []

    @classmethod
    @abstractmethod
    def get_hooks(cls, distro: str, arch: str) -> Sequence[Path]:
        '''
        Return the library hook paths used by the plugin (optional).

        :param str distro: The target Linux distribution such as "ubuntu16.04" or
                           "alpine3.8"
        :param str arch: The target CPU architecture such as "amd64"
        '''
        return []

    @abstractmethod
    async def generate_docker_args(
            cls,
            docker: 'aiodocker.docker.Docker',  # noqa
            limit_gpus: Container[ProcessorIdType] = None) \
            -> Mapping[str, Any]:
        return {}
