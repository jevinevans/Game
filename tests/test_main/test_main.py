from unittest.mock import patch

import pytest

import funclg.managers
from funclg.__main__ import *
from funclg.utils.menu_funcs import Menu


@patch("funclg.__main__.save_exit")
@patch("funclg.managers.build_manager_menu")
def test_build_main_menu(m_build_man, m_save_exit):
    menu = build_main_menu()
    assert isinstance(menu, Menu)
    assert len(menu.menu_items) == 3
    assert "Play Game" in menu.menu_items
    assert "Exit" in menu.menu_items
    assert menu.menu_items["Play Game"] == None
    assert menu.menu_items["Exit"] == m_save_exit
    assert menu.menu_items["Settings"] == m_build_man()


# @patch('builtins.input')
# def test_main_run_play_success(m_input):
#     # TODO This is how to test the main menu.
#     m_input.side_effect = ["1"]

#     assert main() == None

# @patch("funclg.utils.input_validation.choice_validation")
# @patch("sys.exit")
# @patch("builtins.print")
# @patch('builtins.input')
# def test_main_run_play_success(m_input, m_print, m_exit, m_choice):
#     # TODO This is how to test the main menu.
#     m_input.side_effect = ["3", "3"]

#     main
#     assert m_print.called_with("Saving and closing")
#     assert m_exit.called
