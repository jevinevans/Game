from unittest.mock import patch

import pytest

import funclg.managers as man_build


@patch("funclg.managers.role_man.load_data")
@patch("funclg.managers.level_man.load_data")
@patch("funclg.managers.game_man.load_data")
@patch("funclg.managers.equip_man.load_data")
@patch("funclg.managers.char_man.load_data")
@patch("funclg.managers.ability_man.load_data")
def test_manager_load_data(m_ability, m_char, m_equip, m_game, m_level, m_role):
    man_build.load_data()

    assert m_ability.called
    assert m_char.called
    assert m_equip.called
    assert m_game.called
    assert m_level.called
    assert m_role.called


@patch("funclg.managers.role_man.export_data")
@patch("funclg.managers.level_man.export_data")
@patch("funclg.managers.game_man.export_data")
@patch("funclg.managers.equip_man.export_data")
@patch("funclg.managers.char_man.export_data")
@patch("funclg.managers.ability_man.export_data")
def test_manager_save_data(m_ability, m_char, m_equip, m_game, m_level, m_role):
    man_build.save_data()

    assert m_ability.called
    assert m_char.called
    assert m_equip.called
    assert m_game.called
    assert m_level.called
    assert m_role.called


@patch("funclg.managers.level_man")
@patch("funclg.managers.game_man")
def test_manager_build_game_menu(m_game, m_level):
    t_game_menu = man_build.build_game_menu()

    assert t_game_menu.name == "Game Settings"
    assert "Manage Game Settings" in t_game_menu.menu_items
    assert "Levels Manager" in t_game_menu.menu_items
    assert len(t_game_menu.menu_items) == 2
    assert t_game_menu.has_return


@patch("funclg.managers.role_man")
@patch("funclg.managers.equip_man")
@patch("funclg.managers.char_man")
@patch("funclg.managers.ability_man")
def test_manager_build_character_manager(m_ability, m_char, m_equip, m_role):
    t_char_menu = man_build.build_character_menu()

    assert t_char_menu.name == "Character Settings"
    assert "Manage Characters" in t_char_menu.menu_items
    assert "Manage Equipment" in t_char_menu.menu_items
    assert "Manage Roles" in t_char_menu.menu_items
    assert "Manage Abilities" in t_char_menu.menu_items
    assert len(t_char_menu.menu_items) == 4
    assert t_char_menu.has_return


@patch("funclg.managers.role_man")
@patch("funclg.managers.level_man")
@patch("funclg.managers.game_man")
@patch("funclg.managers.equip_man")
@patch("funclg.managers.char_man")
@patch("funclg.managers.ability_man")
def test_manager_build_manager_menu(m_ability, m_char, m_equip, m_game, m_level, m_role):
    t_man_menu = man_build.build_manager_menu()

    assert t_man_menu.name == "Settings"
    assert "Game Settings" in t_man_menu.menu_items
    assert "Character Settings" in t_man_menu.menu_items
    assert len(t_man_menu.menu_items) == 2
    assert t_man_menu.has_return
