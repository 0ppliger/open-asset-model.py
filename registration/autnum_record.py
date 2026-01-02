from dataclasses import dataclass
from typing import List, Optional
from asset import Asset
from asset import AssetType


@dataclass
class AutnumRecord(Asset):
    """AutnumRecord represents the RDAP record for an autonomous
    system."""
    number:       int
    handle:       str
    name:         str
    created_date: str
    updated_date: str
    raw:          Optional[str] = None
    whois_server: Optional[str] = None
    status:       Optional[List[str]] = None

    @property
    def key(self) -> str:
        return self.handle

    @property
    def asset_type(self) -> AssetType:
        return AssetType.AutnumRecord

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "raw": self.raw,
            "number": self.number,
            "handle": self.handle,
            "name": self.name,
            "whois_server": self.whois_server,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "status": self.status,
        }.items() if value is not None}
