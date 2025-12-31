from dataclasses import dataclass
from asset import AssetType
from asset import Asset

@dataclass
class FQDN(Asset):
    """FQDN represents a Fully Qualified Domain Name."""
    name: str
    
    @property
    def key(self) -> str:
        return self.name

    @property
    def asset_type(self) -> AssetType:
        return AssetType.FQDN

    def to_dict(self) -> dict:
        return {
            'name': self.key
        }
