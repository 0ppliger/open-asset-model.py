import json
from json import JSONDecodeError
from dns.fqdn import FQDN
from asset import Asset
from asset import AssetType

def test_fqdn_key():
    want = "example.com"
    fqdn = FQDN(name=want)

    assert fqdn.key == want

def test_fqdn_implements_asset():
    assert issubclass(FQDN, Asset)

def test_successful_creation_of_fqdn_with_valid_name_and_tld():
    fqdn = FQDN(name="foo.example.com")
    
    assert fqdn.name == "foo.example.com"
    assert fqdn.asset_type == AssetType.FQDN

def test_successful_json_serialization_of_fqdn_with_valid_name_and_tld():
    fqdn = FQDN(name="foo.example.com")

    try:
        json_data = fqdn.to_json()
    except JSONDecodeError as err:
        pytest.fail(err)
    expected_json = {"name":"foo.example.com"}
    assert json_data == json.dumps(expected_json)
