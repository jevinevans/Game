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
    assert test_menu.menu_items == []
    assert test_menu.has_return == True
    assert test_menu.return_val == 1

    # Menu with no return
    no_ret_menu = Menu(
        name="No Return Menu", description="Testing Menu with no return", has_return=False
    )
    assert no_ret_menu.menu_items == []
    assert no_ret_menu.has_return == False
    assert no_ret_menu.return_val == 0


def test_menu_add_item():
    test_menu = Menu(name="Test Item Menu", description="Testing Menu with Items")
    test_menu.add_item("Success", success_test)
    test_menu.add_item("Failure", failure_test)

    assert len(test_menu.menu_items) == 2
    assert "Success" == test_menu.menu_items[0]["value"]()
    assert "Failure" == test_menu.menu_items[1]["value"]()
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
    assert "Success" == test_menu.menu_items[0]["value"]()
    assert "Failure" == test_menu.menu_items[1]["value"]()
    assert test_menu.has_return


@patch("funclg.utils.menu_funcs.choice_validation")
@patch("builtins.print")
def test_menu_print_menu_with_return(m_print, m_choice_val):
    test_menu = Menu.build_menu(
        "Test Menu",
        "This is a test menu",
        [{"title": "Success", "value": success_test}, {"title": "Failure", "value": failure_test}],
    )
    test_calls = [test_menu.name, "\t" + test_menu.description]
    test_calls.extend(
        [
            f"{index}. --- {value['title']}"
            for index, value in enumerate(test_menu.menu_items, start=1)
        ]
    )
    test_calls += ["3. --- Go Back"]
    test_calls *= 2

    m_choice_val.side_effect = [1, 3]

    test_menu.print_menu()

    m_print.assert_has_calls([call(x) for x in test_calls])


@patch("funclg.utils.menu_funcs.choice_validation")
@patch("builtins.print")
def test_menu_print_menu_submenu(m_print, m_choice_val):
    def ret_func():
        return

    sub_menu = Menu.build_menu(
        "Sub Menu", "", [{"title": "Return", "value": ret_func}], has_return=False
    )
    test_menu = Menu.build_menu(
        "Test Menu", "This is a test menu", [{"title": "Sub Menu", "value": sub_menu}]
    )
    test_calls = [test_menu.name, "\t" + test_menu.description]
    test_calls += ["1. --- Sub Menu"]
    test_calls += ["2. --- Go Back"]
    test_calls += [sub_menu.name]
    test_calls += ["1. --- Return"]
    test_calls += [test_menu.name, "\t" + test_menu.description]
    test_calls += ["1. --- Sub Menu"]
    test_calls += ["2. --- Go Back"]

    m_choice_val.side_effect = [1, 0, 2]

    test_menu.print_menu()

    m_print.assert_has_calls([call(x) for x in test_calls])
