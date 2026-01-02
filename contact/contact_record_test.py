import pytest
import json
from contact.contact_record import ContactRecord
from asset import Asset
from asset import AssetType

def test_contact_record_key():
    want = "https://owasp.org/contacts"
    cr = ContactRecord(discovered_at=want)
    
    assert cr.key == want

def test_contact_record_asset_type():
    cr = ContactRecord(discovered_at="https://owasp.org/contacts")
    
    assert issubclass(ContactRecord, Asset)
    assert cr.asset_type == AssetType.ContactRecord

def test_contact_record_json():
    cr = ContactRecord(discovered_at="https://owasp.org")
    
    expected_json = json.dumps({"discovered_at": "https://owasp.org"})
    
    json_data = cr.to_json()
    
    assert json_data == expected_json
