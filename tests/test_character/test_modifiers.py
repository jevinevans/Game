"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the modifier classes.
Last Update: 3.23.2022
"""
# import pytest

from funclg.character.modifiers import Modifier

from .fixtures.modifier_fixtures import (
    add_mods,
    modifier_details_expectation,
    modifier_export_expectation,
    modifier_get_expectation,
    modifier_str_expectation,
    mult_mods,
    new_add_modifier,
    new_mult_modifier,
)


def test_modifier_init(add_mods, mult_mods):
    # Test Empty Modifier
    t1 = Modifier("T1")

    assert t1.name == "T1"
    assert not t1.adds
    assert not t1.mults

    # Test Full Modifier (Valid)
    t2 = Modifier("T2", adds=add_mods["valid"], mults=mult_mods["valid"])
    assert t2.adds == add_mods["valid"]
    assert t2.mults == mult_mods["valid"]


def test_modifier_verify_stat(add_mods, mult_mods):
    # Test Invalid Stat Type (Invalid)
    valid_add_mods = add_mods["invalid"].copy()
    valid_mult_mods = mult_mods["invalid"].copy()

    del valid_add_mods["error"]
    del valid_mult_mods["error"]

    t1 = Modifier("T1", adds=add_mods["invalid"], mults=mult_mods["invalid"])
    assert t1.adds == valid_add_mods
    assert t1.mults == valid_mult_mods


def test_modifier_str(add_mods, mult_mods, modifier_str_expectation):
    t1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert t1.__str__() == modifier_str_expectation


def test_modifier_details(add_mods, mult_mods, modifier_details_expectation):
    t1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])

    # Test Indention from 0,2,4...10
    for index, indent in enumerate([x for x in range(0, 11, 2)]):
        assert t1.details(indent=indent) == modifier_details_expectation[index]


def test_modifier_add_modifier(new_add_modifier, new_mult_modifier):
    t1 = Modifier("T1")
    t1.add_mod("adds", new_add_modifier)
    t1.add_mod("mults", new_mult_modifier)

    assert t1.adds == new_add_modifier
    assert t1.mults == new_mult_modifier
    assert len(t1.get_mods()) == 2
    assert len(t1.adds) == 2
    assert len(t1.mults) == 2

    # Test invalid mod type
    t1.add_mod("error_type", {})
    assert len(t1.get_mods()) == 2
    t1.add_mod("adds", {})
    assert len(t1.get_mods()) == 2


def test_modifier_remove_modifier(add_mods, mult_mods):
    valid_adds = add_mods["valid"].copy()
    valid_mults = mult_mods["valid"].copy()
    del valid_adds["defense"]
    del valid_mults["energy"]
    t1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    t1.remove_mod("adds", "defense")

    # Test Invalid stat name
    t1.remove_mod("mults", "energyt")
    t1.remove_mod("mults", "energy")
    t1.remove_mod("error_test", "")

    assert t1.adds == valid_adds
    assert t1.mults == valid_mults


def test_modifier_get_mods(add_mods, mult_mods, modifier_get_expectation):
    t1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert t1.get_mods() == modifier_get_expectation


def test_modifier_friendly_read_branching():
    t1 = Modifier("Friendly Test")
    assert not t1._friendly_read()


def test_modifier_export(add_mods, mult_mods):
    t1 = Modifier("T1", add_mods["valid"], mult_mods["valid"])
    assert t1.export() == {"adds": add_mods["valid"], "mults": mult_mods["valid"]}
