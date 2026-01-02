import json
import pytest
from general.identifier import Identifier
from general.identifier import IdentifierType
from asset import AssetType

def test_identifier_key():
    want = "Legal Entity Identifier:549300XMYB546ZI1F126"
    i = Identifier(
        unique_id=want,
        id="549300XMYB546ZI1F126",
        type=IdentifierType.LEICode
    )
    
    assert i.key == want

def test_identifier_asset_type():
    i = Identifier(unique_id="", id="",
        type=IdentifierType.LEICode)
    
    expected = AssetType.Identifier
    actual = i.asset_type
    
    assert actual == expected

def test_identifier_json():
    i = Identifier(
        unique_id="Legal Entity Identifier:549300XMYB546ZI1F126",
        id="549300XMYB546ZI1F126",
        type=IdentifierType.LEICode,
        creation_date="2013-07-24T14:15:00Z",
        updated_date="2023-08-04T17:33:45Z",
        expiration_date="2020-01-16T00:32:00Z",
        status="ACTIVE"
    )
    
    expected = json.dumps({"unique_id":"Legal Entity Identifier:549300XMYB546ZI1F126","id":"549300XMYB546ZI1F126","id_type":"lei","creation_date":"2013-07-24T14:15:00Z","update_date":"2023-08-04T17:33:45Z","expiration_date":"2020-01-16T00:32:00Z","status":"ACTIVE"})
    actual = i.to_json()

    assert actual == expected
