from dataclasses import dataclass
from typing import Optional, List
from oam.asset import Asset
from oam.asset import AssetType

@dataclass
class IPNetRecord(Asset):
    """IPNetRecord represents the RDAP record for an IP network."""
    cidr:          str
    handle:        str
    type:          str
    name:          str
    created_date:  str
    updated_date:  str
    start_address: str
    end_address:   str
    raw:           Optional[str]  = None
    method:        Optional[str] = None
    country:       Optional[str] = None
    parent_handle: Optional[str] = None
    whois_server:  Optional[str] =  None
    status:        Optional[List[str]] =  None

    @property
    def key(self) -> str:
        return self.handle

    @property
    def asset_type(self) -> AssetType:
        return AssetType.IPNetRecord

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "raw": self.raw,
            "cidr": str(self.cidr),
            "handle": self.handle,
            "start_address": str(self.start_address),
            "end_address": str(self.end_address),
            "type": self.type,
            "name": self.name,
            "method": self.method,
            "country": self.country,
            "parent_handle": self.parent_handle,
            "whois_server": self.whois_server,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "status": self.status,
        }.items() if value is not None}
