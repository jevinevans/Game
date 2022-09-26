"""Unittest for Character Class"""

from unittest.mock import patch

import pytest

from funclg.character import abilities, armor, roles
from funclg.character.character import Character
from funclg.character.equipment import BodyEquipment, Equipment


@pytest.fixture
def basic_char():
    with patch(
        "funclg.utils.data_mgmt.id_gen",
        side_effect=["ROLES-12345-FEJSIG-67890", "CHARS-12345-GEJFSI-67890"],
    ):
        t_armor = armor.Armor(0)
        t_role = roles.Roles("Test_Role", "Test role", 0)
        return Character("Test_Char", 0, t_armor, t_role)


@pytest.fixture
def character_str_expectation():
    return """  Test_Char  \n-------------\n Class: Test_Role\n Armor: Light Armor: <H:0, C:0, B:0, P:0, W:0>"""


@pytest.fixture
def character_export_expectation():
    return {
        "_id": "CHARS-12345-GEJFSI-67890",
        "name": "Test_Char",
        "armor_type": 0,
        "inventory": [],
        "armor": {
            "armor_type": 0,
            "back": None,
            "chest": None,
            "head": None,
            "pants": None,
            "stat": {
                "attack": 10,
                "defense": 10,
                "energy": 10,
                "health": 10,
                "level": None,
                "mods": {},
            },
            "weapon": None,
        },
        "role": {
            "_id": "ROLES-12345-FEJSIG-67890",
            "abilities": [],
            "armor_type": 0,
            "ability_types": "None",
            "description": "Test role",
            "name": "Test_Role",
        },
    }


@pytest.fixture
def character_details_expectation():
    return """Test_Char
---------

  Class: Test_Role
  ----------------
  Armor Type: Light
  Description: Test role
  Role Abilities:
    No Abilities

  Light Armor
  -----------
    Head: None
    Chest: None
    Back: None
    Pants: None
    Weapon: None

    Stats
    -----
    Health: 10
    Energy: 10
    Attack: 10
    Defense: 10"""


@pytest.fixture
def character_inventory_show_expectation():
    inventory = ["item_1", "item_2", "item_3"]
    expectation = "\nInventory:"
    for item in inventory:
        expectation += f"  - {item}"
    return [expectation, inventory]


def test_character_init_no_armor_no_role():
    # Init No Role/Armor
    t_char = Character("Test_Char", 0)
    assert t_char.name == "Test_Char"
    assert t_char.armor != None
    assert t_char.armor.armor_type == t_char.armor_type
    assert t_char.role != None
    assert t_char.role.name == "Basic"
    assert t_char.inventory == []

    # Test with inventory
    test_inventory = [1, 2, 3]
    t_char = Character("Test_Char", 0, inventory=test_inventory)
    assert t_char.inventory == test_inventory


def test_character_str(basic_char, character_str_expectation):
    assert basic_char.__str__() == character_str_expectation


def test_character_export(basic_char, character_export_expectation):
    assert basic_char.export() == character_export_expectation


def test_character_details(basic_char, character_details_expectation):
    assert basic_char.details() == character_details_expectation


def test_character_equip(basic_char):
    t_head = BodyEquipment("Test_Head", basic_char.armor_type, 0)
    basic_char.equip(t_head)
    assert basic_char.armor.head.name == t_head.name


def test_character_dequip(basic_char):
    # Valid Dequip
    t_head = BodyEquipment("Test_Head", basic_char.armor_type, 0)
    basic_char.equip(t_head)
    assert basic_char.armor.head.name == t_head.name

    basic_char.dequip("head")
    assert basic_char.armor.head == None
    assert len(basic_char.inventory) == 1

    # Invalid Dequip
    basic_char.dequip("")
    assert len(basic_char.inventory) == 1


@patch("builtins.print")
def test_character_show_inventory(m_print, basic_char, character_inventory_show_expectation):
    expectation, test_inventory = character_inventory_show_expectation
    basic_char.inventory = test_inventory

    basic_char.show_inventory()
    assert m_print.called_with(expectation)


def test_character_add_power(basic_char):
    t_ability = abilities.Abilities("Test_Ability", "None", "Test ability", {})
    basic_char.add_power(t_ability)
    assert len(basic_char.role.abilities) == 1
    assert basic_char.role.abilities[0].name == t_ability.name
