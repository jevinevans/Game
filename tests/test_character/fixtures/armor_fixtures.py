import pytest

from funclg.character.armor import Armor
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.types import get_item_type, get_weapon_type


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
{' '*indent}Light Armor
{' '*indent}-----------
{' '*(indent+2)}Head: 
{' '*(indent+2)}Head
{' '*(indent+2)}----
{' '*(indent+2)}Type: [Light Head]
{' '*(indent+2)}Description: Test Head

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Head_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Chest: 
{' '*(indent+2)}Chest
{' '*(indent+2)}-----
{' '*(indent+2)}Type: [Light Chest]
{' '*(indent+2)}Description: Test Chest

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Chest_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Back: 
{' '*(indent+2)}Back
{' '*(indent+2)}----
{' '*(indent+2)}Type: [Light Back]
{' '*(indent+2)}Description: Test Back

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Back_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Pants: 
{' '*(indent+2)}Pants
{' '*(indent+2)}-----
{' '*(indent+2)}Type: [Light Pants]
{' '*(indent+2)}Description: Test Pants

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Pants_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Weapon: 
{' '*(indent+2)}Weapon: Knife
{' '*(indent+2)}-------------
{' '*(indent+2)}Type: [Light Knife]
{' '*(indent+2)}Description: Test Weapon

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Weapon: Knife_mod:
{' '*(indent+6)}Attack: +1
{' '*(indent+6)}Energy: +1


{' '*(indent+2)}Stats
{' '*(indent+2)}-----
{' '*(indent+2)}Health: 210
{' '*(indent+2)}Energy: 15.4
{' '*(indent+2)}Attack: 11
{' '*(indent+2)}Defense: 10"""
        expectations.append(base)
    return expectations


@pytest.fixture
def armor_details_missing_weapon():
    indent = 0
    return f"""
{' '*indent}Light Armor
{' '*indent}-----------
{' '*(indent+2)}Head: 
{' '*(indent+2)}Head
{' '*(indent+2)}----
{' '*(indent+2)}Type: [Light Head]
{' '*(indent+2)}Description: Test Head

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Head_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Chest: 
{' '*(indent+2)}Chest
{' '*(indent+2)}-----
{' '*(indent+2)}Type: [Light Chest]
{' '*(indent+2)}Description: Test Chest

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Chest_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Back: 
{' '*(indent+2)}Back
{' '*(indent+2)}----
{' '*(indent+2)}Type: [Light Back]
{' '*(indent+2)}Description: Test Back

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Back_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Pants: 
{' '*(indent+2)}Pants
{' '*(indent+2)}-----
{' '*(indent+2)}Type: [Light Pants]
{' '*(indent+2)}Description: Test Pants

{' '*(indent+2)}Modifier(s):
{' '*(indent+4)}Pants_mod:
{' '*(indent+6)}Health: +50
{' '*(indent+6)}Energy: +10.0%

{' '*(indent+2)}Weapon: None

{' '*(indent+2)}Stats
{' '*(indent+2)}-----
{' '*(indent+2)}Health: 210
{' '*(indent+2)}Energy: 14.0
{' '*(indent+2)}Attack: 10
{' '*(indent+2)}Defense: 10"""


@pytest.fixture
def armor_export_expectations():
    return {
        "armor_type": 0,
        "head": {
            "name": "Head",
            "description": "Test Head",
            "item_type": 0,
            "armor_type": 0,
            "mod": {
                "name": "Head_mod",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "chest": {
            "name": "Chest",
            "description": "Test Chest",
            "item_type": 1,
            "armor_type": 0,
            "mod": {
                "name": "Chest_mod",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "back": {
            "name": "Back",
            "description": "Test Back",
            "item_type": 2,
            "armor_type": 0,
            "mod": {
                "name": "Back_mod",
                "adds": {"health": 50},
                "mults": {"energy": 0.1},
            },
        },
        "pants": {
            "name": "Pants",
            "description": "Test Pants",
            "item_type": 3,
            "armor_type": 0,
            "mod": {
                "name": "Pants_mod",
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
            "mod": {
                "name": "Weapon: Sword_mod",
                "adds": {"attack": 1, "energy": 1},
                "mults": {},
            },
        },
        "stat": {
            "attack": 10,
            "defense": 10,
            "energy": 10,
            "health": 10,
            "level": None,
            "mods": {
                "Back_mod": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Chest_mod": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Head_mod": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Pants_mod": {"adds": {"health": 50}, "mults": {"energy": 0.1}},
                "Weapon: Sword_mod": {"adds": {"attack": 1, "energy": 1}, "mults": {}},
            },
        },
    }
