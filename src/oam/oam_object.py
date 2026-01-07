from __future__ import annotations
from abc import ABC
from json import dumps
from dataclasses import fields
from dataclasses import dataclass
from dataclasses import is_dataclass
from typing import Any
    
def _to_dict(o: Any):
    d = {}
    for field in fields(o):
        json_name = field.metadata["json"] if "json" in field.metadata else field.name
        json_value = o.__dict__[field.name]
        if is_dataclass(json_value):
            for key, val in _to_dict(json_value).items():
                d[f"{json_name}_{key}"] = val
        elif json_value is not None:
            d[json_name] = json_value
    return d

@dataclass
class OAMObject(ABC):
    def to_dict(self) -> dict:
        return _to_dict(self)
    
    def to_json(self) -> str:
        return dumps(self.to_dict())
