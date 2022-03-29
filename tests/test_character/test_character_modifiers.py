"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the modifier classes.
Last Update: 3.23.2022
"""
import enum
import pytest
from unittest import mock
from FUNCLG.character.modifiers import Modifier
from .character_fixtures import add_mods, modifier_str_expectation, mult_mods

def adds_1():
    return {"attack": 43, "defense": -20}


def adds_2():
    return {"attack": -34, "energy": 20, "error": -32}


def mults_1():
    return {"health": 0.33, "energy": -0.6}


def mults_2():
    return {"health": -0.10, "defense": 0.4, "error": 23}


def test_modifier_init(add_mods, mult_mods):
    # Test Empty Modifier
    t1 = Modifier(name="Mod 1 Test")

    assert t1.adds == {}
    assert t1.mults == {}
    assert t1.name == "Mod 1 Test"

    # Test Full Modifier (Valid)
    t2 = Modifier(name="Mod Test 2", adds=add_mods["valid"], mults=mult_mods['valid'])
    assert t2.name == "Mod Test 2"
    assert t2.adds == add_mods["valid"]
    assert t2.mults == mult_mods["valid"]

def test_modifier_verify_stat(add_mods, mult_mods):
    # Test Invalid Stat Type (Invalid)
    valid_add_mods = add_mods['invalid'].copy()
    valid_mult_mods = mult_mods['invalid'].copy()

    del valid_add_mods['error']
    del valid_mult_mods['error']

    t1 = Modifier(name="Invalid Test", adds=add_mods['invalid'], mults=mult_mods['invalid'])
    assert t1.name == "Invalid Test"
    assert t1.adds == valid_add_mods
    assert t1.mults == valid_mult_mods

def test_modifier_str(add_mods, mult_mods, modifier_str_expectation):
    t1 = Modifier("Output Test", add_mods['valid'], mult_mods['valid'])
    assert t1.__str__() == modifier_str_expectation[0]

def test_modifier_details(add_mods, mult_mods, modifier_str_expectation):
    t1 = Modifier("Output Test", add_mods['valid'], mult_mods['valid'])
    
    # Test Indention from 0,2,4...10
    for index, indent in enumerate([x for x in range(0, 11, 2)]):
        assert t1.details(indent=indent) == modifier_str_expectation[index]

def test_modifier_a
#     def test_modifier_add_mods(self):
#         # Correct Add
#         mod_4 = Modifier(name="Test 4")
#         mod_4.add_mods("adds", adds_1())
#         self.assertEqual(mod_4.adds, adds_1())

#         # Incorrect Type
#         mod_4.add_mods("error", adds_2())
#         self.assertEqual(mod_4.mults, {})
#         self.assertEqual(mod_4.adds, adds_1())

#     def test_modifier_remove_mod(self):
#         # Remove no mods
#         mod_5 = Modifier("Test 5", mults=mults_1())

#         # Remove error type
#         mod_5.remove_mod("error", "attack")
#         # Remove error stat
#         mod_5.remove_mod("mults", "error")
#         self.assertEqual(mod_5.mults, mults_1())

#         # Successful Remove
#         mod_5.remove_mod("mults", "energy")
#         answer = mults_1()
#         del answer["energy"]
#         self.assertEqual(mod_5.mults, answer)

#     def test_modifier_get_mods(self):
#         # Parital Get w/ empty set
#         mod_6 = Modifier(name="Test 6", adds=adds_1())
#         self.assertEqual(mod_6.get_mods(), {"mults": {}, "adds": adds_1()})

#         # Full Get
#         mod_7 = Modifier(name="Test 7", adds=adds_1(), mults=mults_1())
#         self.assertEqual(mod_7.get_mods(), {"mults": mults_1(), "adds": adds_1()})

#     def test_modifier_export(self):
#         # Testing of null value
#         mod_8 = Modifier(name="Test 8", adds=adds_1(), mults=mults_1())
#         self.assertIsNotNone(mod_8.export())
#         self.assertIsInstance(mod_8.export(), dict)

#     def test_modifier_output_examples(self):
#         mod_9 = Modifier(name="Test 9", adds=adds_1(), mults=mults_1())
#         print(f"\n{'Modifier Example Output'.center(80, '-')}")
#         print(f"\n__str__ Output:\n{mod_9}")
#         print(f"\ndetails Output:\n{mod_9.details()}")
#         print(f"\nexport Output:\n{mod_9.export()}")
#         print(f"\n{'Done'.center(80, '-')}")
