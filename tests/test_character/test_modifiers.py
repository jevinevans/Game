"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the modifier classes.
Last Update: 3.23.2022
"""
import pytest

from funclg.character.modifiers import Modifier


# Modifier Fixtures
@pytest.fixture
def base_mods():
    return {
        "valid": {"attack": 43, "defense": -20},
        "invalid": {
            "attack": -34,
            "error": -32,
            "energy": 20,
        },
    }


@pytest.fixture
def percentage_mods():
    return {
        "valid": {"health": 0.33, "energy": -0.6},
        "invalid": {
            "health": -0.10,
            "error": 23,
            "defense": 0.4,
        },
    }


@pytest.fixture
def new_add_modifier():
    return {"health": 34, "defense": 60}


@pytest.fixture
def new_mult_modifier():
    return {"energy": 0.56, "attack": 0.25}


@pytest.fixture
def modifier_get_expectation(base_mods, percentage_mods):
    return {"base": base_mods["valid"], "percentage": percentage_mods["valid"]}


@pytest.fixture
def modifier_export_expectation(base_mods, percentage_mods):
    return {
        "base": base_mods["valid"],
        "percentage": percentage_mods["valid"],
    }


@pytest.fixture
def modifier_str_expectation():
    return "Attack +43, Defense -20, Health +33.0%, Energy -60.0%"


@pytest.fixture
def modifier_details_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base = f"""
{' '*(indent)}Attack: +43
{' '*(indent)}Defense: -20
{' '*(indent)}Health: +33.0%
{' '*(indent)}Energy: -60.0%"""
        expectations.append(base)
    return expectations


def test_modifier_init(base_mods, percentage_mods):
    # Test Empty Modifier
    mod_1 = Modifier("T1")

    assert mod_1.name == "T1"
    assert not mod_1.base
    assert not mod_1.percentage

    # Test Full Modifier (Valid)
    mod_2 = Modifier("T2", base=base_mods["valid"], percentage=percentage_mods["valid"])
    assert mod_2.base == base_mods["valid"]
    assert mod_2.percentage == percentage_mods["valid"]


def test_modifier_verify_stat(base_mods, percentage_mods):
    # Test Invalid Stat Type (Invalid)
    valid_base_mods = base_mods["invalid"].copy()
    valid_percentage_mods = percentage_mods["invalid"].copy()

    del valid_base_mods["error"]
    del valid_percentage_mods["error"]

    mod_1 = Modifier("T1", base=base_mods["invalid"], percentage=percentage_mods["invalid"])
    assert mod_1.base == valid_base_mods
    assert mod_1.percentage == valid_percentage_mods


def test_modifier_str(base_mods, percentage_mods, modifier_str_expectation):
    mod_1 = Modifier("T1", base_mods["valid"], percentage_mods["valid"])
    assert mod_1.__str__() == modifier_str_expectation


def test_modifier_details(base_mods, percentage_mods, modifier_details_expectation):
    mod_1 = Modifier("T1", base_mods["valid"], percentage_mods["valid"])

    # Test Indention from 0,2,4...10
    for index, indent in enumerate((list(range(0, 11, 2)))):
        assert mod_1.details(indent=indent) == modifier_details_expectation[index]


def test_modifier_add_modifier(new_add_modifier, new_mult_modifier):
    mod_1 = Modifier("T1")
    mod_1.add_mod("base", new_add_modifier)
    mod_1.add_mod("percentage", new_mult_modifier)

    assert mod_1.base == new_add_modifier
    assert mod_1.percentage == new_mult_modifier
    assert len(mod_1.get_mods()) == 2
    assert len(mod_1.base) == 2
    assert len(mod_1.percentage) == 2

    # Test invalid mod type
    mod_1.add_mod("error_type", {})
    assert len(mod_1.get_mods()) == 2
    mod_1.add_mod("base", {})
    assert len(mod_1.get_mods()) == 2


def test_modifier_remove_modifier(base_mods, percentage_mods):
    valid_base = base_mods["valid"].copy()
    valid_percentage = percentage_mods["valid"].copy()
    del valid_base["defense"]
    del valid_percentage["energy"]
    mod_1 = Modifier("T1", base_mods["valid"], percentage_mods["valid"])
    mod_1.remove_mod("base", "defense")

    # Test Invalid stat name
    mod_1.remove_mod("percentage", "energyt")
    mod_1.remove_mod("percentage", "energy")
    mod_1.remove_mod("error_test", "")

    assert mod_1.base == valid_base
    assert mod_1.percentage == valid_percentage


def test_modifier_get_mods(base_mods, percentage_mods, modifier_get_expectation):
    mod_1 = Modifier("T1", base_mods["valid"], percentage_mods["valid"])
    assert mod_1.get_mods() == modifier_get_expectation


def test_modifier_friendly_read_branching():
    mod_1 = Modifier("Friendly Test")
    assert not mod_1._friendly_read()


def test_modifier_export(base_mods, percentage_mods):
    mod_1 = Modifier("T1", base_mods["valid"], percentage_mods["valid"])
    assert mod_1.export() == {"base": base_mods["valid"], "percentage": percentage_mods["valid"]}


def test_modifier_level_up(base_mods, percentage_mods):
    mod_1 = Modifier("L1", base=base_mods["valid"], percentage=percentage_mods["valid"])
    mod_lvl = Modifier("L2", base=base_mods["valid"], percentage=percentage_mods["valid"])

    mod_lvl.level_up()

    for add in mod_1.base:
        assert abs(mod_1.base[add] - mod_lvl.base[add]) == 1
    for mult in mod_1.percentage:
        assert round(abs(mod_1.percentage[mult] - mod_lvl.percentage[mult]), 2) == 0.01

    mod_lvl.level_up()
    mod_lvl.level_up()
    mod_lvl.level_up()
    mod_lvl.level_up()

    for add in mod_1.base:
        assert abs(mod_1.base[add] - mod_lvl.base[add]) == 5
    for mult in mod_1.percentage:
        assert round(abs(mod_1.percentage[mult] - mod_lvl.percentage[mult]), 2) == 0.05
