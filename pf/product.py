from dataclasses import dataclass
from typing import Optional
from enum import Enum
from asset import Asset
from asset import AssetType

@dataclass
class Product(Asset):
    """Product represents a technology product and organizes the
    product releases in the data model.
    
    Should support relationships for the following:
    - Manufacturer (e.g. Organization)
    - Website
    - Product releases
    """
    id:                str
    name:              str
    type:              str
    category:          Optional[str] = None
    description:       Optional[str] = None
    country_of_origin: Optional[str] = None

    @property
    def key(self) -> str:
        return self.id

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Product

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "unique_id": self.id,
            "product_name": self.name,
            "product_type": self.type,
            "category": self.category,
            "description": self.description,
            "country_of_origin": self.country_of_origin,
        }.items() if value is not None}

@dataclass
class ProductRelease(Asset):
    """ProductRelease represents a release of a technology product
    that belongs to a Product.

    Should support relationships for the following:
    - Amazon Standard Identification Number (ASIN)
    - Global Trade Item Number (GTIN)
    - International Article Number (EAN)
    - International Standard Book Number (ISBN)
    - Manufacturer Part Number (MPN)
    - Model Number
    - NATO Stock Number (NSN)
    - Serial Number
    - Universal Product Code (UPC)
    - Version Number
    - Vulnerabilities
    - Website with release details

    """
    name: str
    release_date: Optional[str] = None

    @property
    def key(self) -> str:
        return self.name

    @property
    def asset_type(self) -> AssetType:
        return AssetType.ProductRelease

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "name": self.name,
            "release_date": self.release_date,
        }.items() if value is not None}
