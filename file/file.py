from dataclasses import dataclass
from typing import Optional
from asset import Asset, AssetType

@dataclass
class File(Asset):
    """File represents a file discovered, such as a document or image."""
    url: str
    name: Optional[str] = None
    type: Optional[str] = None

    @property
    def key(self) -> str:
        return self.url

    @property
    def asset_type(self) -> AssetType:
        return AssetType.File

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "url": self.url,
            "name": self.name,
            "type": self.type,
        }.items() if value is not None}
