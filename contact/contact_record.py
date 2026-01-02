from dataclasses import dataclass
from asset import Asset
from asset import AssetType

@dataclass
class ContactRecord(Asset):
    """ContactRecord links various assets together to form complete contact information."""
    discovered_at: str

    @property
    def key(self) -> str:
        return self.discovered_at

    @property
    def asset_type(self) -> AssetType:
        return AssetType.ContactRecord

    def to_dict(self) -> dict:
        return {
            "discovered_at": self.discovered_at,
        }
