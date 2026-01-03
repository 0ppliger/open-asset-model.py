import json
from abc import ABC
from abc import abstractmethod
from enum import Enum

class AssetType(Enum):
    Account = "Account"
    AutnumRecord = "AutnumRecord"
    AutonomousSystem = "AutonomousSystem"
    ContactRecord = "ContactRecord"
    DomainRecord = "DomainRecord"
    File = "File"
    FQDN = "FQDN"
    FundsTransfer = "FundsTransfer"
    Identifier = "Identifier"
    IPAddress = "IPAddress"
    IPNetRecord = "IPNetRecord"
    Location = "Location"
    Netblock = "Netblock"
    Organization = "Organization"
    Person = "Person"
    Phone = "Phone"
    Product = "Product"
    ProductRelease = "ProductRelease"
    Service = "Service"
    TLSCertificate = "TLSCertificate"
    URL = "URL"

class Asset(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        pass

    @property
    @abstractmethod
    def asset_type(self) -> AssetType:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())

AssetList = list(AssetType)
