"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the armor class and its interations with the equipment class.
"""


import os
import unittest
from random import randint
from typing import Tuple, Dict
from FUNCLG.character.armor import Armor
from FUNCLG.character.equipment import Equipment
from FUNCLG.utils.types import ITEM_TYPES


class ArmorTest(unittest.TestCase):
    def setup(self, raw=True) -> Tuple[Armor, Dict[str, Equipment]]:
        armor_type = 1
        equips = {}
        equips["armor_type"] = armor_type
        equips["head"] = Equipment(
            name = "Gold Head",
            description = "Head piece for Armor Test.",
            armor_type = armor_type,
            item_type = 0,
            weapon_type = None,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["chest"] = Equipment(
            name = "Gold Chest",
            description = "Chest piece for Armor Test.",
            armor_type = armor_type,
            item_type = 1,
            weapon_type = None,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["back"] = Equipment(
            name = "Gold Cape",
            description = "Back piece for Armor Test.",
            armor_type = armor_type,
            item_type = 2,
            weapon_type = None,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["pants"] = Equipment(
            name = "Gold pants",
            description = "Pants piece for Amror Test",
            armor_type = armor_type,
            item_type = 3,
            weapon_type = None,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["sword"] = Equipment(
            name = "Gold Sword",
            description = "Sword weapon for Armor Test",
            armor_type = armor_type,
            item_type = 4,
            weapon_type = 0,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["wand"] = Equipment(
            name = "Gold Wand",
            description = "Wand weapon for Armor Test",
            armor_type = armor_type + 1,
            item_type = 4,
            weapon_type = 1,
            level = randint(0, 100),
            damage = randint(0, 500),
        )
        equips["knife"] = Equipment(
            name = "Gold Knife",
            description = "Knife weapon for Armor Test",
            armor_type = armor_type,
            item_type = 4,
            weapon_type = 2,
            level = randint(0, 100),
            damage = randint(0, 500),
        )

        if raw:
            """Returns new Armor and dict of equipments"""
            return Armor(armor_type), equips
        else:
            """Returns full equiped Armor plus other weapon"""
            return (
                Armor(
                    armor_type = armor_type,
                    head = equips["head"],
                    chest = equips["chest"],
                    back = equips["back"],
                    pants = equips["pants"],
                    weapon = equips["sword"],
                ),
                equips,
            )

    def test_armor_init(self):
        # 1 - Testing blank armor initialization

        arm, equips = self.setup()
        self.assertEqual(arm.armor_type, equips["armor_type"])
        self.assertIsNone(arm.head, "Armor Equipment field is not none")
        self.assertIsNone(arm.chest, "Armor Equipment field is not none")
        self.assertIsNone(arm.back, "Armor Equipment field is not none")
        self.assertIsNone(arm.pants, "Armor Equipment field is not none")
        self.assertIsNone(arm.weapon, "Armor Equipment field is not none")
        self.assertEqual(Armor._id - 1, int(arm.name.split("_")[1]))

        # 2 - Testing creation of full armor initialization

        arm, equips = self.setup(False)
        self.assertEqual(arm.armor_type, equips["armor_type"])
        self.assertEqual(arm.head, equips["head"])
        self.assertEqual(arm.chest, equips["chest"])
        self.assertEqual(arm.back, equips["back"])
        self.assertEqual(arm.pants, equips["pants"])
        self.assertEqual(arm.weapon, equips["sword"])

        self.assertEqual(Armor._id - 1, int(arm.name.split("_")[1]))

    def test_armor_str(self):
        # Testing object print format

        # 1 - Testing Raw Armor
        arm, equips = self.setup()
        self.assertEqual(
            arm.__str__(), f"Armor_{Armor._id-1}: <H:0, C:0, B:0, P:0, W:0>"
        )

        # 2 - Testing Partial Armor - Head Chest Pants
        arm, equips = self.setup()
        arm.head = equips["head"]
        arm.chest = equips["chest"]
        arm.pants = equips["pants"]
        self.assertEqual(
            arm.__str__(), f"Armor_{Armor._id-1}: <H:1, C:1, B:0, P:1, W:0>"
        )

    def test_armor_equip(self):
        # 1 - Testing ability to equip items empty location
        arm, equips = self.setup()
        arm.equip(equips["head"])
        arm.equip(equips["chest"])
        arm.equip(equips["back"])
        arm.equip(equips["pants"])
        arm.equip(equips["sword"])

        self.assertIsNotNone(arm.head)
        self.assertIsNotNone(arm.chest)
        self.assertIsNotNone(arm.back)
        self.assertIsNotNone(arm.pants)
        self.assertIsNotNone(arm.weapon)

        self.assertEqual(arm.head, equips["head"])
        self.assertEqual(arm.chest, equips["chest"])
        self.assertEqual(arm.back, equips["back"])
        self.assertEqual(arm.pants, equips["pants"])
        self.assertEqual(arm.weapon, equips["sword"])

        # 2 - Testing ability to equip an item that is not empty and return it (change equips)
        arm, equips = self.setup(False)

        temp = None
        self.assertIsNone(temp)

        temp = arm.equip(equips["knife"])
        self.assertIsNotNone(temp)
        self.assertEqual(temp, equips["sword"])
        self.assertEqual(arm.weapon, equips["knife"])

        # 3 - Testing ability to not equip uncompatible items
        arm, equips = self.setup(False)
        temp = None
        self.assertIsNone(temp)

        temp = arm.equip(equips["wand"])
        self.assertIsNotNone(temp)
        self.assertEqual(temp, equips["wand"])
        self.assertEqual(arm.weapon, equips["sword"])

    def test_armor_dequip(self):
        # Test 1.a Basic dequip, dequiping with integer, with item equipped
        arms, _ = self.setup(False)

        # Will do a full dequip of all items
        for position in range(5):
            print(arms)
            self.assertIsNotNone(arms.dequip(position))

        self.assertEqual(arms.__str__(), f"{arms.name}: <H:0, C:0, B:0, P:0, W:0>")

        # Test 1.b Basic dequip, dequiping with string, with item equipped
        arms, _ = self.setup(False)

        for x in ITEM_TYPES:
            self.assertIsNotNone(arms.dequip(x))

        self.assertEqual(arms.__str__(), f"{arms.name}: <H:0, C:0, B:0, P:0, W:0>")

        # Test 2.a Testing dequip error for integer value
        arms, _ = self.setup(False)

        self.assertIsNone(arms.dequip(-1))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # Test 2.b Testing dequip error for string value
        arms, _ = self.setup(False)

        self.assertIsNone(arms.dequip("jagiejoijga"))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # Test 2.c Testing dequip error for other value
        arms, _ = self.setup(False)

        self.assertIsNone(arms.dequip(["head", "chest"]))
        self.assertIsNone(arms.dequip(dict()))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # Test 3.a Dequipping an empty slot with integer
        arms, _ = self.setup()
        for x in range(len(ITEM_TYPES)):
            self.assertIsNone(arms.dequip(x))
        
        # Test 3.b Dequipping an empty slot with string
        for x in ITEM_TYPES:
            self.assertIsNone(arms.dequip(x))

    def test_armor_details(self):
        # 1.a Test full armor details
        arms, _ = self.setup(False)
        self.assertIsNotNone(arms.details())
        self.assertIsInstance(arms.details(), str)
        
        arms, _ = self.setup()
        self.assertIsNotNone(arms.details())
        self.assertIsInstance(arms.details(), str)

    def test_armor_print_to_file(self):
        # 1. Testing printToFile existance
        arm, _ = self.setup(False)
        arm.print_to_file()
        filename = f"{arm.name}.json"
        self.assertTrue(os.path.exists(filename), "Armor: print_to_file Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_armor_export(self):
        arm, _ = self.setup(False)
        self.assertIsNotNone(arm.export())
        self.assertIsInstance(arm.export(), dict)

        arm, _ = self.setup()
        self.assertIsNotNone(arm.export())
        self.assertIsInstance(arm.export(), dict)

    def test_armor_item_copy(self):
        arm1, _ = self.setup(False)
        arm2, _ = self.setup(False)
        self.assertNotEqual(id(arm1), id(arm2))
        self.assertNotEqual(id(arm1.head), id(arm2.head))
        self.assertNotEqual(id(arm1.chest), id(arm2.chest))
        self.assertNotEqual(id(arm1.back), id(arm2.back))
        self.assertNotEqual(id(arm1.pants), id(arm2.pants))
        self.assertNotEqual(id(arm1.weapon), id(arm2.weapon))
    
    def test_armor_output_examples(self):
        arm, _ = self.setup(raw=False)
        print(f"\n{'Armor Example Output'.center(80, '-')}")
        print(f"\n__str__ Output:\n{arm}")
        print(f"\ndetails Output:{arm.details()}")
        print(f"\nexport Output:\n{arm.export()}")
        print(f"\n{'Done'.center(80, '-')}")