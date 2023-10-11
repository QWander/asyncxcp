#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XCP_BASE_Protocol-Layer_v1-5-0"""
from dataclasses import dataclass
from typing import Type, List, Optional
from abc import abstractmethod

@dataclass
class PLS:
    """ProtocolLayerSpecification
    所有协议层信息的总类型
    """
    name:str = "ProtocolLayerSpecification"
    version: str = "1.0"
    auther: str = "QWander"
    abbreviation: str = "PLS"

    class BaseCommand:
        """_summary_
        """
        eroe_codes = {}
        Command:str
        Code:int
        Support:str

        @staticmethod
        def __get_all_subclasses(base_cls: Optional["PLS.BaseCommand"]) -> list:
            all_subclasses = []
            for subclass in base_cls.__subclasses__():
                all_subclasses.append(subclass)
                all_subclasses.extend(PLS.BaseCommand.__get_all_subclasses(subclass))
            return all_subclasses

        @classmethod
        def from_request_command(cls, command_id:int) -> Optional[Type["PLS.BaseCommand"]]:
            """from_request_command

            command_id(int): XCP Command

            Returns:
                _type_: Returns an instance of the service 
                identified by the service command (Request)
            """
            classes = PLS.BaseCommand.__get_all_subclasses(cls)
            for obj in classes:
                if obj.request_id() == command_id:
                    return obj
            return None

        @classmethod
        def is_negative(cls, response_data: bytes) -> bool:
            """_summary_

            Args:
                response_data (_type_): _description_
            """
            if response_data[0] == 0xFF:
                return False
            elif response_data[0] == 0xFE:
                return True
            else:
                return True

        @abstractmethod
        def build_request(self):
            """_summary_"""

        @abstractmethod
        def build_response(self):
            """_summary_"""



    # Standard commands (STD)
    @dataclass
    class Connect(BaseCommand):
        """
        Command     CONNECT
        Code        0xFF
        Support     mandatory
        """

        def build_request(self, mode:int=0):
            """_summary_"""
            code:int = 0xFF
            mode:int = 00      #00 = Normal；01 = user-defined. default is Normal

        def build_response(self, data):
            """_summary_"""
            if self.is_negative(data):
                pass
            else:
                
            # response info

            # RESOURCE
            dbg:float = data
            pgm:float
            stim:float
            daq:float
            cal_pag:float
            resource = [dbg, pgm, stim, daq, cal_pag]
            # COMM_MODE_BASIC
            optional:float
            slave_block_mode:float
            address_granularity:float
            byte_order:float
            # MAX_CTO
            max_cto:int
            # MAX_DTO
            max_dto:int
            # XCP Protocol Layer Version Number
            xcp_pls_version:int
            # XCP Transport Layer Version Number
            xcp_tls_version:int

    @dataclass
    class Disconnect():
        """
        Command     DISCONNECT
        Code        0xFE
        Support     mandatory
        """
        pass

    @dataclass
    class GetStatus():
        """
        Command     GET_STATUS
        Code        0xFD
        Support     mandatory
        """
        pass

    @dataclass
    class Synch():
        """
        Command     SYNCH
        Code        0xFC
        Support     mandatory
        """
        pass

    @dataclass
    class GetCommModeInfo():
        """
        Command     GET_COMM_MODE_INFO
        Code        0xFB
        Support     optional
        """
        pass

    @dataclass
    class GetID():
        """
        Command     GET_ID
        Code        0xFA
        Support     optional
        """
        pass

    @dataclass
    class SetRequest():
        """
        Command     SET_REQUEST
        Code        0xF9
        Support     optional
        """
        pass

    @dataclass
    class GetSeed():
        """
        Command     GET_SEED
        Code        0xF8
        Support     optional
        """
        pass

    @dataclass
    class Unlock():
        """
        Command     UNLOCK
        Code        0xF7
        Support     optional
        """
        pass

    @dataclass
    class SetMTA():
        """
        Command     SET_MTA
        Code        0xF6
        Support     optional
        """
        pass

    @dataclass
    class Upload():
        """
        Command     UPLOAD
        Code        0xF5
        Support     optional
        """
        pass

    @dataclass
    class ShortUpload():
        """
        Command     SHORT_UPLOAD
        Code        0xF4
        Support     optional
        """
        pass

    @dataclass
    class BuildChecksum():
        """
        Command     BUILD_CHECKSUM
        Code        0xF3
        Support     optional
        """
        pass

    @dataclass
    class TransportLayerCMD():
        """
        Command     TRANSPORT_LAYER_CMD
        Code        0xF2
        Support     optional
        """
        pass

    @dataclass
    class UserCMD():
        """
        Command     USER_CMD
        Code        0xF1
        Support     optional
        """
        pass

    @dataclass
    class GetVersion():
        """
        Command     GET_VERSION
        Code        0xC0, 0x00
        Support     optional
        """
        pass








    # Calibration Commands
    @dataclass
    class Download():
        pass
    @dataclass
    class DownloadNext():
        pass
    @dataclass
    class DownloadMax():
        pass
    @dataclass
    class ShortDownload():
        pass
    @dataclass
    class ModifyBits():
        pass

    # Page switching commands
    @dataclass
    class SetCalPage():
        pass
    @dataclass
    class GetCalPage():
        pass
    @dataclass
    class GetPagProcessorInfo():
        pass
    @dataclass
    class GetSegmentInfo():
        pass
    @dataclass
    class GetPageInfo():
        pass
    @dataclass
    class SetSegmentMode():
        pass
    @dataclass
    class GetSenmentMode():
        pass
    @dataclass
    class CopyCalPage():
        pass

    # Basic data acquisition and stimulation commands
    @dataclass
    class SET_DAQ_PTR():
        pass
    @dataclass
    class WRITE_DAQ():
        pass
    @dataclass
    class SET_DAQ_LIST_MODE():
        pass
    @dataclass
    class START_STOP_DAQ_LIST():
        pass
    @dataclass
    class START_STOP_SYNCH():
        pass

    @dataclass
    class WRITE_DAQ_MULTIPLE():
        pass
    @dataclass
    class READ_DAQ():
        pass
    @dataclass
    class GET_DAQ_CLOCK():
        pass
    @dataclass
    class GET_DAQ_PROCESSOR_INFO():
        pass
    @dataclass
    class GET_DAQ_RESOLUTION_INFO():
        pass
    @dataclass
    class GET_DAQ_LIST_MODE():
        pass
    @dataclass
    class GET_DAQ_EVENT_INFO():
        pass
    @dataclass
    class DTO_CTR_PROPERTIES():
        pass
    @dataclass
    class SET_DAQ_PACKED_MODE():
        pass
    @dataclass
    class GET_DAQ_PACKED_MODE():
        pass
    @dataclass
    class GET_DAQ_LIST_MODE():
        pass




    

