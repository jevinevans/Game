"""
Equipment Fixtures for testing
"""

import pytest

from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES, MODIFIER_TYPES, WEAPON_TYPES


@pytest.fixture
def body_equipment():
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
def body_mods():
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
def body_equipment_with_mods(body_mods):
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        equipment[item_type + "_mods"] = BodyEquipment(
            name=item_type + "_mods",
            description=f"Medium {item_type} with mods",
            armor_type=1,
            item_type=i_index,
            modifiers=body_mods[item_type + "_mods"],
        )
    return equipment


@pytest.fixture
def weapon_mods():
    item_mods = {}
    for index, weapon_type in enumerate(WEAPON_TYPES[:4]):
        start = index % len(MODIFIER_TYPES)
        end = -1 * (index % len(MODIFIER_TYPES))
        item_mods[weapon_type + "_mods"] = {
            "adds": {MODIFIER_TYPES[start]: 50},
            "mults": {MODIFIER_TYPES[end]: 0.10},
        }
    return item_mods


@pytest.fixture
def weapon_equipment_with_mods(weapon_mods):
    equipment = {}
    for i_index, weapon_type in enumerate(WEAPON_TYPES[:4]):
        equipment[weapon_type + "_mods"] = WeaponEquipment(
            name=weapon_type + "_mods",
            description=f"{weapon_type} with mods",
            weapon_type=i_index,
            modifiers=weapon_mods[weapon_type + "_mods"],
        )
    return equipment

@pytest.fixture
def equipment_str_expectation(body_equipment, weapon_equipment_with_mods):
    expectations = {}

    for name, body in body_equipment.items():
        expectations[name] = f"{body.name} [{body.armor_type} {body.item_type}]"

    for name, weapon in weapon_equipment_with_mods.items():
        expectations[name] = f"{weapon.name} [{weapon.weapon_type} {weapon.item_type}]"

    return expectations


@pytest.fixture
def body_details_expectation():
    expectations = []

    for indent in range(0, 7):
        base = f"""
{' '*indent}Head_mods
{' '*indent}---------
{' '*indent}Type: [Medium Head]
{' '*indent}Description: Medium Head with mods

{' '*indent}Modifier(s):
{' '*(indent+2)}Head_mods_mod:
{' '*(indent+4)}Health: +50, +10.0%
"""
        expectations.append(base)
    return expectations


@pytest.fixture
def weapon_description_expectations():
    descriptions = []
    for weapon_type in WEAPON_TYPES:
        descriptions.append(f"[{weapon_type}]")
    return descriptions
