from unittest.mock import call, patch

import pytest

from funclg.utils.menu_funcs import Menu


def success_test():
    return "Success"


def failure_test():
    return "Failure"


def test_menu_init():
    # Menu default - with return
    test_menu = Menu(name="Test Menu", description="Testing Menu")
    assert test_menu.menu_items == {}
    assert test_menu.has_return == True

    # Menu with no return
    no_ret_menu = Menu(
        name="No Return Menu", description="Testing Menu with no return", has_return=False
    )
    assert no_ret_menu.menu_items == {}
    assert no_ret_menu.has_return == False


def test_menu_add_item():
    test_menu = Menu(name="Test Item Menu", description="Testing Menu with Items")
    test_menu.add_item("Success", success_test)
    test_menu.add_item("Failure", failure_test)

    assert len(test_menu.menu_items) == 2
    assert "Success" == test_menu.menu_items["Success"]()
    assert "Failure" == test_menu.menu_items["Failure"]()
    assert test_menu.has_return


def test_menu_build_menu():
    test_menu_items = [
        {"title": "Success", "value": success_test},
        {"title": "Failure", "value": failure_test},
    ]

    test_menu = Menu.build_menu(
        name="Test Menu Build", description="Building test menu", menu_items=test_menu_items
    )
    assert isinstance(test_menu, Menu)
    assert len(test_menu.menu_items) == 2
    assert "Success" == test_menu.menu_items["Success"]()
    assert "Failure" == test_menu.menu_items["Failure"]()
    assert test_menu.has_return


@patch("funclg.utils.menu_funcs.selection_validation")
def test_menu_print_menu_with_return(m_sel_val):
    test_menu = Menu.build_menu(
        "Test Menu",
        "This is a test menu",
        [{"title": "Success", "value": success_test}, {"title": "Failure", "value": failure_test}],
    )

    m_sel_val.side_effect = ["Success", "Go Back"]

    test_menu.print_menu()


@patch("funclg.utils.menu_funcs.selection_validation")
def test_menu_print_menu_submenu(m_sel_val):
    sub_menu = Menu.build_menu(
        "Sub Menu", "", [{"title": "Return", "value": None}], has_return=False
    )
    test_menu = Menu.build_menu(
        "Test Menu", "This is a test menu", [{"title": "Sub Menu", "value": sub_menu}]
    )

    m_sel_val.side_effect = ["Sub Menu", "Return", "Go Back"]

    test_menu.print_menu()
