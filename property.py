import json
from abc import ABC
from abc import abstractmethod
from enum import Enum

class PropertyType(Enum):
    DNSRecordProperty = "DNSRecordProperty"
    SimpleProperty = "SimpleProperty"
    SourceProperty = "SourceProperty"
    VulnProperty = "VulnProperty"

class Property(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> str:
        pass

    @property
    @abstractmethod
    def property_type(self) -> PropertyType:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())


PropertyList = list(PropertyType)
