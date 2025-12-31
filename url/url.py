from dataclasses import dataclass, asdict
from asset import Asset, AssetType
import json
from typing import Optional

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

    def to_dict(self) -> dict:
        return {
            key: value for key, value in {
                'raw': self.raw,
                'scheme': self.scheme,
                'host': self.host,
                'path': self.path,
                'username': self.username,
                'password': self.password,
                'port': self.port,
                'options': self.options,
                'fragment': self.fragment
            }.items() if value is not None}
