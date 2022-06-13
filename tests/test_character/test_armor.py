"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the armor class and its interations with the equipment class.
"""

import pytest

from funclg.character.armor import Armor
from funclg.character.equipment import BodyEquipment
from funclg.utils.types import ITEM_TYPES

from .fixtures.armor_fixtures import (
    armor_details_expectations,
    armor_export_expectations,
    armor_str_expectations,
    equipment_only,
    heavy_armor_sword,
    light_armor_knife,
    medium_armor_wand,
    medium_half_armor,
    armor_details_missing_weapon,
)


def test_armor_init(light_armor_knife, medium_armor_wand, heavy_armor_sword):
    for item in ITEM_TYPES:
        item = item.lower()
        print(light_armor_knife)
        assert getattr(light_armor_knife, item, False)
        assert getattr(medium_armor_wand, item, False)
        assert getattr(heavy_armor_sword, item, False)


def test_armor_validate_equipment_not_equipment():
    armor = Armor(1, "FUN HEAD FAIL")
    assert armor.head == None


def test_armor_validate_equipment_wrong_slot():
    armor = Armor(
        1,
        weapon=BodyEquipment(
            name="Head Piece", description="Item in wrong slot", armor_type=1, item_type=0
        ),
    )
    assert armor.weapon == None


def test_armor_str(medium_half_armor, heavy_armor_sword, armor_str_expectations):
    empty_armor = Armor(0)
    armors = [medium_half_armor, heavy_armor_sword, empty_armor]
    for expectation, armor in zip(armor_str_expectations, armors):
        assert expectation == armor.__str__()


def test_armor_equipping(equipment_only):
    armor = Armor()
    assert armor.armor_type == 0
    assert armor.head == None
    assert armor.chest == None
    assert armor.back == None
    assert armor.pants == None
    assert armor.weapon == None

    for item in equipment_only.values():
        armor.equip(item)

    for item in ITEM_TYPES:
        item = item.lower()
        assert getattr(armor, item, False)

def test_armor_equipping_error(equipment_only):
    armor = Armor(1)

    for item in equipment_only.values():
        armor.equip(item)

    assert armor.head == None
    assert armor.chest == None
    assert armor.back == None
    assert armor.pants == None
    assert armor.weapon == None


def test_armor_dequipping(light_armor_knife):
    for item_type in ITEM_TYPES:
        light_armor_knife.dequip(item_type)

    assert light_armor_knife.armor_type == 0
    assert light_armor_knife.head == None
    assert light_armor_knife.chest == None
    assert light_armor_knife.back == None
    assert light_armor_knife.pants == None
    assert light_armor_knife.weapon == None


def test_armor_get_equipment(equipment_only):
    armor = Armor()
    assert armor.armor_type == 0
    assert armor.head == None
    assert armor.chest == None
    assert armor.back == None
    assert armor.pants == None
    assert armor.weapon == None

    for item in equipment_only.values():
        armor.equip(item)

    for items in zip(equipment_only.values(), armor.get_equipment()):
        assert items[0].name == items[1].name
        assert items[0].item_type == items[1].item_type


def test_armor_export(equipment_only, armor_export_expectations):
    armor = Armor(0)
    for item in equipment_only.values():
        armor.equip(item)
    assert armor.export() == armor_export_expectations


def test_armor_equip_wrong_slot(equipment_only):
    armor = Armor()
    armor._equip_chest(equipment_only["Back"])

    assert armor.chest == None
    assert armor.back == None

    # Right side
    armor.equip(equipment_only["Back"])
    assert armor.back != None
    assert isinstance(armor.back, BodyEquipment)


def test_armor_details_format(light_armor_knife, armor_details_expectations):
    for indent, expectation in enumerate(armor_details_expectations):
        assert light_armor_knife.details(indent) == expectation
    
def test_armor_details_missing_item(light_armor_knife, armor_details_missing_weapon):
    light_armor_knife.dequip("weapon")
    assert light_armor_knife.details() == armor_details_missing_weapon

def test_armor_stat_info(light_armor_knife):
    assert light_armor_knife.stat.level == None
    current_stats = light_armor_knife.get_stats()
    light_armor_knife.dequip("weapon")
    light_armor_knife.dequip("chest")
    
    for key, value in light_armor_knife.get_stats().items():
        if key == "level":
            assert value == None
        else:
            assert value <= current_stats[key]