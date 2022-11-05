from unittest.mock import patch

import pytest

import funclg.managers.modifier_manager as mod_man
from funclg.utils.types import ABILITY_TYPES


@patch("funclg.managers.modifier_manager.yes_no_validation")
@patch("funclg.managers.modifier_manager.number_range_validation")
@patch("funclg.managers.modifier_manager.list_choice_selection")
def test_modifier_manager_build_modifier_return_mod(m_list_select, m_num_range, m_yn_val):
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
    m_yn_val.side_effect = [True, True, True, True, True, True, True, False, True]

    return_val = mod_man.build_modifier("Test_mod")
    test_mod = mod_man.Modifier(
        "Test_mod", adds={"energy": 50, "attack": 250}, mults={"health": 0.6, "defense": 0.75}
    )
    assert return_val.get_mods() == test_mod.get_mods()

    m_list_select.side_effect = [
        "energy",
        "Base Change",
    ]
    m_num_range.side_effect = [50]
    m_yn_val.side_effect = [False, False, False]

    return_val = mod_man.build_modifier("Test_mod")
    assert return_val == None

    m_list_select.side_effect = ["attack", "Percentage Change"]
    m_num_range.side_effect = [50]
    m_yn_val.side_effect = [False, False, False]

    return_val = mod_man.build_modifier("Test_mod")
    assert return_val == None


@patch("funclg.managers.modifier_manager._gen_mult_mod")
@patch("funclg.managers.modifier_manager._gen_add_mod")
def test_modifier_manager_generate_modifer_flow(m_add, m_mult):
    # Test no item_type
    # m_rand.side_effect = [3, 60, 1, 30]
    m_add.return_value = {"health": 60}
    m_mult.return_value = {"energy": 0.4}
    mod = mod_man.generate_modifier()

    assert mod == {"adds": {"health": 60}, "mults": {"energy": 0.4}}

    # Test Armor Type
    m_add.return_value = {"health": 32}
    m_mult.return_value = {"defense": 0.45}
    mod = mod_man.generate_modifier("armor")
    assert mod == {"adds": {"health": 32}, "mults": {"defense": 0.45}}

    # Test Weapon Type
    m_add.return_value = {"attack": 474}
    m_mult.return_value = {"energy": 0.9}
    mod = mod_man.generate_modifier("weapon")
    assert mod == {"adds": {"attack": 474}, "mults": {"energy": 0.9}}

    # Test Index Error

    # Test Weapon Type
    m_add.return_value = {"energy": 474}
    m_mult.return_value = {"defense": 0.9}
    mod = mod_man.generate_modifier()
    assert mod == {"adds": {"energy": 474}, "mults": {"defense": 0.9}}


@patch("funclg.managers.modifier_manager.randint")
def test_modifier_manager_generate_modifer_ability(m_rand):

    # Test Ability Add
    m_rand.side_effect = [30]

    mod = mod_man.generate_modifier("ability", ABILITY_TYPES["Physical"])
    assert mod == {"adds": {"health": 30}, "mults": {}}

    # Test Ability Mult
    m_rand.side_effect = [60]

    mod = mod_man.generate_modifier("ability", ABILITY_TYPES["Restore"])
    assert mod == {"adds": {}, "mults": {"health": 0.6}}

    # Test Ability Add Random
    m_rand.side_effect = [1, 30]

    mod = mod_man.generate_modifier("ability", ABILITY_TYPES["Physical"], True)
    assert mod == {"adds": {"defense": 30}, "mults": {}}

    # Test Ability Mult Random
    m_rand.side_effect = [2, 60]

    mod = mod_man.generate_modifier("ability", ABILITY_TYPES["Restore"], True)
    assert mod == {"adds": {}, "mults": {"energy": 0.6}}
