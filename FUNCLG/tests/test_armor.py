#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/15/2021                                                                 #
#   Program: Armor Class Test                                                       #
#   Description: The is a unit test for the armor class and its interations         #
#       with the equipment class.                                                   #
#####################################################################################


import os
import unittest
from random import randint

from core.armor import Armor
from core.equipment import Equipment
from utils.types import ITEM_TYPES


class ArmorTest(unittest.TestCase):
    def setup(self, raw=True):
        armorType = 1
        equips = {}
        equips["armorType"] = armorType
        equips["head"] = Equipment(
            "Gold Head",
            "Head piece for Armor Test.",
            armorType,
            0,
            None,
            randint(0, 100),
            randint(0, 500),
        )
        equips["chest"] = Equipment(
            "Gold Chest",
            "Chest piece for Armor Test.",
            armorType,
            1,
            None,
            randint(0, 100),
            randint(0, 500),
        )
        equips["back"] = Equipment(
            "Gold Cape",
            "Back piece for Armor Test.",
            armorType,
            2,
            None,
            randint(0, 100),
            randint(0, 500),
        )
        equips["pants"] = Equipment(
            "Gold pants",
            "Pants piece for Amror Test",
            armorType,
            3,
            None,
            randint(0, 100),
            randint(0, 500),
        )
        equips["sword"] = Equipment(
            "Gold Sword",
            "Sword weapon for Armor Test",
            armorType,
            4,
            0,
            randint(0, 100),
            randint(0, 500),
        )
        equips["wand"] = Equipment(
            "Gold Wand",
            "Wand weapon for Armor Test",
            armorType + 1,
            4,
            1,
            randint(0, 100),
            randint(0, 500),
        )
        equips["knife"] = Equipment(
            "Gold Knife",
            "Knife weapon for Armor Test",
            armorType,
            4,
            2,
            randint(0, 100),
            randint(0, 500),
        )

        if raw:
            """Returns new Armor and dict of equipments"""
            return Armor(armorType), equips
        else:
            """Returns full equiped Armor plus other weapon"""
            return (
                Armor(
                    armorType,
                    equips["head"],
                    equips["chest"],
                    equips["back"],
                    equips["pants"],
                    equips["sword"],
                ),
                equips,
            )

    def test_init(self):
        # 1 - Testing blank armor initialization

        arm, equips = self.setup()
        self.assertEqual(arm.armorType, equips["armorType"])
        self.assertIsNone(arm.head, "Armor Equipment field is not none")
        self.assertIsNone(arm.chest, "Armor Equipment field is not none")
        self.assertIsNone(arm.back, "Armor Equipment field is not none")
        self.assertIsNone(arm.pants, "Armor Equipment field is not none")
        self.assertIsNone(arm.weapon, "Armor Equipment field is not none")

        self.assertEqual(Armor._id - 1, int(arm.name.split("_")[1]))

        # 2 - Testing creation of full armor initialization

        arm, equips = self.setup(False)
        self.assertEqual(arm.armorType, equips["armorType"])
        self.assertEqual(arm.head, equips["head"])
        self.assertEqual(arm.chest, equips["chest"])
        self.assertEqual(arm.back, equips["back"])
        self.assertEqual(arm.pants, equips["pants"])
        self.assertEqual(arm.weapon, equips["sword"])

        self.assertEqual(Armor._id - 1, int(arm.name.split("_")[1]))

    def test_str(self):
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

    def test_equip(self):
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

    def test_dequip(self):
        # Test 1.a: Basic dequip, dequiping with integer, with item equipped
        arms, equips = self.setup(False)

        # Will do a full dequip of all items
        for x in range(5):
            self.assertIsNotNone(arms.dequip(x))

        self.assertEqual(arms.__str__(), f"{arms.name}: <H:0, C:0, B:0, P:0, W:0>")

        # Test 1.b Basic dequip, dequiping with string, with item equipped
        arms, equips = self.setup(False)

        # Will do a full dequip of all items
        for x in ITEM_TYPES:
            self.assertIsNotNone(arms.dequip(x))

        self.assertEqual(arms.__str__(), f"{arms.name}: <H:0, C:0, B:0, P:0, W:0>")

        # Test 2.a Testing dequip error for integer value
        arms, equips = self.setup(False)

        self.assertIsNone(arms.dequip(-1))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # Test 2.b Testing dequip error for string value
        arms, equips = self.setup(False)

        self.assertIsNone(arms.dequip("jagiejoijga"))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # Test 2.c Testing dequip error for other value
        arms, equips = self.setup(False)

        self.assertIsNone(arms.dequip(["head", "chest"]))
        self.assertIsNone(arms.dequip(dict()))
        self.assertEqual(arms.__str__(), f"{arms.name}: <H:1, C:1, B:1, P:1, W:1>")

        # TODO: Test 3.a Dequipping an empty slot with integer
        self.fail("Test 3.a")

        # TODO: Test 3.b Dequipping an empty slot with string
        self.fail("Test 3.b")

    def test_details(self):
        # TODO: test full armor detail
        self.fail("Need to Create Test")

        # TODO: test empty details
        self.fail("Need to Create Test")

    def test_printToFile(self):
        # Testing printToFile existance

        arm, equips = self.setup(False)
        arm.printToFile()
        filename = f"{arm.name}.json"
        self.assertTrue(os.path.exists(filename), "PrintToFile Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_export(self):
        # TODO: test against proper dict option and reload
        arm, equips = self.setup()
        self.fail("Need to Create Test")


def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
