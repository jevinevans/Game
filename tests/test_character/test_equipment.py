"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""

from unittest.mock import patch

import pytest

from FUNCLG.character.equipment import BodyEquipment, Equipment, WeaponEquipment
from FUNCLG.character.modifiers import Modifier
from FUNCLG.utils.types import ARMOR_TYPES, ITEM_TYPES, WEAPON_TYPES

from .fixtures.equipment_fixures import (
    bodyequipment_all_items_mods,
    bodyequipment_all_types,
    bodyequipment_details_expectation,
    bodyequipment_mods,
    equipment_str_expectation,
    weaponequipment_all_types,
    weaponequipment_description_expectations,
)


# =========================== #
# Testing Equipment Functions #
# =========================== #
def test_equipment_str(
    weaponequipment_all_types, bodyequipment_all_types, equipment_str_expectation
):
    # Test Body Equipment
    for name, body in bodyequipment_all_types.items():
        assert body.__str__() == equipment_str_expectation[name]

    # Test weapon Equipment
    for name, weapon in weaponequipment_all_types.items():
        assert weapon.__str__() == equipment_str_expectation[name]


@patch("builtins.open")
@patch("json.dump")
def test_equipment_print_to_file(m_dump, m_open, bodyequipment_all_types):
    first_key = list(bodyequipment_all_types.keys())[0]
    item = bodyequipment_all_types[first_key].copy()

    item.print_to_file()

    m_open.assert_called_once_with(item.name + ".json", "w", encoding="utf-8")
    m_dump.assert_called_with(item.export(), m_open.return_value.__enter__())


def test_equipment_export():
    item = Equipment("Export Test", "Export Test Description", 0, 0)
    assert item.export() == {
        "name": "Export Test",
        "description": "Export Test Description",
        "item_type": 0,
        "armor_type": 0,
    }


def test_equipment_get_item_type(bodyequipment_all_types, weaponequipment_all_types):
    for body in bodyequipment_all_types.values():
        assert body.get_item_type() == ITEM_TYPES[body.item_type]

    for weapon in weaponequipment_all_types.values():
        assert weapon.get_item_type() == ITEM_TYPES[weapon.item_type]


def test_equipment_get_armor_type(bodyequipment_all_types, weaponequipment_all_types):
    for body in bodyequipment_all_types.values():
        assert body.get_armor_type() == ARMOR_TYPES[body.armor_type]

    for weapon in weaponequipment_all_types.values():
        assert weapon.get_armor_type() == ARMOR_TYPES[weapon.armor_type]


def test_equipment_copy():
    item = Equipment("Copy Test", "Copy Test Description", 0, 0)
    new_item = item.copy()

    assert id(new_item) != id(item)
    assert new_item.name == item.name
    assert new_item.description == item.description
    assert new_item.armor_type == item.armor_type
    assert new_item.item_type == item.item_type


# ================================ #
# Testing Body Equipment Functions #
# ================================ #
def test_bodyequipment_init(bodyequipment_mods):
    # Test Body Equipment
    body = BodyEquipment("Init Test", None, "Testing Initialization", 0, 0)
    assert body.mods.name == "Init Test"
    assert body.mods.adds == {}
    assert body.mods.mults == {}

    # Test Modded Equipment
    mod_body = BodyEquipment(
        "Init Mod Test", bodyequipment_mods["Back_mods"], "Testing modded  init", 2, 2
    )
    assert mod_body.mods.name == "Init Mod Test"
    assert mod_body.mods.adds == bodyequipment_mods["Back_mods"]["adds"]
    assert mod_body.mods.mults == bodyequipment_mods["Back_mods"]["mults"]


def test_bodyequipment_get_mods(bodyequipment_mods, bodyequipment_all_items_mods):
    for key, body in bodyequipment_all_items_mods.items():
        assert bodyequipment_mods[key] == body.get_mods()


def test_bodyequipment_copy(bodyequipment_all_items_mods):
    first_key = list(bodyequipment_all_items_mods.keys())[0]
    body_item = bodyequipment_all_items_mods[first_key].copy()
    new_item = body_item.copy()

    assert id(new_item) != id(body_item)
    assert new_item.name == body_item.name
    assert new_item.mods != body_item.mods
    assert isinstance(new_item.mods, Modifier)
    assert new_item.mods.adds == body_item.mods.adds
    assert new_item.mods.mults == body_item.mods.mults
    assert new_item.description == body_item.description
    assert new_item.armor_type == body_item.armor_type
    assert new_item.item_type == body_item.item_type


def test_bodyequipment_export(bodyequipment_all_items_mods):
    for item in bodyequipment_all_items_mods.values():
        exporter = item.export()
        assert exporter.get("mods", False)


def test_bodyequipment_details(bodyequipment_all_items_mods, bodyequipment_details_expectation):
    """Mostly test format and indention"""
    test_item = list(bodyequipment_all_items_mods.values())[0]
    print(test_item.details())
    for index, expectations in enumerate(bodyequipment_details_expectation):
        assert test_item.details(index) == expectations


# ================================== #
# Testing Weapon Equipment Functions #
# ================================== #
def test_weaponequipment_init(weaponequipment_all_types):
    for weapon in weaponequipment_all_types.values():
        assert weapon.get_weapon_type() in WEAPON_TYPES


def test_weaponequipment_copy(weaponequipment_all_types):
    first_key = list(weaponequipment_all_types.keys())[0]
    weapon = weaponequipment_all_types[first_key].copy()
    new_item = weapon.copy()

    assert id(new_item) != id(weapon)
    assert new_item.name == weapon.name
    assert new_item.weapon_type == weapon.weapon_type
    assert new_item.description == weapon.description
    assert new_item.armor_type == weapon.armor_type
    assert new_item.item_type == weapon.item_type


def test_weaponequipment_get_item_description(
    weaponequipment_all_types, weaponequipment_description_expectations
):
    for weapon in weaponequipment_all_types.values():
        assert weapon.get_item_description() in weaponequipment_description_expectations
