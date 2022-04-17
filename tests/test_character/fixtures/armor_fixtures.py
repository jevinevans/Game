import pytest

from FUNCLG.character.armor import Armor
from FUNCLG.character.equipment import BodyEquipment, WeaponEquipment
from FUNCLG.utils.types import get_item_type, get_weapon_type


def gen_equipment(armor_type: int, weapon_type: int):
    equipment = {}
    mods = {"adds": {"health": 50}, "mults": {"energy": 0.1}}
    for item_type in range(4):
        equipment[get_item_type(item_type)] = BodyEquipment(
            name=get_item_type(item_type),
            modifiers=mods,
            description=f"Test {get_item_type(item_type)}",
            armor_type=armor_type,
            item_type=item_type,
        )
    equipment["Weapon"] = WeaponEquipment(
        name=f"Weapon: {get_weapon_type(weapon_type)}",
        weapon_type=weapon_type,
        description="Test Weapon",
        armor_type=armor_type,
    )
    return equipment


@pytest.fixture
def equipment_only():
    return gen_equipment(0, 0)


@pytest.fixture
def light_armor_knife():
    equipment = gen_equipment(0, 2)
    return Armor(
        0,
        equipment["Head"],
        equipment["Chest"],
        equipment["Back"],
        equipment["Pants"],
        equipment["Weapon"],
    )


@pytest.fixture
def medium_armor_wand():
    equipment = gen_equipment(1, 1)
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
    equipment = gen_equipment(2, 0)
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
    equipment = gen_equipment(1, 0)
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
def armor_details_expectations():
    expectations = []
    for indent in range(0, 7):
        base = f"""
{' '*indent} Armor (Light) 
{' '*indent}-----------------
{' '*(indent+2)}Head: Head [0 0]
{' '*(indent+2)}Chest: Chest [0 1]
{' '*(indent+2)}Back: Back [0 2]
{' '*(indent+2)}Pants: Pants [0 3]
{' '*(indent+2)}Weapon: Weapon: Knife [0 4]"""
        expectations.append(base)
    return expectations


@pytest.fixture
def armor_export_expectations():
    return {
        "armor_type": 0,
        "head": {
            "name": "Head",
            "description": "Test Head",
            "item_type": 0,
            "armor_type": 0,
            "mods": {
                "name": "Head",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "chest": {
            "name": "Chest",
            "description": "Test Chest",
            "item_type": 1,
            "armor_type": 0,
            "mods": {
                "name": "Chest",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "back": {
            "name": "Back",
            "description": "Test Back",
            "item_type": 2,
            "armor_type": 0,
            "mods": {
                "name": "Back",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "pants": {
            "name": "Pants",
            "description": "Test Pants",
            "item_type": 3,
            "armor_type": 0,
            "mods": {
                "name": "Pants",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "weapon": {
            "name": "Weapon: Sword",
            "description": "Test Weapon",
            "item_type": 4,
            "weapon_type": 0,
            "armor_type": 0,
        },
    }
