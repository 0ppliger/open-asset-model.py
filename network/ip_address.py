from dataclasses import dataclass
from asset import Asset
from asset import  AssetType
from enum import Enum

class IPAddressType(Enum):
    IPv4 = "IPv4"
    IPv6 = "IPv6"

@dataclass
class IPAddress(Asset):
    """IPAddress represents an IP address."""
    address: str
    type:    IPAddressType

    @property
    def key(self) -> str:
        return self.address

    @property
    def asset_type(self) -> AssetType:
        return AssetType.IPAddress

    def to_dict(self) -> dict:
        return {
            'address': self.address,
            'type': self.type.value
        }
