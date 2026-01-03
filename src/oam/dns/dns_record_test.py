import pytest
from oam.dns.dns_record import BasicDNSRelation
from oam.dns.dns_record import PrefDNSRelation
from oam.dns.dns_record import SRVDNSRelation
from oam.dns.dns_record import RRHeader
from oam.dns.dns_record import DNSRecordProperty
from oam.relation import Relation
from oam.relation import RelationType
from oam.property import Property
from oam.property import PropertyType
import json

def test_basic_dns_relation_name():
    want = "dns_record"
    br = BasicDNSRelation(
        name=want,
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
    )

    assert br.label == want

def test_basic_dns_relation_implements_relation():
    assert issubclass(BasicDNSRelation, Relation)

def test_basic_dns_relation():
    dr = BasicDNSRelation(
        name="dns_record",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
    )

    assert dr.name == "dns_record"
    assert dr.header.rr_type == 1
    assert dr.header.cls == 1
    assert dr.header.ttl == 86400
    assert dr.relation_type == RelationType.BasicDNSRelation

    json_data = dr.to_json()
    expected_json = {
        "label": "dns_record",
        "header": {"rr_type": 1, "class": 1, "ttl": 86400}
    }
    assert json.loads(json_data) == expected_json

def test_pref_dns_relation_name():
    want = "dns_record"
    br = PrefDNSRelation(
        name=want,
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        preference=5,
    )

    assert br.label == want

def test_pref_dns_relation_implements_relation():
    assert issubclass(PrefDNSRelation, Relation)

def test_pref_dns_relation():
    pr = PrefDNSRelation(
        name="dns_record",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        preference=5,
    )

    assert pr.name == "dns_record"
    assert pr.header.rr_type == 1
    assert pr.header.cls == 1
    assert pr.header.ttl == 86400
    assert pr.preference == 5
    assert pr.relation_type is RelationType.PrefDNSRelation

    json_data = pr.to_json()
    expected_json = {
        "label": "dns_record",
        "header": {"rr_type": 1, "class": 1, "ttl": 86400},
        "preference": 5,
    }
    assert json.loads(json_data) == expected_json

def test_srv_dns_relation_name():
    want = "dns_record"
    br = SRVDNSRelation(
        name="dns_record",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        priority=10,
        weight=5,
        port=80
    )

    assert br.label == want

def test_srv_dns_relation_implements_relation():
    assert issubclass(SRVDNSRelation, Relation)

def test_srv_dns_relation():
    sr = SRVDNSRelation(
        name="dns_record",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        priority=10,
        weight=5,
        port=80
    )

    assert sr.name == "dns_record"
    assert sr.header.rr_type == 1
    assert sr.header.cls == 1
    assert sr.header.ttl == 86400
    assert sr.priority == 10
    assert sr.weight == 5
    assert sr.port == 80
    assert sr.relation_type is RelationType.SRVDNSRelation

    json_data = sr.to_json()
    expected_json = {
        "label": "dns_record",
        "header": {"rr_type": 1, "class": 1, "ttl": 86400},
        "priority": 10,
        "weight": 5,
        "port": 80,
    }
    assert json.loads(json_data) == expected_json

def test_dns_record_property_name():
    p = DNSRecordProperty(
        property_name="anything",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        data="foobar"
    )

    assert p.name == "anything"

def test_dns_record_property_value():
    p = DNSRecordProperty(
        property_name="anything",
        header=RRHeader(rr_type=1, cls=1, ttl=86400),
        data="foobar"
    )

    assert p.value == "foobar"

def test_dns_record_property_implements_property():
    assert issubclass(DNSRecordProperty, Property)

def test_dns_record_property():
    p = DNSRecordProperty(
        property_name="anything",
        header=RRHeader(rr_type=16, cls=1, ttl=86400),
        data="foobar"
    )

    assert p.property_name == "anything"
    assert p.data == "foobar"
    assert p.property_type is PropertyType.DNSRecordProperty

    json_data = p.to_json()
    expected_json = {
        "property_name": "anything",
        "header": {"rr_type": 16, "class": 1, "ttl": 86400},
        "data": "foobar"
    }
    assert json.loads(json_data) == expected_json
