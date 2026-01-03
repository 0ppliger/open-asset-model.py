from enum import Enum
from typing import Optional
from dataclasses import dataclass
from dataclasses import field
from oam.relation import Relation
from oam.relation import RelationType
from oam.property import Property
from oam.property import PropertyType

@dataclass
class RRHeader:
    rr_type: int
    cls:     Optional[int] = None
    ttl:     Optional[int] = None

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            'rr_type': self.rr_type,
            'class': self.cls,
            'ttl': self.ttl
        }.items() if value is not None}

@dataclass
class BasicDNSRelation(Relation):
    """BasicDNSRelation is a relation in the graph representing a
    basic DNS resource record."""
    name:   str
    header: RRHeader

    @property
    def relation_type(self) -> RelationType:
        return RelationType.BasicDNSRelation

    @property
    def label(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        return {
            'label': self.label,
            'header': self.header.to_dict()
        }

@dataclass
class PrefDNSRelation(Relation):
    """PrefDNSRelation is a relation in the graph representing a DNS
    resource record with preference information."""
    name:       str
    header:     RRHeader
    preference: int

    @property
    def relation_type(self) -> RelationType:
        return RelationType.PrefDNSRelation

    @property
    def label(self) -> str:
        return self.name
    
    def to_dict(self) -> dict:
        return {
            'label': self.label,
            'header': self.header.to_dict(),
            'preference': self.preference
        }

@dataclass
class SRVDNSRelation(Relation):
    """SRVDNSRelation is a relation in the graph representing a DNS
    SRV resource record."""
    name:     str
    header:   RRHeader
    priority: int
    weight:   int
    port:     int

    @property
    def relation_type(self) -> RelationType:
        return RelationType.SRVDNSRelation
    
    @property
    def label(self) -> str:
        return self.name
    
    def to_dict(self) -> dict:
        return {
            'label': self.label,
            'header': self.header.to_dict(),
            'priority': self.priority,
            'weight': self.weight,
            'port': self.port
        }

@dataclass
class DNSRecordProperty(Property):
    """DNSRecordProperty represents a DNS resource record that does
    not refer to another asset in the graph."""
    property_name: str
    header:        RRHeader
    data:          str

    @property
    def property_type(self) -> PropertyType:
        return PropertyType.DNSRecordProperty
    
    @property
    def name(self) -> str:
        return self.property_name

    @property
    def value(self) -> str:
        return self.data

    def to_dict(self) -> dict:
        return {
            'property_name': self.name,
            'header': self.header.to_dict(),
            'data': self.value
        }
