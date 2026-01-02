from dataclasses import dataclass
from relation import Relation, RelationType
import json

@dataclass
class PortRelation(Relation):
    """PortRelation is a relation in the graph representing an open
    port."""
    name: str
    port_number: int
    protocol: str
    
    @property
    def label(self) -> str:
        return self.name

    @property
    def relation_type(self) -> RelationType:
        return RelationType.PortRelation

    def to_dict(self) -> dict:
        return {
            'label': self.label,
            'port_number': self.port_number,
            'protocol': self.protocol
        }
