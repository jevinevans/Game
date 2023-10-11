"""
Description: Pytest fixtures for the character.armor module
Developer: Jevin Evans
Date: 11/5/2022
"""

import pytest

from funclg.character.armor import Armor
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import get_item_type


def gen_equipment(armor_type: int, weapon_type: str):
    equipment = {}
    mods = {"adds": {"health": 50}, "mults": {"energy": 0.1}}
    for item_type in range(4):
        equipment[get_item_type(item_type)] = BodyEquipment(
            name=get_item_type(item_type),
            mod=mods,
            description=f"Test {get_item_type(item_type)}",
            armor_type=armor_type,
            item_type=item_type,
        )
    equipment["Weapon"] = WeaponEquipment(
        name=f"Weapon: {weapon_type}",
        weapon_type=weapon_type,
        description="Test Weapon",
    )

    return equipment


@pytest.fixture
def equipment_only():
    return gen_equipment(0, "Bow")


@pytest.fixture
def light_armor_knife():
    equipment = gen_equipment(0, "Knife")
    return Armor(
        0,
        head=equipment["Head"],
        chest=equipment["Chest"],
        back=equipment["Back"],
        pants=equipment["Pants"],
        weapon=equipment["Weapon"],
    )


@pytest.fixture
def medium_armor_wand():
    equipment = gen_equipment(1, "Wand")
    return Armor(
        1,
        equipment["Head"],
        equipment["Chest"],
        equipment["Back"],
        equipment["Pants"],
        equipment["Weapon"],
    )


@pytest.fixture
def heavy_armor_sword():
    equipment = gen_equipment(2, "Sword")
    return Armor(
        2,
        equipment["Head"],
        equipment["Chest"],
        equipment["Back"],
        equipment["Pants"],
        equipment["Weapon"],
    )


@pytest.fixture
def medium_half_armor():
    equipment = gen_equipment(1, "Sword")
    return Armor(armor_type=1, chest=equipment["Chest"], pants=equipment["Pants"])


@pytest.fixture
def armor_str_expectations():
    """Str Test for:
    - Medium Half Armor
    - Heavy Armor Sword
    - Empty Armor"""
    return [
        "Medium Armor: <H:0, C:1, B:0, P:1, W:0>",
        "Heavy Armor: <H:1, C:1, B:1, P:1, W:1>",
        "Light Armor: <H:0, C:0, B:0, P:0, W:0>",
    ]


@pytest.fixture
def armor_details_expectations(light_armor_knife):
    expectations = []
    for indent in range(0, 7):
        base = f"""
{' '*indent}Light Armor
{' '*indent}-----------
{' '*(indent+2)}Head: {light_armor_knife.head.details(indent+4)}\n
{' '*(indent+2)}Chest: {light_armor_knife.chest.details(indent+4)}\n
{' '*(indent+2)}Back: {light_armor_knife.back.details(indent+4)}\n
{' '*(indent+2)}Pants: {light_armor_knife.pants.details(indent+4)}\n
{' '*(indent+2)}Weapon: {light_armor_knife.weapon.details(indent+4)}
{light_armor_knife.stat.details(indent+2)}"""
        expectations.append(base)
    return expectations


@pytest.fixture
def armor_details_missing_weapon(light_armor_knife):
    new_armor = Armor(
        armor_type=light_armor_knife.armor_type,
        head=light_armor_knife.head,
        chest=light_armor_knife.chest,
        back=light_armor_knife.back,
        pants=light_armor_knife.pants,
    )
    indent = 0
    return f"""
{' '*indent}Light Armor
{' '*indent}-----------
{' '*(indent+2)}Head: {new_armor.head.details(indent+4)}\n
{' '*(indent+2)}Chest: {new_armor.chest.details(indent+4)}\n
{' '*(indent+2)}Back: {new_armor.back.details(indent+4)}\n
{' '*(indent+2)}Pants: {new_armor.pants.details(indent+4)}\n
{' '*(indent+2)}Weapon: None
{new_armor.stat.details(indent+2)}"""


@pytest.fixture
def armor_export_expectations():
    return {
        "armor_type": 0,
        "head": {
            "name": "Head",
            "description": "Test Head",
            "item_type": 0,
            "armor_type": 0,
            "level": 0,
            "mod": {
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
            "_id": "ARMOR-12345-AFJDEI-67890",
        },
        "chest": {
            "name": "Chest",
            "description": "Test Chest",
            "item_type": 1,
            "armor_type": 0,
            "level": 0,
            "mod": {
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
            "_id": "ARMOR-12345-FEISFJ-67891",
        },
        "back": {
            "name": "Back",
            "description": "Test Back",
            "item_type": 2,
            "armor_type": 0,
            "level": 0,
            "mod": {
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
            "_id": "ARMOR-12345-GIEJSE-67892",
        },
        "pants": {
            "name": "Pants",
            "description": "Test Pants",
            "item_type": 3,
            "armor_type": 0,
            "level": 0,
            "mod": {
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
            "_id": "ARMOR-12345-GEIJGE-67893",
        },
        "weapon": {
            "name": "Weapon: Bow",
            "description": "Test Weapon",
            "item_type": 4,
            "weapon_type": "Bow",
            "armor_type": 0,
            "level": 0,
            "mod": {
                "adds": {"attack": 1, "energy": 1},
                "mults": {},
            },
            "_id": "WEAPON-12345-FEGIF-67894",
        },
        "stat": {
            "attack": 10,
            "defense": 10,
            "energy": 10,
            "health": 10,
            "level": None,
            "mods": {
                "Back": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Chest": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Head": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Pants": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Weapon: Bow": {"adds": {"attack": 1, "energy": 1}, "mults": {}},
            },
        },
    }
