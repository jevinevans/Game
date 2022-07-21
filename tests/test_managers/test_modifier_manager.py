from unittest.mock import call, patch

import pytest

import funclg.managers.modifier_manager as mod_man

@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.utils.data_mgmt.update_data")
@patch("funclg.managers.modifier_manager.yes_no_validation")
@patch("funclg.managers.modifier_manager.number_range_validation")
@patch("funclg.managers.modifier_manager.string_validation")
@patch("funclg.managers.modifier_manager.list_choice_selection")
def test_modifier_manager_build_modifier_add_mod(
    m_list_select, m_str_val, m_num_range, m_yn_val, m_db_update, m_id_gen
):
    # Test new build method (no name, no from method)
    m_str_val.side_effect = ["Test_mod"]
    m_list_select.side_effect = ["energy", "Base Change"]
    m_num_range.side_effect = [50]
    m_yn_val.side_effect = [True, False]
    m_id_gen.return_value = "MODS-12345-EKFIFSO-67890"

    mod_man.build_modifier()
    test_mod = mod_man.Modifier("Test_mod", adds={"energy": 50})
    assert test_mod.export() in mod_man.MODIFIER_DATA["data"].values()
    m_db_update.assert_called_with(mod_man.MODIFIER_DATA)

    # Retry Add
    m_str_val.side_effect = ["Test_mod"]
    m_list_select.side_effect = ["energy", "Base Change", "health", "Base Change"]
    m_num_range.side_effect = [50, 60]
    m_yn_val.side_effect = [False, True, True, False]
    m_id_gen.return_value = "MODS-12345-EKFIFSO-67890"

    mod_man.build_modifier()
    test_mod = mod_man.Modifier("Test_mod", adds={"health": 60})
    assert test_mod.export() in mod_man.MODIFIER_DATA["data"].values()
    m_db_update.assert_called_with(mod_man.MODIFIER_DATA)


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.utils.data_mgmt.update_data")
@patch("funclg.managers.modifier_manager.yes_no_validation")
@patch("funclg.managers.modifier_manager.number_range_validation")
@patch("funclg.managers.modifier_manager.string_validation")
@patch("funclg.managers.modifier_manager.list_choice_selection")
def test_modifier_manager_build_modifier_mult_mod(
    m_list_select, m_str_val, m_num_range, m_yn_val, m_db_update, m_id_gen
):
    m_id_gen.return_value = "MODS-12345-EKFIFSO-67890"
    
    # Test new build method (no name, no from method)
    m_str_val.side_effect = ["Test_mod"]
    m_list_select.side_effect = ["energy", "Percentage Change"]
    m_num_range.side_effect = [50]
    m_yn_val.side_effect = [True, False]

    mod_man.build_modifier()
    test_mod = mod_man.Modifier("Test_mod", mults={"energy": 0.5})
    assert test_mod.export() in mod_man.MODIFIER_DATA["data"].values()
    m_db_update.assert_called_with(mod_man.MODIFIER_DATA)

    # Retry Mult
    m_str_val.side_effect = ["Test_mod"]
    m_list_select.side_effect = ["energy", "Percentage Change", "health", "Percentage Change"]
    m_num_range.side_effect = [50, 60]
    m_yn_val.side_effect = [False, True, True, False]

    mod_man.build_modifier()
    test_mod = mod_man.Modifier("Test_mod", mults={"health": 0.6})
    assert test_mod.export() in mod_man.MODIFIER_DATA["data"].values()
    m_db_update.assert_called_with(mod_man.MODIFIER_DATA)

@patch("funclg.utils.data_mgmt.update_data")
@patch("funclg.managers.modifier_manager.yes_no_validation")
@patch("funclg.managers.modifier_manager.number_range_validation")
@patch("funclg.managers.modifier_manager.list_choice_selection")
def test_modifier_manager_build_modifier_return_mod(m_list_select, m_num_range, m_yn_val, m_db):
    # Add and Mult Mod
    # Multi Adds and Mults
    # Tests return value
    m_list_select.side_effect = [
        "energy",
        "Base Change",
        "attack",
        "Base Change",
        "health",
        "Percentage Change",
        "defense",
        "Percentage Change",
    ]
    m_num_range.side_effect = [50, 250, 60, 75]
    m_yn_val.side_effect = [True, True, True, True, True, True, True, False]

    return_val = mod_man.build_modifier("Test_mod")
    test_mod = mod_man.Modifier(
        "Test_mod", adds={"energy": 50, "attack": 250}, mults={"health": 0.6, "defense": 0.75}
    )
    assert return_val.name == test_mod.name
    assert return_val.get_mods() == test_mod.get_mods()
    assert m_db.called_once