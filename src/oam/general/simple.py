from dataclasses import dataclass
from enum import Enum
from typing import Dict
import json
from oam.property import Property, PropertyType
from oam.relation import Relation, RelationType

@dataclass
class SimpleRelation(Relation):
    """SimpleRelation represents a simple relation in the graph with
    no additional data required."""
    name: str

    @property
    def label(self) -> str:
        return self.name

    @property
    def relation_type(self) -> RelationType:
        return RelationType.SimpleRelation

    def to_dict(self) -> Dict:
        return {'label': self.label}

@dataclass
class SimpleProperty(Property):
    """SimpleProperty represents a simple property in the graph."""
    property_name: str
    property_value: str

    @property
    def name(self) -> str:
        return self.property_name

    @property
    def value(self) -> str:
        return self.property_value

    @property
    def property_type(self) -> PropertyType:
        return PropertyType.SimpleProperty

    def to_dict(self) -> Dict:
        return {'property_name': self.name, 'property_value': self.value}
