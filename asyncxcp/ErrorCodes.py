from enum import Enum

class ErrorCodes(Enum):
    ERR_CMD_SYNCH = 0x00
    ERR_CMD_BUSY = 0x10
    ERR_DAQ_ACTIVE = 0x11
    ERR_PGM_ACTIVE = 0x12
    ERR_CMD_UNKNOWN = 0x20
    ERR_CMD_SYNTAX = 0x21
    ERR_OUT_OF_RANGE = 0x22
    ERR_WRITE_PROTECTED = 0x23
    ERR_ACCESS_DENIED = 0x24
    ERR_ACCESS_LOCKED = 0x25
    ERR_PAGE_NOT_VALID = 0x26
    ERR_MODE_NOT_VALID = 0x27
    ERR_SEGMENT_NOT_VALID = 0x28
    ERR_SEQUENCE = 0x29
    ERR_DAQ_CONFIG = 0x2A
    ERR_MEMORY_OVERFLOW = 0x30
    ERR_GENERIC = 0x31
    ERR_VERIFY = 0x32

    @classmethod
    def get_name(cls, value):
        for name, member in cls.__members__.items():
            if member.value == value:
                return name
        return None
