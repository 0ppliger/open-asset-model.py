from asset_model import AssetType, RelationType, OAMObject, FQDN, BasicDNSRelation
from asset_model import URL

def test_clone_works():
    orig = URL.from_text("http://exemple.com/")
    copy = orig.clone()

    assert orig.strict_equals(copy)

def test_is_fresher_than_works():
    # is_fresher_than returns True if common keys have different values
    a = URL("http://exemple.com/", host="foo")
    b = URL("http://exemple.com/", host="bar")

    assert a.is_fresher_than(b) == True

    # is_fresher_than returns True if a have keys that b don't have
    a = URL("http://exemple.com/", host="foo")
    b = URL("http://exemple.com/")

    assert a.is_fresher_than(b) == True
    # is_fresher_than returns False if b have keys that a don't have
    a = URL("http://exemple.com/")
    b = URL("http://exemple.com/", host="foo")

    assert a.is_fresher_than(b) == False

    # is_fresher_than returns False if b don't have additional key
    a = URL("http://exemple.com/")
    b = URL("http://exemple.com/", host="foo")

    assert a.is_fresher_than(b) == False

def test_override_with_works():
    # override_with must replace overrided fields
    old = URL("http://exemple.com/")
    new = URL("http://www.exemple.com/")
    overrided = old.override_with(new)

    assert overrided.raw == "http://www.exemple.com/"

    # override_with must forward non overrided fields
    old = URL("http://exemple.com/", host="exemple.com")
    new = URL("http://exemple.com/", scheme="http")
    overrided = old.override_with(new)

    assert overrided.raw    == "http://exemple.com/"
    assert overrided.host   == "exemple.com"
    assert overrided.scheme == "http"

def test_from_dict():
    d = {
        "name": "dns_record",
        "header": {
            "rr_type": 1,
            "cls": 1,
            "ttl": 1
        }
    }
    rel = OAMObject.from_dict(BasicDNSRelation, d)
    print(rel)
    assert rel.name == "dns_record"
    assert rel.header.rrtype == 1
