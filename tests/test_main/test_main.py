from unittest.mock import patch

import pytest

from funclg.__main__ import *
from funclg.utils.menu_funcs import Menu


def test_build_main_menu():
    menu = build_main_menu()
    assert isinstance(menu, Menu)
    assert len(menu.menu_items) == 3
    assert menu.menu_items[0]["name"] == "Play"
    assert menu.menu_items[-1]["name"] == "Exit"


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
