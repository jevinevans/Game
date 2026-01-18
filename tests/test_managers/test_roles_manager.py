"""
Description: This module is to unit test the funclg.managers.roles_manager module
Developer: Jevin Evans
Date: 2.6.2022
"""

from unittest.mock import patch

import pytest


from funclg.character.abilities import Abilities
from funclg.character.roles import Roles
from funclg.utils.types import ABILITY_TYPES, ARMOR_TYPES


@pytest.fixture
def test_mage():
    return {
        "name": "Mage",
        "description": "Wielders of magic",
        "armor_type": 1,
        "level": 1,
        "stats": {
            "attributes": {"attack": 5, "health": 5, "energy": 5, "defense": 5},
            "modifiers": {},
        },
        "ability_types": ["Magic", "Restore", "Buff", "Debuff"],
        "abilities": [
            {
                "name": "Fireball",
                "description": "Throws a fireball at target",
                "ability_type": "Magic",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {"defense": -446}, "percentage": {}},
                "_id": "ABILITY-16650-OKNG-98180",
            },
            {
                "name": "Heal",
                "description": "Heals the users mod",
                "ability_type": "Restore",
                "_target": "self",
                "level": 0,
                "mod": {"base": {}, "percentage": {"energy": 0.45}},
                "_id": "ABILITY-16650-DOTD-98286",
            },
            {
                "name": "Empower",
                "description": "Strengthens player",
                "ability_type": "Buff",
                "_target": "self",
                "level": 0,
                "mod": {"base": {}, "percentage": {"defense": 0.98}},
                "_id": "ABILITY-16650-DXUF-98274",
            },
            {
                "name": "Weaken",
                "description": "Weakens an enemy",
                "ability_type": "Debuff",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {}, "percentage": {"defense": -0.83}},
                "_id": "ABILITY-16660-TXKX-31305",
            },
            {
                "name": "Lightning",
                "description": "Sends a bolt of lightning towards the enemy",
                "ability_type": "Magic",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {"health": -240}, "percentage": {}},
                "_id": "ABILITY-16694-TRKE-96324",
            },
        ],
        "_id": "ROLES-12345-ABCDEF-67890",
    }


@pytest.fixture
def test_warrior():
    return {
        "name": "Warrior",
        "description": "Guardian, Protector",
        "armor_type": 2,
        "level": 1,
        "stats": {
            "attributes": {"attack": 5, "health": 5, "energy": 5, "defense": 5},
            "modifiers": {},
        },
        "ability_types": ["Physical", "Buff", "Debuff", "None"],
        "abilities": [
            {
                "name": "Strike",
                "description": "Strikes an enemy with the users weapon",
                "ability_type": "Physical",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {"health": 225}, "percentage": {}},
                "_id": "ABILITY-16659-NYWC-46543",
            },
            {
                "name": "Weaken",
                "description": "Weakens an enemy",
                "ability_type": "Debuff",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {}, "percentage": {"defense": 0.83}},
                "_id": "ABILITY-16660-TXKX-31305",
            },
        ],
        "_id": "ROLES-16694-QPYDLP-95720",
    }


@pytest.fixture
def test_rouge():
    return {
        "name": "Rouge",
        "level": 1,
        "description": "Quick knife wielders",
        "armor_type": 0,
        "stats": {
            "attributes": {"attack": 5, "health": 5, "energy": 5, "defense": 5},
            "modifiers": {},
        },
        "ability_types": ["Physical", "Buff", "Debuff", "None"],
        "abilities": [
            {
                "name": "Strike",
                "description": "Strikes an enemy with the users weapon",
                "ability_type": "Physical",
                "_target": "enemy",
                "level": 0,
                "mod": {"base": {"health": 225}, "percentage": {}},
                "_id": "ABILITY-16659-NYWC-46543",
            },
            {
                "name": "Weaken",
                "description": "Weakens an enemy",
                "ability_type": "Debuff",
                "level": 0,
                "_target": "enemy",
                "mod": {"base": {}, "percentage": {"defense": 0.83}},
                "_id": "ABILITY-16660-TXKX-31305",
            },
        ],
        "_id": "ROLES-12345-GHIJKL-67890",
    }


@pytest.fixture
def test_no_abilities():
    return {
        "name": "Cleric",
        "description": "Magic Healer",
        "armor_type": 1,
        "level": 1,
        "stats": {
            "attributes": {"attack": 5, "health": 5, "energy": 5, "defense": 5},
            "modifiers": {},
        },
        "ability_types": ["Magic", "Restore", "Buff"],
        "abilities": [],
        "_id": "ROLES-16683-UAJMFU-16064",
    }


@patch("funclg.utils.data_mgmt.update_data")
def test_roles_manager_update_data(m_db,test_roles_manager, test_mage):
    test_roles_manager.data[test_mage["_id"]] = test_mage
    test_roles_manager.objects = {}

    test_roles_manager.update_data()

    assert len(test_roles_manager.data) == len(test_roles_manager.objects)
    assert m_db.assert_called_once


@patch("funclg.utils.data_mgmt.update_data")
def test_roles_manager_export_data(m_db,test_roles_manager, test_mage):
    _test_mage = test_mage.copy()
    _test_mage["abilities"] = [Abilities(**_ability) for _ability in test_mage["abilities"]]
    test_roles_manager.objects[test_mage["_id"]] = Roles(**_test_mage)

    test_roles_manager.export_data()
    assert len(test_roles_manager.data) == len(test_roles_manager.objects)
    assert test_mage["_id"] in test_roles_manager.data
    assert m_db.assert_called_once


@patch("funclg.managers.roles_manager.logger")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
def test_roles_manager_select_role(m_sel, m_log,test_roles_manager, test_mage):
    # Test Data Exist
    test_roles_manager.data[test_mage["_id"]] = test_mage
    m_sel.return_value = test_mage["_id"]

    assert test_roles_manager.select_role() == test_mage["_id"]

    # Test Data Not Exist
    test_roles_manager.data = {}
    assert test_roles_manager.select_role() is None
    assert m_log.warning.called


@patch("builtins.print")
@patch("funclg.managers.roles_manager.logger")
@patch("funclg.managers.roles_manager.RolesManager.select_role")
def test_roles_manager_show_role(m_sel, m_log, m_print, test_roles_manager, test_mage):
    # Success Test
    m_sel.return_value = test_mage["_id"]
    _test_mage = test_mage.copy()
    _test_mage["abilities"] = [Abilities(**_ability) for _ability in test_mage["abilities"]]
    test_role = Roles(**_test_mage)
    test_roles_manager.objects[test_mage["_id"]] = test_role

    test_roles_manager.show_role()
    m_print.assert_called_with(test_role.details())

    # No Data
    m_sel.return_value = None
    test_roles_manager.show_role()
    assert m_log.warning.called


@patch("builtins.print")
@patch("funclg.managers.roles_manager.logger")
@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
@patch("funclg.managers.roles_manager.RolesManager.update_data")
@patch("funclg.managers.roles_manager.RolesManager.select_role")
def test_roles_manager_delete_role(m_sel, m_update, m_confirm, m_log, m_print,test_roles_manager, test_mage):
    # Yes Delete
    _test_mage = test_mage.copy()
    _test_mage["abilities"] = [Abilities(**_ability) for _ability in test_mage["abilities"]]
    test_mage_obj = Roles(**_test_mage)

    test_roles_manager.data[test_mage_obj.id] = test_mage
    test_roles_manager.objects[test_mage_obj.id] = test_mage_obj

    m_sel.return_value = test_mage_obj.id
    m_confirm.return_value = True

    test_roles_manager.delete_role()

    assert m_update.called
    assert test_mage_obj.id not in test_roles_manager.data
    assert test_mage_obj.id not in test_roles_manager.objects
    m_print.assert_called_with(f"Deleteing {test_mage_obj.name}")

    # No Delete
    test_roles_manager.data[test_mage_obj.id] = test_mage

    m_sel.return_value = test_mage_obj.id
    m_confirm.return_value = False

    test_roles_manager.delete_role()
    m_print.assert_called_with("Keeping all roles in the vault...")

    # No select role returned
    m_sel.return_value = None
    test_roles_manager.delete_role()
    assert m_log.warning.called


@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
def test_roles_manager_select_ability_types(m_sel, m_confirm, test_roles_manager, test_mage):
    # Test Success
    ability_results = list({ability["ability_type"] for ability in test_mage["abilities"]})
    yn_side_effects = [True for _ in range(len(ability_results) - 1)]
    yn_side_effects.append(False)

    m_sel.side_effect = ability_results
    m_confirm.side_effect = yn_side_effects

    assert ability_results == test_roles_manager._select_ability_types()


@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
def test_roles_manager_select_role_abilities(m_sel, m_confirm, test_roles_manager, test_ability_manager, test_mage):
    test_ability_manager.load_data()
    # Success Test
    abilities = test_mage["abilities"]
    ability_objs = [Abilities(**_ability) for _ability in test_mage["abilities"]]

    m_sel_effects = []

    for ability in abilities:
        m_sel_effects.append(ability["ability_type"])
        m_sel_effects.append(ability["name"])

    m_sel.side_effect = m_sel_effects
    m_confirm.side_effect = [True * len(m_sel_effects), False]

    selected_abilities = test_roles_manager._select_role_abilities(test_mage["ability_types"])
    for ab_test, ab_val in zip(selected_abilities, ability_objs):
        assert ab_test.id == ab_val.id
        assert ab_test.name == ab_val.name


@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
def test_roles_manager_select_role_abilities_no_abilities_added(m_sel, m_confirm, test_roles_manager, test_mage):
    # No abilities added
    abilities = test_mage["abilities"]
    m_sel.side_effect = [abilities[0]["ability_type"], abilities[0]["name"]]
    m_confirm.side_effect = [False, False]

    selected_abilities = test_roles_manager._select_role_abilities(test_mage["ability_types"])
    assert not selected_abilities


@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
def test_roles_manager_select_role_abilities_limited_added(m_sel, m_confirm, test_roles_manager, test_ability_manager, test_mage):
    test_ability_manager.load_data()
    # Limited ability type
    test_heal_ability = {
        "name": "Heal",
        "description": "Heals the users mod",
        "ability_type": "Restore",
        "_target": "self",
        "mod": {"base": {}, "percentage": {"energy": 0.45}},
        "_id": "ABILITY-16650-DOTD-98286",
    }
    with patch("funclg.managers.abilities_manager") as ab_man:
        ab_man.filter_abilities_by_types.return_value = {
            "Restore": {Abilities(**test_heal_ability)}
        }
        m_sel.side_effect = ["Restore", "Heal", "Restore"]
        m_confirm.side_effect = [True, True, False]

        selected_abilities = test_roles_manager._select_role_abilities(["Restore"])
        assert len(selected_abilities) == 1


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.build_stats")
@patch("funclg.managers.roles_manager.RolesManager._select_role_abilities")
@patch("funclg.managers.roles_manager.RolesManager._select_ability_types")
@patch("funclg.managers.roles_manager.RolesManager.update_data")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
@patch("funclg.managers.roles_manager.RolesManager.get_string")
@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
def test_roles_manager_build_role_with_save(
    m_confirm, m_str_val, m_sel, m_update, m_sel_ab_type, m_sel_rol_ab, m_stats_gen, m_id, test_roles_manager, test_mage
):
    # Success Create Test Mage
    m_str_val.side_effect = [test_mage["name"], test_mage["description"]]
    ability_types = list({ability["ability_type"] for ability in test_mage["abilities"]})
    m_sel.return_value = ARMOR_TYPES[test_mage["armor_type"]]
    m_stats_gen.return_value = test_mage["stats"]
    m_sel_ab_type.return_value = ability_types
    m_sel_rol_ab.return_value = [Abilities(**_ability) for _ability in test_mage["abilities"]]
    m_confirm.return_value = True

    mock_ids = [ability["_id"] for ability in test_mage["abilities"]]
    mock_ids.append(test_mage["_id"])

    m_id.side_effect = mock_ids

    test_roles_manager.build_role()

    test_mage["ability_types"].sort()
    test_roles_manager.data[test_mage["_id"]]["ability_types"].sort()

    assert test_mage["_id"] in test_roles_manager.data
    assert test_mage == test_roles_manager.data[test_mage["_id"]]
    m_sel_rol_ab.assert_called_with(ability_types)
    assert m_confirm.called
    assert m_update.called


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.build_stats")
@patch("funclg.managers.roles_manager.RolesManager._select_role_abilities")
@patch("funclg.managers.roles_manager.RolesManager._select_ability_types")
@patch("funclg.managers.roles_manager.RolesManager.update_data")
@patch("funclg.managers.roles_manager.RolesManager.get_selection")
@patch("funclg.managers.roles_manager.RolesManager.get_string")
@patch("funclg.managers.roles_manager.RolesManager.get_confirmation")
def test_roles_manager_build_role_no_save(
    m_confirm, m_str_val, m_sel, m_update, m_sel_ab_type, m_sel_rol_ab, m_stats_gen, m_id, test_roles_manager, test_mage
):
    test_roles_manager.load_data()
    
    # No Save
    m_str_val.side_effect = [test_mage["name"], test_mage["description"]]
    ability_types = list({ability["ability_type"] for ability in test_mage["abilities"]})
    m_sel.return_value = ARMOR_TYPES[test_mage["armor_type"]]
    m_stats_gen.return_value = test_mage["stats"]
    m_sel_ab_type.return_value = ability_types
    m_sel_rol_ab.return_value = [Abilities(**_ability) for _ability in test_mage["abilities"]]
    m_confirm.return_value = False

    mock_ids = [ability["_id"] for ability in test_mage["abilities"]]
    mock_ids.append(test_mage["_id"])

    m_id.side_effect = mock_ids
    test_roles_manager.build_role()

    assert not test_roles_manager.data.get(test_mage["_id"], False)


def test_roles_manager_sort_roles_by_armor_type(
    test_roles_manager, test_mage, test_warrior, test_rouge, test_no_abilities
):
    def _gen_class(role_dict: dict):
        role_abilities = [Abilities(**_ability) for _ability in role_dict["abilities"]]
        role_dict["abilities"] = role_abilities
        return Roles(**role_dict)

    role_objs = {
        "mage": _gen_class(test_mage),
        "warrior": _gen_class(test_warrior),
        "rouge": _gen_class(test_rouge),
        "cleric": _gen_class(test_no_abilities),
    }

    test_roles_manager.objects = {}

    test_roles_manager.objects.update(role_objs)

    sort_results = {
        "Light": [role_objs["rouge"]],
        "Medium": [role_objs["mage"], role_objs["cleric"]],
        "Heavy": [role_objs["warrior"]],
    }

    assert sort_results == test_roles_manager.sort_roles_by_armor_type()
