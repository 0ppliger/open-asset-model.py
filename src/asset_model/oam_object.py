from __future__ import annotations
from abc import ABC
from json import dumps
from dataclasses import fields
from dataclasses import dataclass
from typing import Any
from typing import TypeVar, Type
from typing import cast
from typing import Mapping
from enum import Enum

T = TypeVar("T", bound="OAMObject")


@dataclass(kw_only=True)
class OAMObject(ABC):
    @staticmethod
    def from_dict(o: Type[T], d: Mapping[str, Any]) -> T:
        real_d = {}
        o_fields = fields(cast(Any, o))
        for key, value in d.items():
            for field in o_fields:
                if ("json" in field.metadata and field.metadata["json"] == key) \
                   or field.name == key:
                    if isinstance(field.type, type) \
                       and issubclass(field.type, OAMObject):
                        value = OAMObject.from_dict(field.type, value)
                    real_d[field.name] = value
                    break

        return o(**real_d)

    def to_dict(self) -> dict:
        d = {}
        for field in fields(self):
            json_name = field.metadata["json"] if "json" in field.metadata else field.name
            json_value = self.__dict__[field.name]
            if json_value is not None:
                if isinstance(json_value, Enum):
                    d[json_name] = json_value.value
                elif isinstance(json_value, OAMObject):
                    d[json_name] = json_value.to_dict()
                else:
                    d[json_name] = json_value

        return d

    def to_json(self) -> str:
        return dumps(self.to_dict())

    def clone(self):
        return OAMObject.from_dict(type(self), self.to_dict())

    def equals(self, to: OAMObject):
        return self.to_dict() == to.to_dict()

    def strict_equals(self, to: OAMObject):
        return self.to_dict() == to.to_dict()

    def is_fresher_than(self, obj: OAMObject) -> bool:
        asset_cls = type(self)
        if not isinstance(obj, asset_cls):
            raise Exception("both objects must instanciate the same OAM object type")

        old_dict = obj.to_dict()
        new_dict = self.to_dict()

        # Check for common keys with different values
        common_keys = set(old_dict.keys()) & set(new_dict.keys())
        for key in common_keys:
            if old_dict[key] != new_dict[key]:
                return True

        # Check for keys present in new_dict but not in old_dict
        new_only_keys = set(new_dict.keys()) - set(old_dict.keys())
        if new_only_keys:
            return True

        return False

    def override_with(self, obj: T) -> T:
        asset_cls = type(obj)
        if not isinstance(self, asset_cls):
            raise Exception("both objects must instanciate the same OAM object type")

        merged_dict = dict(self.to_dict())
        merged_dict.update(obj.to_dict())

        return OAMObject.from_dict(asset_cls, merged_dict)
