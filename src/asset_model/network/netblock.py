from dataclasses import dataclass
from asset_model.asset import Asset
from asset_model.asset import AssetType
from enum import Enum

class NetblockType(str, Enum):
    IPv4 = "IPv4"
    IPv6 = "IPv6"

@dataclass
class Netblock(Asset):
    """Netblock represents a block of IP addresses in a network."""
    cidr: str
    type: NetblockType

    @property
    def key(self) -> str:
        return self.cidr

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Netblock
