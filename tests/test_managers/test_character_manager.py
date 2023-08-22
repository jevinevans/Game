"""
Description: This is to unit test the FUNCLG character manager module
Developer: Jevin Evans
Date: 02.20.2023
"""

from unittest.mock import patch

import pytest

import funclg.managers.character_manager as char_man
from funclg.character.abilities import Abilities
from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.character.roles import Roles
from funclg.utils.types import ITEM_TYPES


@pytest.fixture
def test_character_mage():
    return {
        "name": "Test Char Mage",
        "armor_type": 1,
        "inventory": [],
        "armor": {
            "armor_type": 1,
            "stat": {
                "level": None,
                "health": 20,
                "energy": 20,
                "attack": 20,
                "defense": 20,
                "mods": {
                    "Basic Mage Tunic": {"adds": {"health": 100}, "mults": {"health": 0.45}},
                    "Calins Wand": {"adds": {"attack": 337}, "mults": {"energy": 1}},
                },
            },
            "head": None,
            "chest": {
                "name": "Basic Mage Tunic",
                "description": "Armor used by beginner mages",
                "item_type": 1,
                "armor_type": 1,
                "mod": {"adds": {"health": 100}, "mults": {"health": 0.45}},
                "_id": "ARMOR-16809-BCWSVN-76675",
            },
            "back": None,
            "pants": None,
            "weapon": {
                "weapon_type": "Wand",
                "name": "Calins Wand",
                "description": "The original wand of Calin",
                "item_type": 4,
                "armor_type": 1,
                "mod": {"adds": {"attack": 337}, "mults": {"energy": 1}},
                "_id": "WEAPON-16645-ACIGL-01214",
            },
        },
        "role": {
            "name": "Mage",
            "description": "Magic user",
            "armor_type": 1,
            "ability_types": ["Magic", "Buff", "Debuff", "Restore"],
            "abilities": [
                {
                    "name": "Fireball",
                    "description": "Throws a fireball at target",
                    "ability_type": "Magic",
                    "_target": "enemy",
                    "mod": {"adds": {"defense": -446}, "mults": {}},
                    "_id": "ABILITY-16650-OKNG-98180",
                },
                {
                    "name": "Empower",
                    "description": "Strengthens player",
                    "ability_type": "Buff",
                    "_target": "self",
                    "mod": {"adds": {}, "mults": {"defense": 0.98}},
                    "_id": "ABILITY-16650-DXUF-98274",
                },
                {
                    "name": "Weaken",
                    "description": "Weakens an enemy",
                    "ability_type": "Debuff",
                    "_target": "enemy",
                    "mod": {"adds": {}, "mults": {"defense": -0.83}},
                    "_id": "ABILITY-16660-TXKX-31305",
                },
            ],
            "_id": "ROLES-16695-ZBLWXR-20642",
        },
        "_id": "CHARS-16809-QKLNBT-73916",
    }


@patch("funclg.utils.data_mgmt.update_data")
def test_char_manager_update_data(m_db, test_character_mage):
    char_man.CHARACTER_DATA["data"] = {}
    char_man.CHARACTER_DATA["data"][test_character_mage["_id"]] = test_character_mage
    char_man.CHARACTER_DATA["objects"] = {}

    char_man.update_data()

    assert len(char_man.CHARACTER_DATA["data"]) == len(char_man.CHARACTER_DATA["objects"])
    assert m_db.called_once


@patch("funclg.utils.data_mgmt.update_data")
def test_char_manager_export_data(m_db, test_character_mage):
    _test_char_mage = test_character_mage.copy()
    _test_char_mage = char_man._update_char_role(test_character_mage, _test_char_mage)
    _test_char_mage = char_man._update_char_armor(test_character_mage, _test_char_mage)
    char_man.CHARACTER_DATA["objects"][_test_char_mage["_id"]] = char_man.Character(
        **_test_char_mage
    )
    char_man.CHARACTER_DATA["data"] = {}

    char_man.export_data()

    assert len(char_man.CHARACTER_DATA["data"]) == len(char_man.CHARACTER_DATA["objects"])
    assert _test_char_mage["_id"] in char_man.CHARACTER_DATA["data"]
    assert m_db.called_once


@patch("funclg.managers.character_manager.logger")
@patch("funclg.managers.character_manager.selection_validation")
def test_char_manager_select_character(m_sel, m_log, test_character_mage):
    # No Charater Data
    char_man.CHARACTER_DATA["data"] = {}
    assert char_man.select_character() is None
    assert m_log.warning.called

    # Character Data Exists
    char_man.CHARACTER_DATA["data"][test_character_mage["_id"]] = test_character_mage
    m_sel.return_value = test_character_mage["_id"]
    assert char_man.select_character() == test_character_mage["_id"]


@patch("builtins.print")
@patch("funclg.managers.character_manager.logger")
@patch("funclg.managers.character_manager.select_character")
def test_char_manager_show_character(m_sel, m_log, m_print, test_character_mage):
    # No Data
    m_sel.return_value = None
    char_man.show_character()
    assert m_log.warning.called

    # Return Test Value
    m_sel.return_value = test_character_mage["_id"]
    _test_char_mage = test_character_mage.copy()
    _test_char_mage = char_man._update_char_role(test_character_mage, _test_char_mage)
    _test_char_mage = char_man._update_char_armor(test_character_mage, _test_char_mage)
    char_man.CHARACTER_DATA["objects"][_test_char_mage["_id"]] = char_man.Character(
        **_test_char_mage
    )

    char_man.show_character()
    assert m_print.called_with(
        char_man.CHARACTER_DATA["objects"][test_character_mage["_id"]].details()
    )


@patch("builtins.print")
@patch("funclg.managers.character_manager.logger")
@patch("funclg.managers.character_manager.confirmation")
@patch("funclg.managers.character_manager.update_data")
@patch("funclg.managers.character_manager.select_character")
def test_char_manager_delete_role(m_sel, m_update, m_confirm, m_log, m_print, test_character_mage):
    # Yes Delete
    _tmp_char = test_character_mage.copy()
    _tmp_char = char_man._update_char_role(test_character_mage, _tmp_char)
    _tmp_char = char_man._update_char_armor(test_character_mage, _tmp_char)

    char_obj = char_man.Character(**_tmp_char)
    char_man.CHARACTER_DATA["objects"][char_obj.id] = char_obj
    char_man.CHARACTER_DATA["data"][char_obj.id] = test_character_mage

    m_sel.return_value = char_obj.id
    m_confirm.return_value = True

    char_man.delete_character()

    assert m_update.called
    assert char_obj.id not in char_man.CHARACTER_DATA["data"]
    assert char_obj.id not in char_man.CHARACTER_DATA["objects"]
    assert m_print.called_with(f"Delete {char_obj.name}")

    # No Delete
    char_man.CHARACTER_DATA["data"][char_obj.id] = test_character_mage

    m_sel.return_value = char_obj.id
    m_confirm.return_value = False
    char_man.delete_character()
    assert m_print.called_with("Keeping all characters alive...")

    # No select (Error Case)
    m_sel.return_value = None
    char_man.delete_character()
    assert m_log.warning.called


@patch("builtins.print")
@patch("funclg.managers.equipment_manager.filter_equipment_by_armor_type")
@patch("funclg.managers.character_manager.confirmation")
@patch("funclg.managers.character_manager.list_choice_selection")
def test_char_manager_pick_char_armor_equipment(m_lsel, m_confirm, m_fil_equip, m_print):
    t_chest = BodyEquipment(
        **{
            "name": "Basic Mage Tunic",
            "description": "Armor used by beginner mages",
            "item_type": 1,
            "armor_type": 1,
            "mod": {"adds": {"health": 100}, "mults": {"health": 0.45}},
            "_id": "ARMOR-16809-BCWSVN-76675",
        }
    )
    t_pants = BodyEquipment(
        **{
            "name": "Basic Mage Pants",
            "description": "Pants for a beginner mage",
            "item_type": 3,
            "armor_type": 1,
            "mod": {"adds": {"health": 459}, "mults": {"health": 0.51}},
            "_id": "ARMOR-16809-AEAYIE-76732",
        }
    )
    t_weapon = WeaponEquipment(
        **{
            "weapon_type": "Wand",
            "name": "Calins Wand",
            "description": "The original wand of Calin",
            "item_type": 4,
            "armor_type": 1,
            "mod": {"adds": {"attack": 337}, "mults": {"energy": 1}},
            "_id": "WEAPON-16645-ACIGL-01214",
        }
    )

    # TODO: Need to find the corret way to return thes results
    m_fil_equip.return_value = {
        "Head": {},
        "Chest": {t_chest.id: t_chest},
        "Back": {},
        "Pants": {t_pants.id: t_pants},
        "Weapon": {t_weapon.id: t_weapon},
    }
    m_lsel.side_effect = [t_chest.name, "Skip", t_weapon.name]
    m_confirm.side_effect = [True, True]

    selected_equipment = char_man._pick_char_armor_equipment("Medium", 1)

    expected_results = {"chest": t_chest, "weapon": t_weapon}

    assert m_print.called_with("There are not any Medium Head items, continuing...\n")
    assert m_print.called_with("There are not any Medium Back items, continuing...\n")
    for a_type, item in selected_equipment.items():
        assert item.name == expected_results[a_type].name
        assert item.id == expected_results[a_type].id

    # Testing No Pants Confirmation
    m_lsel.side_effect = [t_chest.name, t_pants.name, t_weapon.name]
    m_confirm.side_effect = [True, False, True]

    selected_equipment = char_man._pick_char_armor_equipment("Medium", 1)

    expected_results = {"chest": t_chest, "weapon": t_weapon}

    assert m_print.called_with("There are not any Medium Head items, continuing...\n")
    assert m_print.called_with("There are not any Medium Back items, continuing...\n")
    for a_type, item in selected_equipment.items():
        if expected_results.get(a_type):
            assert item.name == expected_results[a_type].name
            assert item.id == expected_results[a_type].id
        else:
            assert item == None


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.roles_manager.sort_roles_by_armor_type")
@patch("funclg.managers.character_manager.update_data")
@patch("funclg.managers.character_manager._pick_char_armor_equipment")
@patch("funclg.managers.character_manager.confirmation")
@patch("funclg.managers.character_manager.string_validation")
@patch("funclg.managers.character_manager.list_choice_selection")
def test_char_man_build_character(
    m_lsel,
    m_str_val,
    m_confirm,
    m_char_armor_sel,
    m_update,
    m_sort_roles,
    m_id,
    test_character_mage,
):
    # Define Test Roles
    _t_mage = test_character_mage.copy()
    _t_mage["role"] = test_character_mage["role"].copy()
    _t_mage["armor"] = test_character_mage["armor"].copy()

    _t_mage["role"]["abilities"] = [
        Abilities(**_ability) for _ability in _t_mage["role"]["abilities"].copy()
    ]
    t_mage = Roles(**_t_mage["role"])

    t_warrior = Roles(
        **{
            "name": "Warrior",
            "description": "Fierce figher",
            "armor_type": 2,
            "ability_types": ["None"],
            "abilities": [],
            "_id": "ROLES-16695-FENWUF-20643",
        }
    )
    t_rouge = Roles(
        **{
            "name": "Rouge",
            "description": "Sneaky Assassin",
            "armor_type": 0,
            "ability_types": ["None"],
            "abilities": [],
            "_id": "ROLES-16695-GIEJNN-20644",
        }
    )

    # Define Test Equipment
    t_chest = BodyEquipment(
        **{
            "name": "Basic Mage Tunic",
            "description": "Armor used by beginner mages",
            "item_type": 1,
            "armor_type": 1,
            "mod": {"adds": {"health": 100}, "mults": {"health": 0.45}},
            "_id": "ARMOR-16809-BCWSVN-76675",
        }
    )

    t_weapon = WeaponEquipment(
        **{
            "weapon_type": "Wand",
            "name": "Calins Wand",
            "description": "The original wand of Calin",
            "item_type": 4,
            "armor_type": 1,
            "mod": {"adds": {"attack": 337}, "mults": {"energy": 1}},
            "_id": "WEAPON-16645-ACIGL-01214",
        }
    )

    m_sort_roles.return_value = {"Light": [t_rouge], "Medium": [t_mage], "Heavy": [t_warrior]}

    # Roles Exist, Add Equipment, Save Character

    m_str_val.return_value = _t_mage["name"]
    m_char_armor_sel.return_value = {"chest": t_chest, "weapon": t_weapon}
    m_lsel.side_effect = ["Medium", "Mage"]
    m_confirm.side_effect = [True, True]
    m_id.side_effect = [ability.id for ability in t_mage.abilities] + [
        t_mage.id,
        t_warrior.id,
        t_rouge.id,
        t_chest.id,
        t_weapon.id,
        _t_mage["_id"],
    ]

    char_man.build_character()

    result = char_man.CHARACTER_DATA["data"].get(_t_mage["_id"], False)

    assert test_character_mage["_id"] in char_man.CHARACTER_DATA["data"].keys()
    assert m_update.called
    assert result

    result["armor"]["chest"] = result["armor"]["chest"].export()
    result["armor"]["weapon"] = result["armor"]["weapon"].export()
    result["role"]["abilities"] = [ability.export() for ability in result["role"]["abilities"]]

    assert test_character_mage == result


@patch("funclg.managers.character_manager.logger")
@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.roles_manager.sort_roles_by_armor_type")
@patch("funclg.managers.character_manager.update_data")
@patch("funclg.managers.character_manager._pick_char_armor_equipment")
@patch("funclg.managers.character_manager.confirmation")
@patch("funclg.managers.character_manager.string_validation")
@patch("funclg.managers.character_manager.list_choice_selection")
def test_char_man_build_character_no_roles(
    m_lsel,
    m_str_val,
    m_confirm,
    m_char_armor_sel,
    m_update,
    m_sort_roles,
    m_id,
    m_log,
    test_character_mage,
):
    # Define Mocks
    m_str_val.return_value = "Test Mage"
    m_confirm.side_effect = [True, True]
    m_sort_roles.return_value = {}

    assert not char_man.build_character()
    assert m_log.warning.called


@patch("funclg.managers.character_manager.logger")
@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.roles_manager.sort_roles_by_armor_type")
@patch("funclg.managers.character_manager.update_data")
@patch("funclg.managers.character_manager._pick_char_armor_equipment")
@patch("funclg.managers.character_manager.confirmation")
@patch("funclg.managers.character_manager.string_validation")
@patch("funclg.managers.character_manager.list_choice_selection")
def test_char_man_build_character_no_equip_no_save(
    m_lsel,
    m_str_val,
    m_confirm,
    m_char_armor_sel,
    m_update,
    m_sort_roles,
    m_id,
    m_log,
    test_character_mage,
):
    # Define Test Roles
    _t_mage = test_character_mage.copy()
    _t_mage["role"] = test_character_mage["role"].copy()
    _t_mage["armor"] = test_character_mage["armor"].copy()
    _t_mage["_id"] = "ROLES-16234-FEJOWK-09834"

    _t_mage["role"]["abilities"] = [
        Abilities(**_ability) for _ability in _t_mage["role"]["abilities"].copy()
    ]
    t_mage = Roles(**_t_mage["role"])

    t_warrior = Roles(
        **{
            "name": "Warrior",
            "description": "Fierce figher",
            "armor_type": 2,
            "ability_types": ["None"],
            "abilities": [],
            "_id": "ROLES-16695-FENWUF-20643",
        }
    )
    t_rouge = Roles(
        **{
            "name": "Rouge",
            "description": "Sneaky Assassin",
            "armor_type": 0,
            "ability_types": ["None"],
            "abilities": [],
            "_id": "ROLES-16695-GIEJNN-20644",
        }
    )

    m_sort_roles.return_value = {"Light": [t_rouge], "Medium": [t_mage], "Heavy": [t_warrior]}

    m_str_val.return_value = _t_mage["name"]
    m_lsel.side_effect = ["Medium", "Mage"]
    m_id.side_effect = [ability.id for ability in t_mage.abilities] + [
        t_mage.id,
        t_warrior.id,
        t_rouge.id,
        _t_mage["_id"],
    ]
    m_confirm.side_effect = [False, False]

    char_man.build_character()

    assert not char_man.CHARACTER_DATA["data"].get(_t_mage["_id"], False)
    assert not m_update.called
