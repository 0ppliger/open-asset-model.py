from dataclasses import dataclass
from asset import Asset
from asset import AssetType
from typing import Optional
from enum import Enum

@dataclass
class Account(Asset):
    """Account represents an account managed by an organization.
    
    Should support relationships for the following:
    - User (e.g. Person or Organization)
    - Funds transfers
    - IBAN and SWIFT codes
    """
    id:             str
    account_type:   str
    username:       Optional[str] = None
    account_number: Optional[str] = None
    balance:        Optional[float] = None
    active:         Optional[bool] = None

    @property
    def key(self) -> str:
        return self.id

    @property
    def asset_type(self) -> AssetType:
        return AssetType.Account

    def to_dict(self) -> dict:
        return {
            key: value for key, value in {
                "unique_id": self.id,
                "account_type": self.account_type,
                "username": self.username,
                "account_number": self.account_number,
                "balance": self.balance,
                "active": self.active,
            }.items() if value is not None}
