import json
from abc import ABC
from abc import abstractmethod
from enum import Enum

class RelationType(Enum):
    BasicDNSRelation = "BasicDNSRelation"
    PortRelation = "PortRelation"
    PrefDNSRelation = "PrefDNSRelation"
    SimpleRelation = "SimpleRelation"
    SRVDNSRelation = "SRVDNSRelation"

class Relation(ABC):
    @property
    @abstractmethod
    def label(self) -> str:
        pass

    @property
    @abstractmethod
    def relation_type(self) -> RelationType:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
RelationList = list(RelationType)
