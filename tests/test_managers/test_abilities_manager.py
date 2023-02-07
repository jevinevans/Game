"""
Description: The is a unit test for the abilties manager class.
Developer: Jevin Evans
Date: 11.12.2022
"""

from unittest.mock import patch

import pytest

import funclg.managers.abilities_manager as ab_man


@pytest.fixture
def test_magic():
    return {
        "name": "Test_Magic",
        "description": "Test Magic",
        "ability_type": "Magic",
        "_target": "self",
        "mod": {"base": {"attack": 200}, "percentage": {}},
        "_id": "ABILITY-12345-EJFI-67890",
    }


@patch("funclg.utils.data_mgmt.update_data")
def test_abilities_manager_update_data(m_db, test_magic):
    ab_man.ABILITIES_DATA["data"][test_magic["_id"]] = test_magic
    ab_man.ABILITIES_DATA["objects"] = {}

    ab_man.update_data()

    assert len(ab_man.ABILITIES_DATA["data"]) == len(ab_man.ABILITIES_DATA["objects"])
    assert m_db.called_once


@patch("funclg.utils.data_mgmt.update_data")
def test_abilities_manager_export_data(m_db, test_magic):
    ab_man.ABILITIES_DATA["objects"][test_magic["_id"]] = ab_man.Abilities(**test_magic)

    ab_man.export_data()
    assert len(ab_man.ABILITIES_DATA["data"]) == len(ab_man.ABILITIES_DATA["objects"])
    assert test_magic["_id"] in ab_man.ABILITIES_DATA["data"]
    assert m_db.called_once


@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.selection_validation")
def test_abilities_manager_select_ability(m_sel, m_log, test_magic):
    # Data Exists - Select Success
    ab_man.ABILITIES_DATA["data"][test_magic["_id"]] = test_magic
    m_sel.return_value = test_magic["_id"]

    assert ab_man.select_ability() == test_magic["_id"]

    # Data Not Exists - Return Nothing
    ab_man.ABILITIES_DATA["data"] = {}
    assert ab_man.select_ability() is None
    assert m_log.warning.called_with("There are no abilities available.")


@patch("builtins.print")
@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.select_ability")
def test_abilities_manager_show_ability(m_sel, m_log, m_print, test_magic):
    # Success Test
    m_sel.return_value = test_magic["_id"]
    _ability = ab_man.Abilities(**test_magic)
    ab_man.ABILITIES_DATA["objects"][test_magic["_id"]] = _ability

    ab_man.show_ability()
    assert m_print.called_with(_ability.details())

    # No Data
    m_sel.return_value = None
    ab_man.show_ability()
    assert m_log.warning.called_with("There are no abilities to show.")


@patch("builtins.print")
@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.confirmation")
@patch("funclg.managers.abilities_manager.update_data")
@patch("funclg.managers.abilities_manager.select_ability")
def test_abilities_manager_delete_ability(m_sel, m_upd, m_confirm, m_log, m_print, test_magic):
    # Success Delete
    _mag = ab_man.Abilities(**test_magic)
    ab_man.ABILITIES_DATA["data"][_mag.id] = test_magic
    ab_man.ABILITIES_DATA["objects"][_mag.id] = _mag

    m_sel.return_value = _mag.id
    m_confirm.return_value = True

    ab_man.delete_ability()

    assert _mag.id not in ab_man.ABILITIES_DATA["data"]
    assert _mag.id not in ab_man.ABILITIES_DATA["objects"]
    assert m_print.called_with(f"Deleting {_mag.name}")
    assert m_upd.called

    # No Delete
    _mag = ab_man.Abilities(**test_magic)
    ab_man.ABILITIES_DATA["data"][_mag.id] = test_magic

    m_sel.return_value = _mag.id
    m_confirm.return_value = False

    ab_man.delete_ability()

    assert m_print.called_with("Keeping all abilities in the vault...")

    # No Id

    m_sel.return_value = None
    ab_man.delete_ability()
    assert m_log.warning.called


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.generate_modifier")
@patch("funclg.managers.abilities_manager.update_data")
@patch("funclg.managers.abilities_manager.confirmation")
@patch("funclg.managers.abilities_manager.selection_validation")
@patch("funclg.managers.abilities_manager.string_validation")
def test_abilities_manager_build_ability(
    m_str_val, m_sel, m_confirm, m_update, m_mod_gen, m_id, test_magic
):
    m_sel.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_confirm.return_value = True

    _mag = ab_man.Abilities(**test_magic)

    ab_man.build_ability()

    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["_id"] == _mag.id
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["name"] == _mag.name
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["description"] == _mag.description
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["ability_type"] == _mag.ability_type
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["_target"] == _mag._target
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["mod"]["base"] == _mag.mod.base
    assert (
        ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["mod"]["percentage"] == _mag.mod.percentage
    )
    assert m_update.called
    print(m_update.called, m_update.call_count)

    # Test Not Saved - Coverage
    m_sel.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_confirm.return_value = False

    ab_man.build_ability()

    assert m_update.call_count == 1


def test_abilities_manager_filter_abilities_by_types():
    ab_man.load_data()
    assert ab_man.ABILITIES_DATA["objects"]

    # Single Type Test
    results = ab_man.filter_abilities_by_types(["Magic"])

    assert "Magic" in results
    for t_ability in results["Magic"]:
        assert t_ability.ability_type == "Magic"

    # # Multiple Types Test
    results = ab_man.filter_abilities_by_types(["Buff", "Physical"])
    for a_type in ["Buff", "Physical"]:
        assert a_type in results
        for t_ability in results[a_type]:
            assert t_ability.ability_type == a_type

    # Test None Types
    results = ab_man.filter_abilities_by_types(["None"])
    assert "None" in results

    for t_ability in results["None"]:
        assert t_ability.ability_type == "None"

    results = ab_man.filter_abilities_by_types([])
    assert not results
