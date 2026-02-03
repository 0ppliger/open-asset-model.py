from enum import Enum
from typing import Optional, Any
from dataclasses import dataclass
from dataclasses import field
from asset_model.relation import Relation
from asset_model.relation import RelationType
from asset_model.property import Property
from asset_model.property import PropertyType
from asset_model.oam_object import OAMObject

@dataclass
class RRHeader(OAMObject):
    rrtype:  int = field(metadata={"json":"rr_type"})
    rrname:  int = field(metadata={"json":"rr_name"})
    cls:     Optional[int] = field(default=None, metadata={"json":"class"})
    ttl:     Optional[int] = field(default=None, metadata={"json":"ttl"})
    

@dataclass
class BasicDNSRelation(Relation):
    """BasicDNSRelation is a relation in the graph representing a
    basic DNS resource record."""
    name:    str = field(metadata={"json":"label"})
    header:  RRHeader = field(init=False, metadata={"json":"header"})

    def __init__(
        self,
        name:   str,
        rrtype: int,
        rrname: str,
        cls: Optional[int] = None,
        ttl: Optional[int] = None,
        extra: dict[str, Any] = {}
    ):
        super().__init__(extra=extra)
        self.name = name
        self.header = RRHeader(
            rrtype=rrtype,
            rrname=rrname,
            cls=cls,
            ttl=ttl,
        )
    
    @property
    def relation_type(self) -> RelationType:
        return RelationType.BasicDNSRelation

    @property
    def label(self) -> str:
        return self.name

@dataclass
class PrefDNSRelation(Relation):
    """PrefDNSRelation is a relation in the graph representing a DNS
    resource record with preference information."""
    name:       str = field(metadata={"json":"label"})
    preference: int
    header:  RRHeader = field(init=False, metadata={"json":"header"})

    def __init__(
        self,
        name:   str,
        preference: int,
        rrtype: int,
        rrname: str,
        cls: Optional[int] = None,
        ttl: Optional[int] = None,
        extra: dict[str, Any] = {}
    ):
        super().__init__(extra=extra)
        self.name = name
        self.preference = preference
        self.header = RRHeader(
            rrtype=rrtype,
            rrname=rrname,
            cls=cls,
            ttl=ttl,
        )

    @property
    def relation_type(self) -> RelationType:
        return RelationType.PrefDNSRelation

    @property
    def label(self) -> str:
        return self.name

@dataclass
class SRVDNSRelation(Relation):
    """SRVDNSRelation is a relation in the graph representing a DNS
    SRV resource record."""
    name:     str = field(metadata={"json":"label"})
    priority: int
    weight:   int
    port:     int
    header:  RRHeader = field(init=False, metadata={"json":"header"})

    def __init__(
        self,
        name: str,
        priority: int,
        weight:   int,
        port:     int,
        rrtype:   int,
        rrname:   str,
        cls: Optional[int] = None,
        ttl: Optional[int] = None,
        extra: dict[str, Any] = {}
    ):
        super().__init__(extra=extra)
        self.name = name
        self.priority = priority
        self.weight = weight
        self.port = port
        self.header = RRHeader(
            rrtype=rrtype,
            rrname=rrname,
            cls=cls,
            ttl=ttl,
        )
    
    @property
    def relation_type(self) -> RelationType:
        return RelationType.SRVDNSRelation
    
    @property
    def label(self) -> str:
        return self.name

@dataclass
class DNSRecordProperty(Property):
    """DNSRecordProperty represents a DNS resource record that does
    not refer to another asset in the graph."""
    property_name: str
    data:          str
    header:  RRHeader = field(init=False, metadata={"json":"header"})

    def __init__(
        self,
        property_name: str,
        data:          str,
        rrtype:        int,
        rrname:        str,
        cls: Optional[int] = None,
        ttl: Optional[int] = None,
        extra: dict[str, Any] = {}
    ):
        super().__init__(extra=extra)
        self.property_name = property_name
        self.data = data
        self.header = RRHeader(
            rrtype=rrtype,
            rrname=rrname,
            cls=cls,
            ttl=ttl,
        )
    
    @property
    def property_type(self) -> PropertyType:
        return PropertyType.DNSRecordProperty
    
    @property
    def name(self) -> str:
        return self.property_name

    @property
    def value(self) -> str:
        return self.data
