"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""

from unittest.mock import patch

import pytest

from funclg.character.equipment import BodyEquipment, Equipment, WeaponEquipment
from funclg.character.stats import Stats
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, WEAPON_TYPES

from .fixtures.equipment_fixures import (
    body_details_expectation,
    body_equipment,
    equipment_str_expectation,
    weapon_equipment,
)


# =========================== #
# Testing Equipment Functions #
# =========================== #
def test_equipment_str(weapon_equipment, body_equipment, equipment_str_expectation):
    # Test Body Equipment
    for name, body in body_equipment.items():
        assert body.__str__() == equipment_str_expectation[name]

    # Test weapon Equipment
    for name, weapon in weapon_equipment.items():
        assert weapon.__str__() == equipment_str_expectation[name]

    # Test Equipement
    test_equipment = Equipment("Test Equip", Stats(), "Test equip description", 0, 0)
    assert test_equipment.__str__() == "Test Equip [lvl 1] [Head]"


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
        stats=Stats({"health": 2}),
        description="Export Test Description",
        item_type=0,
        armor_type=0,
    )
    assert item.export() == {
        "name": "Export Test",
        "description": "Export Test Description",
        "item_type": 0,
        "armor_type": 0,
        "stats": {
            "attributes": {"attack": 1, "defense": 1, "energy": 1, "health": 2},
            "modifiers": {},
        },
        "_id": test_id,
        "level": 1,
    }


def test_equipment_get_item_type(body_equipment, weapon_equipment):
    for body in body_equipment.values():
        assert body.get_item_type() == ITEM_TYPES[body.item_type]

    for weapon in weapon_equipment.values():
        assert weapon.get_item_type() == ITEM_TYPES[weapon.item_type]


def test_equipment_get_armor_type(body_equipment, weapon_equipment):
    for body in body_equipment.values():
        assert body.get_armor_type() == ARMOR_TYPES[body.armor_type]

    for weapon in weapon_equipment.values():
        assert weapon.get_armor_type() == ARMOR_TYPES[weapon.armor_type]


def test_equipment_copy():
    item = Equipment(
        name="Copy Test",
        description="Copy Test Description",
        item_type=0,
        armor_type=0,
        stats=Stats(),
    )
    new_item = item.copy()

    assert id(new_item) != id(item)
    assert new_item.name == item.name
    assert new_item.description == item.description
    assert new_item.armor_type == item.armor_type
    assert new_item.item_type == item.item_type


# ================================ #
# Testing Body Equipment Functions #
# ================================ #
def test_bodyequipment_init():
    # Test Body Equipment no Stats
    body = BodyEquipment(
        name="Init Test", description="Testing Initialization", item_type=0, armor_type=0
    )
    assert body.stats.get_stats() == {"health": 5, "attack": 1, "defense": 5, "energy": 1}

    # Test Equipment w/ Stats
    body_stat = BodyEquipment(
        name="Init Mod Test",
        description="Testing modded  init",
        armor_type=2,
        item_type=2,
        stats={"attributes": {"defense": 7, "health": 2}},
    )
    assert body_stat.stats.get_stats() == {"health": 2, "attack": 1, "defense": 7, "energy": 1}


def test_bodyequipment_copy(body_equipment):
    first_key = list(body_equipment.keys())[0]
    body_item = body_equipment[first_key].copy()
    new_item = body_item.copy()

    assert id(new_item) != id(body_item)
    assert new_item.name == body_item.name
    assert new_item.stats == body_item.stats
    assert isinstance(new_item.stats, Stats)
    assert new_item.stats.get_stats() == body_item.stats.get_stats()
    assert new_item.description == body_item.description
    assert new_item.armor_type == body_item.armor_type
    assert new_item.item_type == body_item.item_type


@patch("funclg.utils.data_mgmt.id_gen")
def test_bodyequipment_export(m_id):
    test_id = "ARMOR-12345-HJFJEF-67890"
    m_id.return_value = test_id

    body_item = BodyEquipment(
        name="export test",
        item_type=0,
        armor_type=0,
        description="Light Head",
        stats={"attributes": {"energy": 4, "defense": 3}},
    )
    export_test = {
        "name": "export test",
        "description": "Light Head",
        "item_type": 0,
        "armor_type": 0,
        "stats": {
            "attributes": {"attack": 1, "defense": 3, "energy": 4, "health": 1},
            "modifiers": {},
        },
        "_id": test_id,
        "level": 1,
    }
    assert body_item.export() == export_test


def test_bodyequipment_details(body_equipment, body_details_expectation):
    """Mostly test format and indention"""
    test_item = list(body_equipment.values())[0]
    for index, expectations in enumerate(body_details_expectation):
        assert test_item.details(index) == expectations


# ================================== #
# Testing Weapon Equipment Functions #
# ================================== #
def test_weaponequipment_init(weapon_equipment):
    for weapon in weapon_equipment.values():
        assert weapon.weapon_type in WEAPON_TYPES

    # Base Stat test
    mod_weapon = WeaponEquipment(
        name="Init Mod Test",
        description="Testing Mod Weapon Init",
        weapon_type="Sword",
        armor_type=0,
    )
    assert mod_weapon.stats.get_stats() == {"attack": 5, "defense": 1, "energy": 5, "health": 1}


def test_weaponequipment_copy(weapon_equipment):
    first_key = list(weapon_equipment.keys())[0]
    weapon = weapon_equipment[first_key].copy()
    new_item = weapon.copy()

    assert isinstance(new_item, WeaponEquipment)
    assert id(new_item) != id(weapon)
    assert new_item.name == weapon.name
    assert new_item.weapon_type == weapon.weapon_type
    assert new_item.description == weapon.description
    assert new_item.armor_type == weapon.armor_type
    assert new_item.item_type == weapon.item_type


# ======================================= #
# Testing Body/Weapon Equipment Functions #
# ======================================= #


def test_level_up(weapon_equipment, body_equipment):
    first_key = list(weapon_equipment.keys())[0]
    weapon = weapon_equipment[first_key].copy()
    weapon_lvl = weapon.copy()

    weapon_lvl.level_up()

    print(weapon.stats)
    print(weapon_lvl.stats)

    assert abs(weapon.level - weapon_lvl.level) == 1
    assert abs(weapon.stats.health - weapon_lvl.stats.health) == 1
    assert abs(weapon.stats.energy - weapon_lvl.stats.energy) == 1
    assert abs(weapon.stats.defense - weapon_lvl.stats.defense) == 1
    assert abs(weapon.stats.attack - weapon_lvl.stats.attack) == 1
    assert abs(weapon.stats.power - weapon_lvl.stats.power) == 4

    first_key = list(body_equipment.keys())[0]
    body = body_equipment[first_key].copy()
    body_lvl = body.copy()

    for _ in range(9):
        body_lvl.level_up()

    assert abs(body.level - body_lvl.level) == 9
    assert abs(body.stats.health - body_lvl.stats.health) == 9
    assert abs(body.stats.energy - body_lvl.stats.energy) == 9
    assert abs(body.stats.defense - body_lvl.stats.defense) == 9
    assert abs(body.stats.attack - body_lvl.stats.attack) == 9
    assert abs(body.stats.power - body_lvl.stats.power) == 36


def test_equipment_get_stats(weapon_equipment):
    first_key = list(weapon_equipment.keys())[0]
    weapon_stats = weapon_equipment[first_key].get_stats()

    for attr in Stats.BASE_ATTRIBUTES:
        assert attr in weapon_stats
