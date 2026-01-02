from dataclasses import dataclass
from typing import Optional
from asset import Asset
from asset import AssetType

@dataclass
class Location(Asset):
    """Location represents the street address location."""
    address:         str
    city:            Optional[str] = None
    building:        Optional[str] = None
    building_number: Optional[str] = None
    street_name:     Optional[str] = None
    unit:            Optional[str] = None
    po_box:          Optional[str] = None
    locality:        Optional[str] = None
    province:        Optional[str] = None
    country:         Optional[str] = None
    postal_code:     Optional[str] = None
    gln:             Optional[int] = None

    @property
    def key(self) -> str:
        return self.address

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Location

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "address": self.address,
            "building": self.building,
            "building_number": self.building_number,
            "street_name": self.street_name,
            "unit": self.unit,
            "po_box": self.po_box,
            "city": self.city,
            "locality": self.locality,
            "province": self.province,
            "country": self.country,
            "postal_code": self.postal_code,
            "gln": self.gln,
        }.items() if value is not None}
