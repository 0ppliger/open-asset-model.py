from dataclasses import dataclass
from enum import Enum
from typing import Optional
from asset import Asset, AssetType

@dataclass
class Person(Asset):
    """Person represents a person's information."""
    id:          str
    full_name:   str
    first_name:  Optional[str] = None
    family_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date:  Optional[str] = None
    gender:      Optional[str] = None

    @property
    def key(self) -> str:
        return self.id

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Person

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "unique_id": self.id,
            "full_name": self.full_name,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "family_name": self.family_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
        }.items() if value is not None}
