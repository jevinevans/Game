"""Unittest for Character Class"""

from unittest.mock import patch

import pytest

from funclg.character import abilities, armor, roles
from funclg.character.character import Character, Player
from funclg.character.equipment import BodyEquipment


@pytest.fixture
def basic_char():
    with patch(
        "funclg.utils.data_mgmt.id_gen",
        side_effect=["ROLES-12345-FEJSIG-67890", "CHARS-12345-GEJFSI-67890"],
    ):
        t_armor = armor.Armor(0)
        t_role = roles.Roles("Test_Role", "Test role", 0)
        return Character("Test_Char", t_armor, t_role)


@pytest.fixture
def character_str_expectation():
    return """Test_Char [lvl 1]\n-----------------\n Class: Test_Role\n Armor: Light Armor: <H:0, C:0, B:0, P:0, W:0>"""


@pytest.fixture
def character_export_expectation():
    return {
        "_id": "CHARS-12345-GEJFSI-67890",
        "name": "Test_Char",
        "armor_type": 0,
        "level": 1,
        "armor": {
            "armor_type": 0,
            "back": None,
            "chest": None,
            "head": None,
            "pants": None,
            "weapon": None,
        },
        "role": {
            "_id": "ROLES-12345-FEJSIG-67890",
            "abilities": [],
            "armor_type": 0,
            "ability_types": ["Basic"],
            "description": "Test role",
            "name": "Test_Role",
            "level": 1,
            "stats": {
                "attributes": {"attack": 5, "defense": 5, "energy": 5, "health": 5},
                "modifiers": {},
            },
        },
        "stats": {
            "attributes": {"attack": 5, "defense": 5, "energy": 5, "health": 5},
            "modifiers": {},
        },
    }


@pytest.fixture
def character_details_expectation():
    return """Test_Char [lvl 1]
-----------------

Stats [80]
----------
  Health [5]: 20
  Attack [5]: 20
  Defense [5]: 20
  Energy [5]: 20

  Class: Test_Role [lvl 1]
  ------------------------
  Armor Type: Light
  Description: Test role

  Stats [20]
  ----------
    Health [5]: 5
    Attack [5]: 5
    Defense [5]: 5
    Energy [5]: 5

  Role Abilities:
    No Abilities

  Stats [20]
  ----------
    Health [5]: 5
    Attack [5]: 5
    Defense [5]: 5
    Energy [5]: 5

  Light Armor
  -----------
    Stats [40]
    ----------
      Health [10]: 10
      Attack [10]: 10
      Defense [10]: 10
      Energy [10]: 10

    Head: None

    Chest: None

    Back: None

    Pants: None

    Weapon: None

"""


@pytest.fixture
def character_inventory_show_expectation():
    inventory = ["item_1", "item_2", "item_3"]
    expectation = "\nInventory:" + "  - ".join(inventory)
    return [expectation, inventory]


def test_character_init_no_armor_no_role():
    # Init No Role/Armor
    t_char = Character("Test_Char")
    assert t_char.name == "Test_Char"
    assert t_char.armor is not None
    assert t_char.armor.armor_type == t_char.armor_type
    assert t_char.role is not None
    assert t_char.role.name == "NPC"
    assert t_char.id
    assert t_char.power == 80


def test_character_str(basic_char, character_str_expectation):
    assert basic_char.__str__() == character_str_expectation


def test_character_export(basic_char, character_export_expectation):
    assert basic_char.export() == character_export_expectation


def test_character_details(basic_char, character_details_expectation):
    print(basic_char.stats.get_stats())
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

    assert basic_char.dequip("head").name == t_head.name
    assert basic_char.armor.head is None

    # Invalid Dequip
    assert basic_char.dequip("") is None


def test_player_init_no_armor_no_role():
    # Init No Role/Armor
    t_char = Player("Test_Char")
    assert t_char.name == "Test_Char"
    assert t_char.armor is not None
    assert t_char.armor.armor_type == t_char.armor_type
    assert t_char.role is not None
    assert t_char.role.name == "NPC"
    assert t_char.id
    assert t_char.power == 80
    assert t_char.inventory == []


@patch("builtins.print")
def test_player_show_inventory(m_print, character_inventory_show_expectation):
    expectation, test_inventory = character_inventory_show_expectation
    t_player = Player("Test Player")
    t_player.inventory = test_inventory

    t_player.show_inventory()
    assert m_print.called_with(expectation)
