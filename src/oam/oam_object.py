from __future__ import annotations
from abc import ABC
from json import dumps
from dataclasses import field
from dataclasses import fields
from dataclasses import dataclass
from dataclasses import is_dataclass
from typing import Any
from typing import Mapping
from enum import Enum

@dataclass(kw_only=True)
class OAMObject(ABC):
    extra: Mapping[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        d = {}
        for field in fields(self):
            if field.name == "extra":
                continue
            json_name = field.metadata["json"] if "json" in field.metadata else field.name
            json_value = self.__dict__[field.name]
            if json_value is not None:
                if isinstance(json_value, Enum):
                    d[json_name] = json_value.value
                else:  
                    d[json_name] = json_value

        extra_d = { f"extra_{k}": v for k, v in self.extra.items() }

        d.update(extra_d)
            
        return d
    
    def to_json(self) -> str:
        return dumps(self.to_dict())        

    def equals(self, to: OAMObject):
        return self.to_dict() == to.to_dict()
