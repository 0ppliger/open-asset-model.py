from dataclasses import dataclass
from asset import Asset
from asset import AssetType

@dataclass
class AutonomousSystem(Asset):
    """AutonomousSystem represents an autonomous system."""
    number: int

    @property
    def key(self) -> str:
        return str(self.number)

    @property
    def asset_type(self) -> AssetType:
        return AssetType.AutonomousSystem

    def to_dict(self) -> dict:
        return {'number': self.number}
