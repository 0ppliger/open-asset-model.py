from dataclasses import dataclass
from typing import Optional, Dict, List
from oam.property import PropertyType
from oam.relation import RelationType
from oam.asset import Asset
from oam.asset import AssetType

@dataclass
class Service(Asset):
    """Service represents a service provided by an asset and/or organization.
    It should support relationships such as the following:
    - Provider (e.g. Organization)
    - Terms of service (e.g. File or URL)
    - TLS Certificate (e.g. TLSCertificate)
    - Product used to provide the service (e.g. Product or ProductRelease)
    """
    id: str
    type: str
    output: Optional[str] = None
    output_len: Optional[int] = None
    attributes: Optional[Dict[str, List[str]]] = None

    @property
    def key(self) -> str:
        return self.id

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Service

    def to_dict(self) -> dict:
        return {
            "unique_id": self.id,
            "service_type": self.type,
            **{key: value for key, value in {
                "output": self.output,
                "output_length": self.output_len,
                "attributes": self.attributes
            }.items() if value is not None}
        }
