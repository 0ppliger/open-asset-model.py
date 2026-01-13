from dataclasses import fields
from typing import Type, TypeVar, cast
import inspect
import asset_model
from asset_model import OAMObject
from asset_model import Asset, AssetType, AssetList
from asset_model import Relation, RelationType, RelationList
from asset_model import Property, PropertyType, PropertyList

T = TypeVar("T", bound="OAMObject")

def _get_oam_obj_by_name(name: str) -> Type[OAMObject]:
    for [_name, cls] in inspect.getmembers(asset_model, inspect.isclass):
        if _name == name:
            return cast(type[OAMObject], cls)

    raise Exception("unsupported oam object")

def get_property_by_type(type: PropertyType) -> Type[Property]:
    if type not in PropertyList:
        raise Exception("unsupported relation type")
    return cast(Type[Property], _get_oam_obj_by_name(type.value))

def get_relation_by_type(type: RelationType) -> Type[Relation]:
    if type not in RelationList:
        raise Exception("unsupported relation type")
    return cast(Type[Relation], _get_oam_obj_by_name(type.value))

def get_asset_by_type(type: AssetType) -> Type[Asset]:
    if type not in AssetList:
        raise Exception("unsupported asset type")
    return cast(Type[Asset], _get_oam_obj_by_name(type.value))

TypeResult = type[Asset] | type[Property] | type[Relation]

def describe_type(o: TypeResult | AssetType | PropertyType | RelationType) -> list:
    _o: TypeResult
    match o:
        case AssetType():
            _o = get_asset_by_type(o)
        case PropertyType():
            _o = get_property_by_type(o)
        case RelationType():
            _o = get_relation_by_type(o)
        case _:
            _o = o
    
    d = []
    for field in fields(_o):
        json_name = field.metadata["json"] if "json" in field.metadata else field.name
        d.append(json_name)

    return d
