"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""

from unittest.mock import patch

import pytest

from funclg.character.equipment import BodyEquipment, Equipment, WeaponEquipment
from funclg.character.modifiers import Modifier
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, WEAPON_TYPES

from .fixtures.equipment_fixures import (
    body_equipment_with_mods,
    body_equipment,
    body_details_expectation,
    body_mods,
    equipment_str_expectation,
    weapon_equipment_with_mods,
    weapon_description_expectations,
    weapon_mods,
)


# =========================== #
# Testing Equipment Functions #
# =========================== #
def test_equipment_str(
    weapon_equipment_with_mods, body_equipment, equipment_str_expectation
):
    # Test Body Equipment
    for name, body in body_equipment.items():
        assert body.__str__() == equipment_str_expectation[name]

    # Test weapon Equipment
    for name, weapon in weapon_equipment_with_mods.items():
        assert weapon.__str__() == equipment_str_expectation[name]


@patch("builtins.open")
@patch("json.dump")
def test_equipment_print_to_file(m_dump, m_open, body_equipment):
    first_key = list(body_equipment.keys())[0]
    item = body_equipment[first_key].copy()

    item.print_to_file()

    m_open.assert_called_once_with(item.name + ".json", "w", encoding="utf-8")
    m_dump.assert_called_with(item.export(), m_open.return_value.__enter__())


@patch("funclg.utils.data_mgmt.id_gen")
def test_equipment_export(m_id):
    test_id = "EQUIP-12345-HJFJEF-67890"
    m_id.return_value = test_id

    item = Equipment(
        name="Export Test",
        modifier={"adds": {"health": 1}},
        description="Export Test Description",
        item_type=0,
        armor_type=0,
    )
    assert item.export() == {
        "name": "Export Test",
        "description": "Export Test Description",
        "item_type": 0,
        "armor_type": 0,
        "mod": {"adds": {"health": 1}},
        "_id": test_id,
    }


def test_equipment_get_item_type(body_equipment, weapon_equipment_with_mods):
    for body in body_equipment.values():
        assert body.get_item_type() == ITEM_TYPES[body.item_type]

    for weapon in weapon_equipment_with_mods.values():
        assert weapon.get_item_type() == ITEM_TYPES[weapon.item_type]


def test_equipment_get_armor_type(body_equipment, weapon_equipment_with_mods):
    for body in body_equipment.values():
        assert body.get_armor_type() == ARMOR_TYPES[body.armor_type]

    for weapon in weapon_equipment_with_mods.values():
        assert weapon.get_armor_type() == ARMOR_TYPES[weapon.armor_type]


def test_equipment_copy():
    item = Equipment("Copy Test", "Copy Test Description", 0, 0)
    new_item = item.copy()

    assert id(new_item) != id(item)
    # assert new_item.id != item.id TODO
    assert new_item.name == item.name
    assert new_item.description == item.description
    assert new_item.armor_type == item.armor_type
    assert new_item.item_type == item.item_type


# ================================ #
# Testing Body Equipment Functions #
# ================================ #
def test_bodyequipment_init(body_mods):
    # Test Body Equipment
    body = BodyEquipment("Init Test", None, "Testing Initialization", 0, 0)
    assert body.mod.name == "Init Test_mod"
    assert body.mod.adds == {"defense": 1, "health": 1}
    assert body.mod.mults == {}

    # Test Modded Equipment
    mod_body = BodyEquipment(
        "Init Mod Test", body_mods["Back_mods"], "Testing modded  init", 2, 2
    )
    assert mod_body.mod.name == "Init Mod Test_mod"
    assert mod_body.mod.adds == body_mods["Back_mods"]["adds"]
    assert mod_body.mod.mults == body_mods["Back_mods"]["mults"]


def test_bodyequipment_get_mods(body_mods, body_equipment_with_mods):
    for key, body in body_equipment_with_mods.items():
        assert body_mods[key] == body.get_mods()


def test_bodyequipment_copy(body_equipment_with_mods):
    first_key = list(body_equipment_with_mods.keys())[0]
    body_item = body_equipment_with_mods[first_key].copy()
    new_item = body_item.copy()

    assert id(new_item) != id(body_item)
    assert new_item.name == body_item.name
    assert new_item.mod != body_item.mod
    assert isinstance(new_item.mod, Modifier)
    assert new_item.mod.adds == body_item.mod.adds
    assert new_item.mod.mults == body_item.mod.mults
    assert new_item.description == body_item.description
    assert new_item.armor_type == body_item.armor_type
    assert new_item.item_type == body_item.item_type


def test_bodyequipment_export(body_equipment_with_mods):
    for item in body_equipment_with_mods.values():
        exporter = item.export()
        assert exporter.get("mod", False)


def test_bodyequipment_details(body_equipment_with_mods, body_details_expectation):
    """Mostly test format and indention"""
    test_item = list(body_equipment_with_mods.values())[0]
    print(test_item.details())
    for index, expectations in enumerate(body_details_expectation):
        assert test_item.details(index) == expectations


# ================================== #
# Testing Weapon Equipment Functions #
# ================================== #
def test_weaponequipment_init(weapon_equipment_with_mods, weapon_mods):
    for weapon in weapon_equipment_with_mods.values():
        assert weapon.get_weapon_type() in WEAPON_TYPES

    mod_weapon = WeaponEquipment(
        name="Init Mod Test",
        modifiers=weapon_mods["Sword_mods"],
        description="Testing Mod Weapon Init",
        weapon_type=0,
        armor_type=0,
    )
    assert mod_weapon.mod.name == "Init Mod Test_mod"
    assert mod_weapon.mod.adds == weapon_mods["Sword_mods"]["adds"]
    assert mod_weapon.mod.mults == weapon_mods["Sword_mods"]["mults"]


def test_weaponequipment_get_mods(weapon_mods, weapon_equipment_with_mods):
    for key, weapon in weapon_equipment_with_mods.items():
        assert weapon_mods[key] == weapon.get_mods()


def test_weaponequipment_copy(weapon_equipment_with_mods):
    first_key = list(weapon_equipment_with_mods.keys())[0]
    weapon = weapon_equipment_with_mods[first_key].copy()
    new_item = weapon.copy()

    assert isinstance(new_item, WeaponEquipment)
    assert id(new_item) != id(weapon)
    assert new_item.name == weapon.name
    assert new_item.weapon_type == weapon.weapon_type
    assert new_item.description == weapon.description
    assert new_item.armor_type == weapon.armor_type
    assert new_item.item_type == weapon.item_type


def test_weaponequipment_get_item_description(
    weapon_equipment_with_mods, weapon_description_expectations
):
    for weapon in weapon_equipment_with_mods.values():
        assert weapon.get_item_description() in weapon_description_expectations
