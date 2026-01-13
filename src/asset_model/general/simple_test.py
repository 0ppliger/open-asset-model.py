import pytest
import json
from asset_model.general.simple import SimpleRelation
from asset_model.general.simple import SimpleProperty
from asset_model.property import Property
from asset_model.property import PropertyType
from asset_model.relation import Relation
from asset_model.relation import RelationType


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

    expected = {"label":"anything"}
    assert sr.to_dict() == expected


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

    expected_json = {
        "property_name":"anything",
        "property_value":"foobar"
    }
    assert sp.to_dict() == expected_json
