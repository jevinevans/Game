"""
Description: The is a unit test for the abilties manager class.
Developer: Jevin Evans
Date: 11.12.2022
"""

from unittest.mock import patch
from funclg.character.abilities import Abilities


@patch("funclg.utils.data_mgmt.update_data")
def test_abilities_manager_update_data(m_db, test_ability_manager,test_magic, ):

    test_ability_manager.data[test_magic["_id"]] = test_magic
    test_ability_manager.update_data()

    assert len(test_ability_manager.data) == len(test_ability_manager.objects)
    assert m_db.assert_called_once


@patch("funclg.utils.data_mgmt.update_data")
def test_abilities_manager_export_data(m_db, test_ability_manager,test_magic):
    test_ability_manager.objects[test_magic["_id"]] = Abilities(**test_magic)

    test_ability_manager.export_data()
    assert len(test_ability_manager.data) == len(test_ability_manager.objects)
    assert test_magic["_id"] in test_ability_manager.data
    assert m_db.assert_called_once


@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.AbilitiesManager.get_selection")
def test_abilities_manager_select_ability(m_sel, m_log, test_ability_manager, test_magic):
    # Data Exists - Select Success
    test_ability_manager.data[test_magic["_id"]] = test_magic
    m_sel.return_value = test_magic["_id"]

    assert test_ability_manager.select_ability() == test_magic["_id"]

    # Data Not Exists - Return Nothing
    test_ability_manager.data = {}
    assert test_ability_manager.select_ability() is None
    m_log.warning.assert_called_with("There are no abilities available.")


@patch("builtins.print")
@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.AbilitiesManager.select_ability")
def test_abilities_manager_show_ability(m_sel, m_log, m_print, test_ability_manager, test_magic):
    # Success Test
    m_sel.return_value = test_magic["_id"]
    _ability = Abilities(**test_magic)
    test_ability_manager.objects[test_magic["_id"]] = _ability
    test_ability_manager.show_ability()
    m_print.assert_called_with(_ability.details())

    # No Data
    m_sel.return_value = None
    test_ability_manager.show_ability()
    m_log.warning.assert_called_with("There are no abilities to show.")


@patch("builtins.print")
@patch("funclg.managers.abilities_manager.logger")
@patch("funclg.managers.abilities_manager.AbilitiesManager.get_confirmation")
@patch("funclg.managers.abilities_manager.AbilitiesManager.update_data")
@patch("funclg.managers.abilities_manager.AbilitiesManager.select_ability")
def test_abilities_manager_delete_ability(m_sel, m_upd, m_confirm, m_log, m_print, test_ability_manager, test_magic):
    # Success Delete
    _mag = Abilities(**test_magic)
    test_ability_manager.data[_mag.id] = test_magic
    test_ability_manager.objects[_mag.id] = _mag
    m_sel.return_value = _mag.id
    m_confirm.return_value = True

    test_ability_manager.delete_ability()
    assert _mag.id not in test_ability_manager.data
    assert _mag.id not in test_ability_manager.objects
    m_print.assert_called_with(f"Deleting {_mag.name}")
    assert m_upd.called

    # No Delete
    _mag = Abilities(**test_magic)
    test_ability_manager.data[_mag.id] = test_magic
    test_ability_manager.objects[_mag.id] = _mag

    m_sel.return_value = _mag.id
    m_confirm.return_value = False

    test_ability_manager.delete_ability()

    m_print.assert_called_with("Keeping all abilities in the vault...")

    # No Id

    m_sel.return_value = None
    test_ability_manager.delete_ability()
    assert m_log.warning.called


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.generate_modifier")
@patch("funclg.managers.abilities_manager.AbilitiesManager.update_data")
@patch("funclg.managers.abilities_manager.AbilitiesManager.get_confirmation")
@patch("funclg.managers.abilities_manager.AbilitiesManager.get_selection")
@patch("funclg.managers.abilities_manager.AbilitiesManager.get_string")
def test_abilities_manager_build_ability(
    m_str_val, m_sel, m_confirm, m_update, m_mod_gen, m_id, test_ability_manager, test_magic
):
    m_sel.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_confirm.return_value = True

    _mag = Abilities(**test_magic)

    test_ability_manager.build_ability()

    assert test_ability_manager.data[test_magic["_id"]]["_id"] == _mag.id
    assert test_ability_manager.data[test_magic["_id"]]["name"] == _mag.name
    assert test_ability_manager.data[test_magic["_id"]]["description"] == _mag.description
    assert test_ability_manager.data[test_magic["_id"]]["ability_type"] == _mag.ability_type
    assert test_ability_manager.data[test_magic["_id"]]["_target"] == _mag._target
    assert test_ability_manager.data[test_magic["_id"]]["mod"]["base"] == _mag.mod.base
    assert (
        test_ability_manager.data[test_magic["_id"]]["mod"]["percentage"] == _mag.mod.percentage
    )
    assert m_update.called

    # Test Not Saved - Coverage
    m_sel.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_confirm.return_value = False

    test_ability_manager.build_ability()

    assert m_update.call_count == 1


def test_abilities_manager_filter_abilities_by_types(test_ability_manager):
    test_ability_manager.load_data()
    assert test_ability_manager.objects

    # Single Type Test
    results = test_ability_manager.filter_abilities_by_types(["Magic"])

    assert "Magic" in results
    for t_ability in results["Magic"]:
        assert t_ability.ability_type == "Magic"

    # # Multiple Types Test
    results = test_ability_manager.filter_abilities_by_types(["Buff", "Physical"])
    for a_type in ["Buff", "Physical"]:
        assert a_type in results
        for t_ability in results[a_type]:
            assert t_ability.ability_type == a_type

    # Test None Types
    results = test_ability_manager.filter_abilities_by_types(["None"])
    assert "None" in results

    for t_ability in results["None"]:
        assert t_ability.ability_type == "None"

    results = test_ability_manager.filter_abilities_by_types([])
    assert not results
