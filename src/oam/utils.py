import inspect
from oam.oam_object import OAMObject
import oam

def _get_oam_obj_by_name(name: str) -> OAMObject:
    for [_name, cls] in inspect.getmembers(oam, inspect.isclass):
        if _name == name:
            return cls

    raise Exception("unsupported oam object")

def get_property_by_type(type: oam.PropertyType) -> oam.Asset:
    if type not in oam.PropertyList:
        raise Exception("unsupported relation type")
    return _get_oam_obj_by_name(type.value)

def get_relation_by_type(type: oam.RelationType) -> oam.Asset:
    if type not in oam.RelationList:
        raise Exception("unsupported relation type")
    return _get_oam_obj_by_name(type.value)

def get_asset_by_type(type: oam.AssetType) -> oam.Asset:
    if type not in oam.AssetList:
        raise Exception("unsupported asset type")
    return _get_oam_obj_by_name(type.value)

