"""
Description: Pytest fixtures for the character.equipment module
Developer: Jevin Evans
Date: 11/5/2022
"""

import pytest

from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, WEAPON_TYPES


@pytest.fixture
def body_equipment():
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        for a_index, armor_type in enumerate(ARMOR_TYPES):
            equipment[item_type + "_" + armor_type] = BodyEquipment(
                name=item_type + "_" + armor_type,
                description=f"{armor_type} {item_type}",
                armor_type=a_index,
                item_type=i_index,
                stats={"attributes": {"health": 10, "attack": 10, "defense": 10, "energy": 10}},
            )
    return equipment


@pytest.fixture
def weapon_equipment():
    equipment = {}
    for weapon_type in WEAPON_TYPES:
        equipment[weapon_type + "_mods"] = WeaponEquipment(
            name=weapon_type + "_mods",
            description=f"{weapon_type} with mods",
            weapon_type=weapon_type,
            stats={"attributes": {"health": 10, "attack": 10, "defense": 10, "energy": 10}},
        )
    return equipment


@pytest.fixture
def equipment_str_expectation(body_equipment, weapon_equipment):
    expectations = {}

    for name, body in body_equipment.items():
        expectations[
            name
        ] = f"{body.name} [{ARMOR_TYPES[body.armor_type]} {ITEM_TYPES[body.item_type]}]"

    for name, weapon in weapon_equipment.items():
        expectations[name] = f"{weapon.name} [{weapon.weapon_type} {ITEM_TYPES[weapon.item_type]}]"

    return expectations


@pytest.fixture
def body_details_expectation():
    expectations = []

    for indent in range(0, 7):
        base = f"""
{' '*indent}Head_Light [lvl 0]
{' '*indent}--------------------
{' '*indent}Type: [Light Head]
{' '*indent}Description: Light Head

{' '*(indent)}Stats [40]
{' '*(indent)}----------
{' '*(indent+2)}Health [10]: 10
{' '*(indent+2)}Attack [10]: 10
{' '*(indent+2)}Defense [10]: 10
{' '*(indent+2)}Energy [10]: 10"""
        expectations.append(base)
    return expectations
