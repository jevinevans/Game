"""
Programmer: Jevin Evans
Date: 1.8.2022
Description: The is a unit test for the abilties class.
"""

import os
import unittest
from random import randint
from typing import Dict

from FUNCLG.character.abilities import Abilities


class AbilityTest(unittest.TestCase):
    def setup(self) -> Dict[str, Abilities]:
        test_abilities = {}
        test_abilities["Magic"] = Abilities(
            name="Fireball",
            damage_type="Magic",
            effect=randint(1, 50),
            description="A blazing ball of fire",
        )
        test_abilities["Physical"] = Abilities(
            name="Slash",
            damage_type="Physical",
            effect=randint(1, 50),
            description="A slashing strike with a sharp weapon",
        )
        test_abilities["Repair"] = Abilities(
            name="Armor Fix",
            damage_type="Repair",
            effect=randint(1, 50),
            description="Repairs the armor of the user",
        )
        test_abilities["Healing"] = Abilities(
            name="Holy Light",
            damage_type="Healing",
            effect=randint(1, 50),
            description="Heals the user",
        )
        test_abilities["Error"] = Abilities(
            name="Error Test",
            damage_type="error",
            effect=randint(1, 50),
            description="Testing if this will default to None",
        )

        return test_abilities

    def test_abilities_init(self):
        test_abilities = self.setup()
        valid_neg, valid_pos, invalid = (
            test_abilities["Magic"],
            test_abilities["Healing"],
            test_abilities["Error"],
        )
        # Test Valid Negative Effect
        self.assertEqual(valid_neg.name, "Fireball")
        self.assertEqual(valid_neg.damage_type, "Magic")
        self.assertEqual(valid_neg.ability_group, "Damage")
        self.assertIsInstance(valid_neg.effect, int)
        self.assertLessEqual(valid_neg.effect, -1)
        self.assertIsNotNone(valid_neg.description)

        # Test Valid Positive Effect
        self.assertGreaterEqual(valid_pos.effect, 1)

        # Test Invalid
        self.assertEqual(invalid.damage_type, "None")
        self.assertEqual(invalid.ability_group, "None")
        self.assertEqual(invalid.effect, 0)

    def test_abilities_str(self):
        for _, ability in self.setup().items():
            self.assertIsNotNone(ability.__str__())
            self.assertIsInstance(ability.__str__(), str)

    def test_abilities_details(self):
        for _, ability in self.setup().items():
            self.assertIsNotNone(ability.details())
            self.assertIsInstance(ability.details(), str)

    def test_abilities_export(self):
        for _, ability in self.setup().items():
            self.assertIsNotNone(ability.export())
            self.assertIsInstance(ability.export(), dict)

    def test_abilities_print_to_file(self):
        test_ability = self.setup()["Magic"]
        test_ability.print_to_file()
        filename = f"{test_ability.name}.json"
        self.assertTrue(os.path.exists(filename), "Abilities: print_to_file Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_abilities_output_examples(self):
        damage_ability = self.setup()["Magic"]
        print(f"\n{'Abilites Example Output'.center(80, '-')}")
        print(f"\n__str__ Output:\n{damage_ability}")
        print(f"\ndetails Output:{damage_ability.details()}")
        print(f"\nexport Output:\n{damage_ability.export()}")
        print(f"\n{'Done'.center(80, '-')}")

    def test_abilities_copy(self):
        abilities = self.setup()

        repair_1 = abilities["Repair"]
        repair_2 = repair_1.copy()

        # Test object difference
        self.assertNotEqual(repair_1, repair_2)
        self.assertNotEqual(id(repair_1), id(repair_2))
        
        # Test Information is the same
        self.assertEqual(repair_1.name, repair_2.name)
        self.assertEqual(repair_1.damage_type, repair_2.damage_type)
        self.assertEqual(repair_1.ability_group, repair_2.ability_group)
        self.assertEqual(repair_1.effect, repair_2.effect)
        self.assertEqual(repair_1.description, repair_2.description)
