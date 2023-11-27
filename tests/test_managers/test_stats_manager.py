"""
Description: The is a unit test for the Stats and modifier manager class.
Developer: Jevin Evans
Date: 11.12.2022
"""

from unittest.mock import patch

import funclg.managers.stats_manager as stats_man
from funclg.utils.types import ABILITY_TYPES

# import pytest


@patch("funclg.managers.stats_manager.confirmation")
@patch("funclg.managers.stats_manager.number_range_validation")
@patch("funclg.managers.stats_manager.selection_validation")
def test_modifier_manager_build_modifier_return_mod(m_sel, m_num_range, m_confirm):
    # Add and Mult Mod
    # Multi base and percentage
    # Tests return value
    m_sel.side_effect = [
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
    m_confirm.side_effect = [True, True, True, True, True, True, True, False, True]

    return_val = stats_man.build_modifier("Test_mod")
    test_mod = stats_man.Modifier(
        "Test_mod", base={"energy": 50, "attack": 250}, percentage={"health": 0.6, "defense": 0.75}
    )
    assert return_val.get_mods() == test_mod.get_mods()

    m_sel.side_effect = [
        "energy",
        "Base Change",
    ]
    m_num_range.side_effect = [50]
    m_confirm.side_effect = [False, False, False]

    return_val = stats_man.build_modifier("Test_mod")
    assert return_val is None

    m_sel.side_effect = ["attack", "Percentage Change"]
    m_num_range.side_effect = [50]
    m_confirm.side_effect = [False, False, False]

    return_val = stats_man.build_modifier("Test_mod")
    assert return_val is None


@patch("funclg.managers.stats_manager._gen_percentage_mod")
@patch("funclg.managers.stats_manager._gen_base_mod")
def test_modifier_manager_generate_modifer_flow(m_base, m_percentage):
    # Test no item_type
    # m_rand.side_effect = [3, 60, 1, 30]
    m_base.return_value = {"health": 60}
    m_percentage.return_value = {"energy": 0.4}
    mod = stats_man.generate_modifier()

    assert mod == {"base": {"health": 60}, "percentage": {"energy": 0.4}}

    # Test Armor Type
    m_base.return_value = {"health": 32}
    m_percentage.return_value = {"defense": 0.45}
    mod = stats_man.generate_modifier("armor")
    assert mod == {"base": {"health": 32}, "percentage": {"defense": 0.45}}

    # Test Weapon Type
    m_base.return_value = {"attack": 474}
    m_percentage.return_value = {"energy": 0.9}
    mod = stats_man.generate_modifier("weapon")
    assert mod == {"base": {"attack": 474}, "percentage": {"energy": 0.9}}

    # Test Index Error

    # Test Weapon Type
    m_base.return_value = {"energy": 474}
    m_percentage.return_value = {"defense": 0.9}
    mod = stats_man.generate_modifier()
    assert mod == {"base": {"energy": 474}, "percentage": {"defense": 0.9}}


@patch("funclg.managers.stats_manager.randint")
def test_modifier_manager_generate_modifer_ability(m_rand):
    # Test Ability Add
    m_rand.side_effect = [30]

    mod = stats_man.generate_modifier("ability", ABILITY_TYPES["Physical"])
    assert mod == {"base": {"health": 30}, "percentage": {}}

    # Test Ability Mult
    m_rand.side_effect = [60]

    mod = stats_man.generate_modifier("ability", ABILITY_TYPES["Restore"])
    assert mod == {"base": {}, "percentage": {"health": 0.6}}

    # Test Ability Add Random
    m_rand.side_effect = [1, 30]

    mod = stats_man.generate_modifier("ability", ABILITY_TYPES["Physical"], True)
    assert mod == {"base": {"defense": 30}, "percentage": {}}

    # Test Ability Mult Random
    m_rand.side_effect = [2, 60]

    mod = stats_man.generate_modifier("ability", ABILITY_TYPES["Restore"], True)
    assert mod == {"base": {}, "percentage": {"energy": 0.6}}
