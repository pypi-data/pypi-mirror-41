# coding: UTF-8

from __future__ import annotations

from abc import ABCMeta
from ctypes import addressof, py_object
from typing import TYPE_CHECKING, Union, overload

from linux_aio_bind import IOCB, IOCBCMD, IOCBFlag, IOPRIO_CLASS_SHIFT, gen_io_priority

if TYPE_CHECKING:
    from typing import Any, Optional
    from linux_aio_bind import IOCBPriorityClass, IOCBRWFlag
    from .non_rw import FDsyncCmd, FsyncCmd, PollCmd
    from .non_vector import ReadCmd, WriteCmd
    from .vector import ReadVCmd, WriteVCmd


class AIOCmd(metaclass=ABCMeta):
    """
    .. versionadded:: 0.1.0
    """
    __slots__ = ('_iocb', '_py_obj', '_file_obj', '_deleted')

    _iocb: IOCB
    _py_obj: py_object  # to avoid garbage collection
    _file_obj: Union[Any, int]
    _deleted: bool

    def __init__(self, file: Union[Any, int], cmd: IOCBCMD, rw_flags: IOCBRWFlag, priority_class: IOCBPriorityClass,
                 priority_value: int, buffer: int, length: int, offset: int, res_fd: int) -> None:
        fd = self._get_fd(file)
        priority = gen_io_priority(priority_class, priority_value)

        flags: IOCBFlag = 0

        if priority is not 0:
            flags |= IOCBFlag.IOPRIO

        if res_fd is not 0:
            flags |= IOCBFlag.RESFD

        self._file_obj = file
        self._deleted = False
        self._py_obj = py_object(self)
        self._iocb = IOCB(
                aio_data=addressof(self._py_obj),
                aio_rw_flags=rw_flags,
                aio_lio_opcode=cmd,
                aio_reqprio=priority,
                aio_fildes=fd,
                aio_buf=buffer,
                aio_nbytes=length,
                aio_offset=offset,
                aio_flags=flags,
                aio_resfd=res_fd
        )

    def __hash__(self) -> int:
        return addressof(self._iocb)

    @classmethod
    def _get_fd(cls, file: Union[int, Any]) -> int:
        if isinstance(file, int):
            fd = file
        else:
            try:
                fd = file.fileno()
            except AttributeError:
                raise AttributeError(f'`file` must be an int or an object with a fileno() method. current: {file}')

        return fd

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.POLL) -> PollCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.FDSYNC) -> FDsyncCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.FSYNC) -> FsyncCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.PREAD) -> ReadCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.PWRITE) -> WriteCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.PREADV) -> ReadVCmd:
        ...

    @overload
    def change_cmd(self, new_cmd: IOCBCMD.PWRITEV) -> WriteVCmd:
        ...

    def change_cmd(self, new_cmd: IOCBCMD) -> AIOCmd:
        if new_cmd is self.cmd:
            return self

        if new_cmd is IOCBCMD.PWRITE:
            from .non_vector import WriteCmd
            block = WriteCmd.__new__(WriteCmd)
            if self.cmd is not IOCBCMD.PREAD:
                self._reset_buf()

        elif new_cmd is IOCBCMD.PREAD:
            from .non_vector import ReadCmd
            block = ReadCmd.__new__(ReadCmd)
            if self.cmd is not IOCBCMD.PWRITE:
                self._reset_buf()

        elif new_cmd is IOCBCMD.FSYNC:
            from .non_rw import FsyncCmd
            block = FsyncCmd.__new__(FsyncCmd)
            self._reset_for_non_rw()

        elif new_cmd is IOCBCMD.FDSYNC:
            from .non_rw import FDsyncCmd
            block = FDsyncCmd.__new__(FDsyncCmd)
            self._reset_for_non_rw()

        elif new_cmd is IOCBCMD.POLL:
            from .non_rw import PollCmd
            block = PollCmd.__new__(PollCmd)
            self._reset_for_non_rw()

        elif new_cmd is IOCBCMD.PWRITEV:
            from .vector import WriteVCmd
            block = WriteVCmd.__new__(WriteVCmd)
            if self.cmd is not IOCBCMD.PREADV:
                self._reset_buf()

        elif new_cmd is IOCBCMD.PREADV:
            from .vector import ReadVCmd
            block = ReadVCmd.__new__(ReadVCmd)
            if self.cmd is not IOCBCMD.PWRITEV:
                self._reset_buf()
        else:
            raise ValueError(f'Unknown command :{new_cmd}')

        block._py_obj = py_object(block)
        block._iocb = self._iocb
        block._iocb.aio_lio_opcode = new_cmd
        block._iocb.aio_data = addressof(block._py_obj)
        block._file_obj = self._file_obj
        block._deleted = False

        self._deleted = True

        return block

    def _reset_for_non_rw(self) -> None:
        self._iocb.aio_flags = 0
        self._iocb.aio_rw_flags = 0
        self._reset_buf()

    def _reset_buf(self) -> None:
        self._iocb.aio_buf = 0
        self._iocb.aio_nbytes = 0
        self._iocb.aio_offset = 0

    @property
    def file(self) -> Union[Any, int]:
        return self._file_obj

    @file.setter
    def file(self, new_file: Union[Any, int]) -> None:
        self._iocb.aio_fildes = self._get_fd(new_file)
        self._file_obj = new_file

    @property
    def fileno(self) -> int:
        return self._iocb.aio_fildes

    @property
    def cmd(self) -> IOCBCMD:
        return IOCBCMD(self._iocb.aio_lio_opcode)

    @property
    def flag(self) -> int:
        return self._iocb.aio_flags

    @flag.setter
    def flag(self, new_flag: int) -> None:
        self._iocb.aio_flags = new_flag

    @property
    def res_fd(self) -> Optional[int]:
        res_fd = self._iocb.aio_resfd
        if res_fd is not 0:
            return res_fd
        else:
            return None

    @res_fd.setter
    def res_fd(self, fd: int) -> None:
        self.flag |= IOCBFlag.RESFD
        self._iocb.aio_resfd = fd

    @property
    def priority_class(self) -> int:
        return self._iocb.aio_reqprio >> IOPRIO_CLASS_SHIFT

    @priority_class.setter
    def priority_class(self, new_class: IOCBPriorityClass) -> None:
        self.flag |= IOCBFlag.IOPRIO
        self._iocb.aio_reqprio = new_class << IOPRIO_CLASS_SHIFT | self.priority_value

    @property
    def priority_value(self) -> int:
        return self._iocb.aio_reqprio & ((1 << IOPRIO_CLASS_SHIFT) - 1)

    @priority_value.setter
    def priority_value(self, value: int) -> None:
        self.flag |= IOCBFlag.IOPRIO
        self._iocb.aio_reqprio = self.priority_class << IOPRIO_CLASS_SHIFT | value

    def set_priority(self, io_class: IOCBPriorityClass, priority: int) -> None:
        self.flag |= IOCBFlag.IOPRIO
        self._iocb.aio_reqprio = gen_io_priority(io_class, priority)
