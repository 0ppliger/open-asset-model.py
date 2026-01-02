from dataclasses import dataclass
from asset import Asset
from asset import AssetType
from typing import Optional
from urllib.parse import urlparse

@dataclass
class URL(Asset):
    """URL represents a URL."""
    raw:      str
    scheme:   str
    host:     str
    path:     str
    username: Optional[str] = None
    password: Optional[str] = None
    port:     Optional[int] = None
    options:  Optional[str] = None
    fragment: Optional[str] = None

    @property
    def key(self) -> str:
        return self.raw

    @property
    def asset_type(self) -> AssetType:
        return AssetType.URL

    @staticmethod
    def from_text(url: str) -> 'URL':
        o = urlparse(url)
        return URL(
            raw=url,
            scheme=o.scheme,
            host=o.hostname or "",
            path=o.path,
            username=o.username,
            password=o.password,
            port=o.port,
            options=o.query,
            fragment=o.fragment
        )
    
    def to_dict(self) -> dict:
        return {
            key: value for key, value in {
                'url': self.raw,
                'scheme': self.scheme,
                'host': self.host,
                'path': self.path,
                'username': self.username,
                'password': self.password,
                'port': self.port,
                'options': self.options,
                'fragment': self.fragment
            }.items() if value is not None}
