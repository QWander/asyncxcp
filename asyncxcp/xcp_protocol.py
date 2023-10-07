from dataclasses import dataclass
from typing import Type, List, Optional
from abc import ABC, abstractclassmethod

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
        @classmethod
        @abstractclassmethod
        def errordo_codes():
            pass
        @classmethod
        def response_id():
            pass

    # Standard commands (STD)
    @dataclass
    class CONNECT():
        pass
    @dataclass
    class DISCONNECT():
        pass
