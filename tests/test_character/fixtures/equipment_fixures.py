"""
Equipment Fixtures for testing
"""

from unittest import expectedFailure

import pytest

from FUNCLG.character.equipment import BodyEquipment, WeaponEquipment
from FUNCLG.utils.types import ARMOR_TYPES, ITEM_TYPES, MODIFIER_TYPES, WEAPON_TYPES


@pytest.fixture
def bodyequipment_all_types():
    # For each armor type creates an item of that type
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        for a_index, armor_type in enumerate(ARMOR_TYPES):
            # NO_Mods
            equipment[item_type + "_" + armor_type] = BodyEquipment(
                name=item_type + "_" + armor_type,
                description=f"{armor_type} {item_type}",
                armor_type=a_index,
                item_type=i_index,
            )
    return equipment


@pytest.fixture
def bodyequipment_mods():
    item_mods = {}
    for index, item_type in enumerate(ITEM_TYPES[:4]):
        start = index % len(MODIFIER_TYPES)
        end = -1 * (index % len(MODIFIER_TYPES))
        item_mods[item_type + "_mods"] = {
            "adds": {MODIFIER_TYPES[start]: 50},
            "mults": {MODIFIER_TYPES[end]: 0.10},
        }
    return item_mods


@pytest.fixture
def bodyequipment_all_items_mods(bodyequipment_mods):
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        equipment[item_type + "_mods"] = BodyEquipment(
            name=item_type + "_mods",
            description=f"Medium {item_type} with mods",
            armor_type=1,
            item_type=i_index,
            modifiers=bodyequipment_mods[item_type + "_mods"],
        )
    return equipment


@pytest.fixture
def weaponequipment_all_types():
    # For each armor type, creates a weapon of that type
    weapons = {}
    for w_index, weapon_type in enumerate(WEAPON_TYPES):
        for a_index, armor_type in enumerate(ARMOR_TYPES):
            weapons[weapon_type + "_" + armor_type] = WeaponEquipment(
                name=weapon_type + "_" + armor_type,
                description=f"{armor_type} {weapon_type}",
                weapon_type=w_index,
                armor_type=a_index,
            )
    return weapons


@pytest.fixture
def equipment_str_expectation(bodyequipment_all_types, weaponequipment_all_types):
    expectations = {}

    for name, body in bodyequipment_all_types.items():
        expectations[name] = f"{body.name} [{body.armor_type} {body.item_type}]"

    for name, weapone in weaponequipment_all_types.items():
        expectations[name] = f"{weapone.name} [{weapone.armor_type} {weapone.item_type}]"

    return expectations


@pytest.fixture
def bodyequipment_details_expectation(bodyequipment_all_items_mods):
    expectations = []

    for indent in range(0, 7):
        base = f"""
{' '*indent}Head_mods
{' '*indent}---------
{' '*indent}Type: [Medium Head]
{' '*indent}Description: Medium Head with mods

{' '*indent}Modifier(s):
{' '*(indent+2)}Head_mods:
{' '*(indent+4)}Health
{' '*(indent+6)}+50
{' '*(indent+6)}+10.0%

"""
        expectations.append(base)
    return expectations


@pytest.fixture
def weaponequipment_description_expectations():
    descriptions = []
    for armor_type in ARMOR_TYPES:
        for weapon_type in WEAPON_TYPES:
            descriptions.append(f"[{armor_type} {weapon_type}]")
    return descriptions
