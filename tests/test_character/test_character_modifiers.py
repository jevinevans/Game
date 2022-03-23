"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the modifier classes.
Last Update: 3.23.2022
"""

import unittest
from random import randint, random

from FUNCLG.character.modifiers import Modifier


def adds_1():
    return {"attack": 43, "defense": -20}


def adds_2():
    return {"attack": -34, "energy": 20, "error": -32}


def mults_1():
    return {"health": 0.33, "energy": -0.6}


def mults_2():
    return {"health": -0.10, "defense": 0.4, "error": 23}


class ModifierTest(unittest.TestCase):
    def test_modifier_init(self):

        # Create No Mod
        mod_1 = Modifier(name="Test 1")
        self.assertEqual(mod_1.adds, {})
        self.assertEqual(mod_1.mults, {})

        # Create Full Mods
        mod_2 = Modifier(name="Test 2", adds=adds_1(), mults=mults_1())
        self.assertEqual(mod_2.adds, adds_1())
        self.assertEqual(mod_2.mults, mults_1())

        # Partial Incorrect Create
        mod_3 = Modifier(name="Test 3", adds=adds_2())
        self.assertNotIn("error", mod_3.adds)

    def test_modifier_add_mods(self):
        # Correct Add
        mod_4 = Modifier(name="Test 4")
        mod_4.add_mods("adds", adds_1())
        self.assertEqual(mod_4.adds, adds_1())

        # Incorrect Type
        mod_4.add_mods("error", adds_2())
        self.assertEqual(mod_4.mults, {})
        self.assertEqual(mod_4.adds, adds_1())

    def test_modifier_remove_mod(self):
        # Remove no mods
        mod_5 = Modifier("Test 5", mults=mults_1())

        # Remove error type
        mod_5.remove_mod("error", "attack")
        # Remove error stat
        mod_5.remove_mod("mults", "error")
        self.assertEqual(mod_5.mults, mults_1())

        # Successful Remove
        mod_5.remove_mod("mults", "energy")
        answer = mults_1()
        del answer["energy"]
        self.assertEqual(mod_5.mults, answer)

    def test_modifier_get_mods(self):
        # Parital Get w/ empty set
        mod_6 = Modifier(name="Test 6", adds=adds_1())
        self.assertEqual(mod_6.get_mods(), {"mults": {}, "adds": adds_1()})

        # Full Get
        mod_7 = Modifier(name="Test 7", adds=adds_1(), mults=mults_1())
        self.assertEqual(mod_7.get_mods(), {"mults": mults_1(), "adds": adds_1()})

    def test_modifier_export(self):
        # Testing of null value
        mod_8 = Modifier(name="Test 8", adds=adds_1(), mults=mults_1())
        self.assertIsNotNone(mod_8.export())
        self.assertIsInstance(mod_8.export(), dict)

    def test_modifier_output_examples(self):
        mod_9 = Modifier(name="Test 9", adds=adds_1(), mults=mults_1())
        print(f"\n{'Modifier Example Output'.center(80, '-')}")
        print(f"\n__str__ Output:\n{mod_9}")
        print(f"\ndetails Output:\n{mod_9.details()}")
        print(f"\nexport Output:\n{mod_9.export()}")
        print(f"\n{'Done'.center(80, '-')}")
