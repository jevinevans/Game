from unittest.mock import patch

import pytest

import funclg.managers as man_build


@patch("funclg.managers.npc_manager.NPCManager.load_data")
@patch("funclg.managers.roles_manager.RolesManager.load_data")
@patch("funclg.managers.game_manager.GameManager.load_data")
@patch("funclg.managers.equipment_manager.EquipmentManager.load_data")
@patch("funclg.managers.character_manager.CharacterManager.load_data")
@patch("funclg.managers.abilities_manager.AbilitiesManager.load_data")
def test_manager_load_data(m_ability, m_char, m_equip, m_game, m_role, m_npc):
    man_build.load_data()

    assert m_ability.called
    assert m_char.called
    assert m_equip.called
    assert m_game.called
    assert m_role.called
    assert m_npc.called


@patch("funclg.managers.npc_manager.NPCManager.export_data")
@patch("funclg.managers.roles_manager.RolesManager.export_data")
@patch("funclg.managers.game_manager.GameManager.export_data")
@patch("funclg.managers.equipment_manager.EquipmentManager.export_data")
@patch("funclg.managers.character_manager.CharacterManager.export_data")
@patch("funclg.managers.abilities_manager.AbilitiesManager.export_data")
def test_manager_save_data(m_ability, m_char, m_equip, m_game,  m_role, m_npc):
    man_build.save_data()

    assert m_ability.called
    assert m_char.called
    assert m_equip.called
    assert m_game.called
    assert m_role.called
    assert m_npc.called



def test_manager_build_game_menu():
    t_game_menu = man_build.build_game_menu()

    assert t_game_menu.name == "Game Settings"

    sub_menus = ["Manage Game Settings", "Manage NPCs"]
    for sub_menu in sub_menus:
        assert sub_menu in t_game_menu.menu_items
    assert len(t_game_menu.menu_items) == 2
    assert t_game_menu.has_return


def test_manager_build_character_manager():
    t_char_menu = man_build.build_character_menu()

    assert t_char_menu.name == "Character Settings"
    assert "Manage Characters" in t_char_menu.menu_items
    assert "Manage Equipment" in t_char_menu.menu_items
    assert "Manage Roles" in t_char_menu.menu_items
    assert "Manage Abilities" in t_char_menu.menu_items
    assert len(t_char_menu.menu_items) == 4
    assert t_char_menu.has_return



def test_manager_build_manager_menu():
    t_man_menu = man_build.build_manager_menu()

    assert t_man_menu.name == "Settings"
    assert "Game Settings" in t_man_menu.menu_items
    assert "Character Settings" in t_man_menu.menu_items
    assert len(t_man_menu.menu_items) == 2
    assert t_man_menu.has_return
