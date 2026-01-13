from dataclasses import dataclass
from typing import List, Optional
from asset_model.asset import Asset
from asset_model.asset import AssetType


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
