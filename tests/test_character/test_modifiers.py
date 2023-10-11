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
def add_mods():
    return {
        "valid": {"attack": 43, "defense": -20},
        "invalid": {
            "attack": -34,
            "error": -32,
            "energy": 20,
        },
    }


@pytest.fixture
def mult_mods():
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
def modifier_get_expectation(add_mods, mult_mods):
    return {"adds": add_mods["valid"], "mults": mult_mods["valid"]}


@pytest.fixture
def modifier_export_expectation(add_mods, mult_mods):
    return {
        "adds": add_mods["valid"],
        "mults": mult_mods["valid"],
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


def test_modifier_init(add_mods, mult_mods):
    # Test Empty Modifier
    mod_1 = Modifier("T1")

    assert mod_1.name == "T1"
    assert not mod_1.adds
    assert not mod_1.mults

    # Test Full Modifier (Valid)
    mod_2 = Modifier("T2", adds=add_mods["valid"], mults=mult_mods["valid"])
    assert mod_2.adds == add_mods["valid"]
    assert mod_2.mults == mult_mods["valid"]


def test_modifier_verify_stat(add_mods, mult_mods):
    # Test Invalid Stat Type (Invalid)
    valid_add_mods = add_mods["invalid"].copy()
    valid_mult_mods = mult_mods["invalid"].copy()

    del valid_add_mods["error"]
    del valid_mult_mods["error"]

    mod_1 = Modifier("T1", adds=add_mods["invalid"], mults=mult_mods["invalid"])
    assert mod_1.adds == valid_add_mods
    assert mod_1.mults == valid_mult_mods


def test_modifier_str(add_mods, mult_mods, modifier_str_expectation):
    mod_1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert mod_1.__str__() == modifier_str_expectation


def test_modifier_details(add_mods, mult_mods, modifier_details_expectation):
    mod_1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])

    # Test Indention from 0,2,4...10
    for index, indent in enumerate((list(range(0, 11, 2)))):
        assert mod_1.details(indent=indent) == modifier_details_expectation[index]


def test_modifier_add_modifier(new_add_modifier, new_mult_modifier):
    mod_1 = Modifier("T1")
    mod_1.add_mod("adds", new_add_modifier)
    mod_1.add_mod("mults", new_mult_modifier)

    assert mod_1.adds == new_add_modifier
    assert mod_1.mults == new_mult_modifier
    assert len(mod_1.get_mods()) == 2
    assert len(mod_1.adds) == 2
    assert len(mod_1.mults) == 2

    # Test invalid mod type
    mod_1.add_mod("error_type", {})
    assert len(mod_1.get_mods()) == 2
    mod_1.add_mod("adds", {})
    assert len(mod_1.get_mods()) == 2


def test_modifier_remove_modifier(add_mods, mult_mods):
    valid_adds = add_mods["valid"].copy()
    valid_mults = mult_mods["valid"].copy()
    del valid_adds["defense"]
    del valid_mults["energy"]
    mod_1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    mod_1.remove_mod("adds", "defense")

    # Test Invalid stat name
    mod_1.remove_mod("mults", "energyt")
    mod_1.remove_mod("mults", "energy")
    mod_1.remove_mod("error_test", "")

    assert mod_1.adds == valid_adds
    assert mod_1.mults == valid_mults


def test_modifier_get_mods(add_mods, mult_mods, modifier_get_expectation):
    mod_1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert mod_1.get_mods() == modifier_get_expectation


def test_modifier_friendly_read_branching():
    mod_1 = Modifier("Friendly Test")
    assert not mod_1._friendly_read()


def test_modifier_export(add_mods, mult_mods):
    mod_1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert mod_1.export() == {"adds": add_mods["valid"], "mults": mult_mods["valid"]}


def test_modifier_level_up(add_mods, mult_mods):
    mod_1 = Modifier("L1", adds=add_mods["valid"], mults=mult_mods["valid"])
    mod_lvl = Modifier("L2", adds=add_mods["valid"], mults=mult_mods["valid"])

    mod_lvl.level_up()

    for add in mod_1.adds:
        assert abs(mod_1.adds[add] - mod_lvl.adds[add]) == 1
    for mult in mod_1.mults:
        assert round(abs(mod_1.mults[mult] - mod_lvl.mults[mult]), 2) == 0.01

    mod_lvl.level_up()
    mod_lvl.level_up()
    mod_lvl.level_up()
    mod_lvl.level_up()

    for add in mod_1.adds:
        assert abs(mod_1.adds[add] - mod_lvl.adds[add]) == 5
    for mult in mod_1.mults:
        assert round(abs(mod_1.mults[mult] - mod_lvl.mults[mult]), 2) == 0.05
