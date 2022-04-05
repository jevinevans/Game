"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the modifier classes.
Last Update: 3.23.2022
"""
import pytest

from FUNCLG.character.modifiers import Modifier

from .fixtures.modifier_fixtures import (
    add_mods,
    modifier_export_expectation,
    modifier_get_expectation,
    modifier_str_expectation,
    mult_mods,
    new_add_modifier,
    new_mult_modifier,
)


def test_modifier_init(add_mods, mult_mods):
    # Test Empty Modifier
    t1 = Modifier(name="Mod 1 Test")

    assert t1.adds == {}
    assert t1.mults == {}
    assert t1.name == "Mod 1 Test"

    # Test Full Modifier (Valid)
    t2 = Modifier(name="Mod Test 2", adds=add_mods["valid"], mults=mult_mods["valid"])
    assert t2.name == "Mod Test 2"
    assert t2.adds == add_mods["valid"]
    assert t2.mults == mult_mods["valid"]


def test_modifier_verify_stat(add_mods, mult_mods):
    # Test Invalid Stat Type (Invalid)
    valid_add_mods = add_mods["invalid"].copy()
    valid_mult_mods = mult_mods["invalid"].copy()

    del valid_add_mods["error"]
    del valid_mult_mods["error"]

    t1 = Modifier(name="Invalid Test", adds=add_mods["invalid"], mults=mult_mods["invalid"])
    assert t1.name == "Invalid Test"
    assert t1.adds == valid_add_mods
    assert t1.mults == valid_mult_mods


def test_modifier_str(add_mods, mult_mods, modifier_str_expectation):
    t1 = Modifier("Output Test", add_mods["valid"], mult_mods["valid"])
    assert t1.__str__() == modifier_str_expectation[0]


def test_modifier_details(add_mods, mult_mods, modifier_str_expectation):
    t1 = Modifier("Output Test", add_mods["valid"], mult_mods["valid"])

    # Test Indention from 0,2,4...10
    for index, indent in enumerate([x for x in range(0, 11, 2)]):
        assert t1.details(indent=indent) == modifier_str_expectation[index]


def test_modifier_add_modifier(new_add_modifier, new_mult_modifier):
    t1 = Modifier(name="Test Add Modifier")
    t1.add_mods("adds", new_add_modifier)
    t1.add_mods("mults", new_mult_modifier)

    assert t1.adds == new_add_modifier
    assert t1.mults == new_mult_modifier


def test_modifier_remove_modifier(add_mods, mult_mods):
    valid_adds = add_mods["valid"].copy()
    valid_mults = mult_mods["valid"].copy()
    del valid_adds["defense"]
    del valid_mults["energy"]
    t1 = Modifier("Test Remove Modifier", add_mods["valid"], mult_mods["valid"])
    t1.remove_mod("adds", "defense")
    # Test Invalid stat name
    t1.remove_mod("mults", "energyt")
    t1.remove_mod("mults", "energy")

    assert t1.adds == valid_adds
    assert t1.mults == valid_mults


def test_modifier_get_mods(add_mods, mult_mods, modifier_get_expectation):
    t1 = Modifier("Test Get Mods", add_mods["valid"], mult_mods["valid"])
    assert t1.get_mods() == modifier_get_expectation


def test_modifier_export(add_mods, mult_mods, modifier_export_expectation):
    t1 = Modifier("Test Export", add_mods["valid"], mult_mods["valid"])
    assert t1.export() == modifier_export_expectation
