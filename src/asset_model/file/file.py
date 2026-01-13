from mimetypes import guess_type
from urllib.parse import urlparse
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from asset_model.asset import Asset, AssetType

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

    @staticmethod
    def from_url(url: str) -> 'File':
        filename = Path(urlparse(url).path).name
        filetype,_ = guess_type(filename)
        return File(
            url  = url,
            name = filename,
            type = filetype
        )
        
