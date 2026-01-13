from dataclasses import dataclass
from asset_model.asset import AssetType
from asset_model.asset import Asset
from fqdn import FQDN as _FQDN

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

    @staticmethod
    def from_text(fqdn: str) -> 'FQDN':
        if not _FQDN(fqdn).is_valid:
            raise ValueError("invalid fqdn")
        return FQDN(name=fqdn)
