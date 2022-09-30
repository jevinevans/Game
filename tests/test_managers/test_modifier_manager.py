from unittest.mock import patch

import pytest

import funclg.managers.modifier_manager as mod_man


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
    assert return_val.name == test_mod.name
    assert return_val.get_mods() == test_mod.get_mods()


@patch("funclg.managers.modifier_manager.randint")
def test_modifier_manager_generate_modifer(m_rand):
    # Test no item_type
    m_rand.side_effect = [3, 60, 1, 30]
    mod = mod_man.generate_modifier()

    assert mod == {"adds": {"defense": 60}, "mults": {"energy": 0.3}}

    # Test Armor Type
    m_rand.side_effect = [0, 32, 0, 45]
    mod = mod_man.generate_modifier("armor")
    assert mod == {"adds": {"health": 32}, "mults": {"defense": 0.45}}

    # Test Weapon Type
    m_rand.side_effect = [1, 474, 0, 90]
    mod = mod_man.generate_modifier("weapon")
    assert mod == {"adds": {"attack": 474}, "mults": {"energy": 0.9}}

    # Test Index Error

    # Test Weapon Type
    m_rand.side_effect = [1, 474, 10, 90]
    mod = mod_man.generate_modifier()
    assert mod == {"adds": {"energy": 474}, "mults": {"defense": 0.9}}
