import inspect
from typing import cast
from oam.oam_object import OAMObject
import oam

def _get_oam_obj_by_name(name: str) -> OAMObject:
    for [_name, cls] in inspect.getmembers(oam, inspect.isclass):
        if _name == name:
            return cast(OAMObject, cls)

    raise Exception("unsupported oam object")

def get_property_by_type(type: oam.PropertyType) -> oam.Property:
    if type not in oam.PropertyList:
        raise Exception("unsupported relation type")
    return cast(oam.Property, _get_oam_obj_by_name(type.value))

def get_relation_by_type(type: oam.RelationType) -> oam.Relation:
    if type not in oam.RelationList:
        raise Exception("unsupported relation type")
    return cast(oam.Relation, _get_oam_obj_by_name(type.value))

def get_asset_by_type(type: oam.AssetType) -> oam.Asset:
    if type not in oam.AssetList:
        raise Exception("unsupported asset type")
    return cast(oam.Asset, _get_oam_obj_by_name(type.value))

