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
        "mod": {"adds": {"attack": 200}, "mults": {}},
        "_id": "ABILITY-12345-EJFI-67890",
    }


@patch("funclg.utils.data_mgmt.update_data")
def test_abilities_manager_update_data(m_db, test_magic):
    ab_man.ABILITIES_DATA["data"][test_magic["_id"]] = test_magic

    assert len(ab_man.ABILITIES_DATA["objects"]) != 0
    assert len(ab_man.ABILITIES_DATA["data"]) != len(ab_man.ABILITIES_DATA["objects"])

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
@patch("funclg.managers.abilities_manager.char_manager_choice_selection")
def test_abilities_manager_select_ability(m_chr_sel, m_log, test_magic):
    # Data Exists - Select Success
    ab_man.ABILITIES_DATA["data"][test_magic["_id"]] = test_magic
    m_chr_sel.return_value = test_magic["_id"]

    assert ab_man.select_ability() == test_magic["_id"]

    # Data Not Exists - Return Nothing
    ab_man.ABILITIES_DATA["data"] = {}
    assert ab_man.select_ability() == None
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
@patch("funclg.managers.abilities_manager.yes_no_validation")
@patch("funclg.managers.abilities_manager.update_data")
@patch("funclg.managers.abilities_manager.select_ability")
def test_abilities_manager_delete_ability(m_sel, m_upd, m_yn_val, m_log, m_print, test_magic):
    # Success Delete
    _mag = ab_man.Abilities(**test_magic)
    ab_man.ABILITIES_DATA["data"][_mag.id] = test_magic
    ab_man.ABILITIES_DATA["objects"][_mag.id] = _mag

    m_sel.return_value = _mag.id
    m_yn_val.return_value = True

    ab_man.delete_ability()

    assert _mag.id not in ab_man.ABILITIES_DATA["data"]
    assert _mag.id not in ab_man.ABILITIES_DATA["objects"]
    assert m_print.called_with(f"Deleting {_mag.name}")
    assert m_upd.called

    # No Delete
    _mag = ab_man.Abilities(**test_magic)
    ab_man.ABILITIES_DATA["data"][_mag.id] = test_magic

    m_sel.return_value = _mag.id
    m_yn_val.return_value = False

    ab_man.delete_ability()

    assert m_print.called_with("Keeping all abilities in the vault...")

    # No Id

    m_sel.return_value = None
    ab_man.delete_ability()
    assert m_log.warning.called


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.modifier_manager.generate_modifier")
@patch("funclg.managers.abilities_manager.update_data")
@patch("funclg.managers.abilities_manager.yes_no_validation")
@patch("funclg.managers.abilities_manager.list_choice_selection")
@patch("funclg.managers.abilities_manager.string_validation")
def test_abilities_manager_build_ability(
    m_str_val, m_list_val, m_yn_val, m_update, m_mod_gen, m_id, test_magic
):
    m_list_val.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_yn_val.return_value = True

    _mag = ab_man.Abilities(**test_magic)

    ab_man.build_ability()

    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["_id"] == _mag.id
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["name"] == _mag.name
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["description"] == _mag.description
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["ability_type"] == _mag.ability_type
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["_target"] == _mag._target
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["mod"]["adds"] == _mag.mod.adds
    assert ab_man.ABILITIES_DATA["data"][test_magic["_id"]]["mod"]["mults"] == _mag.mod.mults
    assert m_update.called
    print(m_update.called, m_update.call_count)

    # Test Not Saved - Coverage
    m_list_val.return_value = test_magic["ability_type"]
    m_str_val.side_effect = [test_magic["name"], test_magic["description"]]
    m_mod_gen.return_value = test_magic["mod"]
    m_id.return_value = test_magic["_id"]
    m_yn_val.return_value = False

    ab_man.build_ability()

    assert m_update.call_count == 1


def test_abilities_manager_filter_abilities_by_types():

    assert ab_man.ABILITIES_DATA["objects"]

    # Single Type Test
    results = ab_man.filter_abilities_by_types(["Magic"])

    assert "Magic" in results
    assert all([ab.ability_type == "Magic" for ab in results["Magic"]])

    # # Multiple Types Test
    results = ab_man.filter_abilities_by_types(["Buff", "Physical"])
    for x in ["Buff", "Physical"]:
        assert x in results
        assert all([ab.ability_type == x for ab in results[x]])

    # Test None Types
    results = ab_man.filter_abilities_by_types(["None"])
    assert "None" in results
    assert all([ab.ability_type == "None" for ab in results["None"]])

    results = ab_man.filter_abilities_by_types([])
    assert not results
