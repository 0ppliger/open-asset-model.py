from dataclasses import dataclass
from asset import Asset
from asset import AssetType
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

    def to_dict(self) -> dict:
        return {
            'cidr': self.cidr,
            'type': self.type.value
        }
