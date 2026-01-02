from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
from asset import Asset, AssetType

@dataclass
class Organization(Asset):
    """Organization represents an organization.
    Should support relationships for the following:
    - Principal place of business
    - Parent organizations
    - Subsidiaries
    - Sister companies
    - DUNS number
    - Tax identification number
    - Trader identification number
    - ARIN organization identifier
    - Decentralized identifier (DID)
    - Ticker symbol
    - Global Location Number (GLN)
    - ISIC, NAICS, SIC, BIC, and ISO 6523 code
    - Legal Entity Identifier (LEI) ISO 17442 code
    - Registration number
    - Website
    - Social media profiles
    - Contact information
    - Founder, sponsorships, and funding sources
    """
    id: str
    name: str
    legal_name:      Optional[str] = None
    founding_date:   Optional[str] = None
    jurisdiction:    Optional[str] = None
    registration_id: Optional[str] = None
    industry:        Optional[str] = None
    target_markets:  Optional[List[str]] = None
    active:          Optional[bool] = None
    non_profit:      Optional[bool] = None
    headcount:       Optional[int] = None

    @property
    def key(self) -> str:
        return self.id

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Organization

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "unique_id": self.id,
            "name": self.name,
            "legal_name": self.legal_name,
            "founding_date": self.founding_date,
            "jurisdiction": self.jurisdiction,
            "registration_id": self.registration_id,
            "industry": self.industry,
            "target_markets": self.target_markets,
            "active": self.active,
            "non_profit": self.non_profit,
            "headcount": self.headcount,
        }.items() if value is not None}
