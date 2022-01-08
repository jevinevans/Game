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
from typing import Tuple, Dict
from FUNCLG.character.armor import Armor
from FUNCLG.character.equipment import Equipment
from FUNCLG.utils.types import ITEM_TYPES


class ArmorTest(unittest.TestCase):
    def setup(self, raw=True) -> Tuple[Equipment, Dict[str, Equipment]]:
        armorType = 1
        equips = {}
        equips["armorType"] = armorType
        equips["head"] = Equipment(
            name = "Gold Head",
            description = "Head piece for Armor Test.",
            armorType = armorType,
            itemType = 0,
            weaponType = None,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["chest"] = Equipment(
            name = "Gold Chest",
            description = "Chest piece for Armor Test.",
            armorType = armorType,
            itemType = 1,
            weaponType = None,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["back"] = Equipment(
            name = "Gold Cape",
            description = "Back piece for Armor Test.",
            armorType = armorType,
            itemType = 2,
            weaponType = None,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["pants"] = Equipment(
            name = "Gold pants",
            description = "Pants piece for Amror Test",
            armorType = armorType,
            itemType = 3,
            weaponType = None,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["sword"] = Equipment(
            name = "Gold Sword",
            description = "Sword weapon for Armor Test",
            armorType = armorType,
            itemType = 4,
            weaponType = 0,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["wand"] = Equipment(
            name = "Gold Wand",
            description = "Wand weapon for Armor Test",
            armorType = armorType + 1,
            itemType = 4,
            weaponType = 1,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )
        equips["knife"] = Equipment(
            name = "Gold Knife",
            description = "Knife weapon for Armor Test",
            armorType = armorType,
            itemType = 4,
            weaponType = 2,
            level = randint(0, 100),
            abilityPoints = randint(0, 500),
        )

        if raw:
            """Returns new Armor and dict of equipments"""
            return Armor(armorType), equips
        else:
            """Returns full equiped Armor plus other weapon"""
            return (
                Armor(
                    armorType = armorType,
                    head = equips["head"],
                    chest = equips["chest"],
                    back = equips["back"],
                    pants = equips["pants"],
                    weapon = equips["sword"],
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
        # Test 1.a Basic dequip, dequiping with integer, with item equipped
        arms, _ = self.setup(False)

        # Will do a full dequip of all items
        for x in range(5):
            self.assertIsNotNone(arms.dequip(x))

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
        print("\n\nDequip Test\n")
        for x in range(len(ITEM_TYPES)):
            self.assertIsNone(arms.dequip(x))
        
        # Test 3.b Dequipping an empty slot with string
        for x in ITEM_TYPES:
            self.assertIsNone(arms.dequip(x))

    def test_details(self):
        # 1.a Test full armor details
        arms, _ = self.setup(False)
        for equipment in arms.getEquipment():
            self.assertIn(equipment.__str__(), arms.details())

        # 1.b Test empty details
        arms, _ = self.setup()
        for equipment in arms.getEquipment():
            self.assertIn(equipment.__str__(), arms.details())

    def test_printToFile(self):
        # 1. Testing printToFile existance
        arm, _ = self.setup(False)
        arm.printToFile()
        filename = f"{arm.name}.json"
        self.assertTrue(os.path.exists(filename), "PrintToFile Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_export(self):
        # TODO: test against proper dict option and reload
        arm, _ = self.setup(False)
        self.assertEqual(arm.export(), arm.__dict__)

    def test_itemCopy(self):
        arm1, _ = self.setup(False)
        arm2, _ = self.setup(False)
        self.assertNotEqual(id(arm1), id(arm2))
        self.assertNotEqual(id(arm1.head), id(arm2.head))
        self.assertNotEqual(id(arm1.chest), id(arm2.chest))
        self.assertNotEqual(id(arm1.back), id(arm2.back))
        self.assertNotEqual(id(arm1.pants), id(arm2.pants))
        self.assertNotEqual(id(arm1.weapon), id(arm2.weapon))