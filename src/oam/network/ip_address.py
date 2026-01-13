from dataclasses import dataclass
from oam.asset import Asset
from oam.asset import  AssetType
from enum import Enum
from ipaddress import ip_address
from ipaddress import IPv4Address, IPv6Address

class IPAddressType(str, Enum):
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

    @staticmethod
    def from_text(address: str) -> 'IPAddress':
        try:
            ip_type = IPAddressType.IPv4 \
                if type(ip_address(address)) is IPv4Address \
                else IPAddressType.IPv6
        except ValueError as e:
            raise e
            
        return IPAddress(address, ip_type)
