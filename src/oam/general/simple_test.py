import pytest
import json
from oam.general.simple import SimpleRelation
from oam.general.simple import SimpleProperty
from oam.property import Property
from oam.property import PropertyType
from oam.relation import Relation
from oam.relation import RelationType


def test_simple_relation_name():
    want = "anything"
    sr = SimpleRelation(name=want)
    
    assert sr.label == want


def test_simple_relation_implements_relation():
    assert issubclass(SimpleRelation, Relation)


def test_simple_relation():
    sr = SimpleRelation(name="anything")

    assert sr.name == "anything"
    assert sr.relation_type == RelationType.SimpleRelation

    json_data = sr.to_json()
    assert json_data == json.dumps({"label":"anything"})


def test_simple_property_name():
    want = "anything"
    sp = SimpleProperty(property_name="anything", property_value="foobar")

    assert sp.name == want


def test_simple_property_value():
    want = "foobar"
    sp = SimpleProperty(property_name="anything", property_value="foobar")

    assert sp.value == want


def test_simple_property_implements_property():
    assert issubclass(SimpleProperty, Property)


def test_simple_property():
    sp = SimpleProperty(property_name="anything", property_value="foobar")

    assert sp.property_name == "anything"
    assert sp.property_value == "foobar"
    assert sp.property_type == PropertyType.SimpleProperty

    json_data = sp.to_json()
    assert json_data == json.dumps({"property_name":"anything", "property_value":"foobar"})
