import pytest

from funclg.managers.abilities_manager import AbilitiesManager
from funclg.managers.equipment_manager import EquipmentManager
from funclg.managers.roles_manager import RolesManager
from funclg.managers.character_manager import CharacterManager

@pytest.fixture
def test_magic():
    return {
        "name": "Test_Magic",
        "description": "Test Magic",
        "ability_type": "Magic",
        "_target": "enemy",
        "mod": {"base": {"health": 200}, "percentage": {}},
        "_id": "ABILITY-12345-EJFI-67890",
    }

@pytest.fixture
def test_equipment():
    return {
        "name": "Test Plate",
        "description": "Test Chest Plate",
        "item_type": 1,
        "armor_type": 0,
        "stats": {
            "attributes": {"defense": 10, "health": 1, "energy": 1, "attack": 1, "_power": 13}
        },
        "_id": "ARMOR-16342-QLERCA-36276",
    }


@pytest.fixture
def test_equipment_2():
    return {
        "name": "Test Head",
        "description": "Test Chest Head",
        "item_type": 0,
        "armor_type": 2,
        "stats": {
            "attributes": {"defense": 10, "health": 40, "energy": 1, "attack": 1, "_power": 53}
        },
        "_id": "ARMOR-16342-QLPBCA-36276",
    }


@pytest.fixture
def test_weapon():
    return {
        "name": "Test Spear",
        "description": "Test Spear",
        "item_type": 4,
        "armor_type": 2,
        "stats": {
            "attributes": {"defense": 10, "health": 1, "energy": 1, "attack": 27, "_power": 39}
        },
        "_id": "WEAPON-16151-OEGEFS-36126",
        "weapon_type": "Spear",
    }


@pytest.fixture()
def test_ability_manager():

    return AbilitiesManager()

@pytest.fixture()
def test_equipment_manager():
    return EquipmentManager()

@pytest.fixture()
def test_roles_manager():
    return RolesManager()

@pytest.fixture()
def test_character_manager():
    return CharacterManager()