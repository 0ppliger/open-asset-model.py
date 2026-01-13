import json
import pytest
from asset_model.pf.service import Service
from asset_model.property import PropertyType
from asset_model.relation import RelationType
from asset_model.asset import AssetType

def test_service_key():
    want = "222333444"
    serv = Service(id=want, type="HTTP")
    assert serv.key == want

def test_service_asset_type():
    s = Service(id="dummy", type="dummy")
    want = AssetType.Service
    assert s.asset_type == want

def test_service_json():
    s = Service(
        id="222333444",
        type="HTTP",
        output="Hello",
        output_len=5,
        attributes={"server": ["nginx-1.26.0"]}
    )

    expected_json = {
        "unique_id": "222333444",
        "service_type": "HTTP",
        "output": "Hello",
        "output_length": 5,
        "attributes": {"server": ["nginx-1.26.0"]}}
    json_data = s.to_dict()
    assert json_data == expected_json
