"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the armor class and its interations with the equipment class.
"""

import unittest
from random import randint
from typing import Dict, Tuple

from FUNCLG.character.armor import Armor
from FUNCLG.character.equipment import Equipment, WeaponEquipment
from FUNCLG.utils.types import ITEM_TYPES


class ArmorTest(unittest.TestCase):
    def setup(self, raw=True) -> Tuple[Armor, Dict[str, Equipment]]:
        armor_type = 1
        equips = {}
        equips["armor_type"] = armor_type
        equips["head"] = Equipment(
            name="Gold Head",
            description="Head piece for Armor Test.",
            armor_type=armor_type,
            item_type=0,
        )
        equips["chest"] = Equipment(
            name="Gold Chest",
            description="Chest piece for Armor Test.",
            armor_type=armor_type,
            item_type=1,
        )
        equips["back"] = Equipment(
            name="Gold Cape",
            description="Back piece for Armor Test.",
            armor_type=armor_type,
            item_type=2,
        )
        equips["pants"] = Equipment(
            name="Gold pants",
            description="Pants piece for Amror Test",
            armor_type=armor_type,
            item_type=3,
        )
        equips["sword"] = WeaponEquipment(
            name="Gold Sword",
            description="Sword weapon for Armor Test",
            armor_type=armor_type,
            weapon_type=0,
        )
        equips["wand"] = WeaponEquipment(
            name="Gold Wand",
            description="Wand weapon for Armor Test",
            armor_type=armor_type + 1,
            weapon_type=1,
        )
        equips["knife"] = WeaponEquipment(
            name="Gold Knife",
            description="Knife weapon for Armor Test",
            armor_type=armor_type,
            weapon_type=2,
        )

        if raw:
            # Returns new Armor and dict of equipments
            return Armor(armor_type), equips
        # Returns full equiped Armor plus other weapon
        return (
            Armor(
                armor_type=armor_type,
                head=equips["head"],
                chest=equips["chest"],
                back=equips["back"],
                pants=equips["pants"],
                weapon=equips["sword"],
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

        # 2 - Testing creation of full armor initialization

        arm, equips = self.setup(False)
        self.assertEqual(arm.armor_type, equips["armor_type"])
        self.assertNotEqual(arm.head, equips["head"])
        self.assertNotEqual(arm.chest, equips["chest"])
        self.assertNotEqual(arm.back, equips["back"])
        self.assertNotEqual(arm.pants, equips["pants"])
        self.assertNotEqual(arm.weapon, equips["sword"])

        self.assertEqual(arm.head.name, equips["head"].name)
        self.assertEqual(arm.chest.name, equips["chest"].name)
        self.assertEqual(arm.back.name, equips["back"].name)
        self.assertEqual(arm.pants.name, equips["pants"].name)
        self.assertEqual(arm.weapon.name, equips["sword"].name)

    def test_armor_str(self):
        # Testing object print format

        # 1 - Testing Raw Armor
        arm, equips = self.setup()
        self.assertEqual(arm.__str__(), f"Medium Armor: <H:0, C:0, B:0, P:0, W:0>")

        # 2 - Testing Partial Armor - Head Chest Pants
        arm, equips = self.setup()
        arm.head = equips["head"]
        arm.chest = equips["chest"]
        arm.pants = equips["pants"]
        self.assertEqual(arm.__str__(), f"Medium Armor: <H:1, C:1, B:0, P:1, W:0>")

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

        self.assertEqual(arm.head.name, equips["head"].name)
        self.assertEqual(arm.chest.name, equips["chest"].name)
        self.assertEqual(arm.back.name, equips["back"].name)
        self.assertEqual(arm.pants.name, equips["pants"].name)
        self.assertEqual(arm.weapon.name, equips["sword"].name)

        # 2 - Testing ability to equip an item that is not empty and return it (change equips)
        arm, equips = self.setup(False)
        arm.equip(equips["knife"])
        self.assertEqual(arm.weapon.name, equips["knife"].name)

        # 3 - Testing ability to not equip uncompatible items
        arm, equips = self.setup(False)

        arm.equip(equips["wand"])
        self.assertEqual(arm.weapon.name, equips["sword"].name)

    def test_armor_dequip(self):
        # Test 1.a Basic dequip, dequiping with string, with item equipped
        arms, _ = self.setup(False)

        for item in ITEM_TYPES:
            self.assertIsNone(arms.dequip(item))
            # TODO: For pytest, us patch to check the status of the message

        self.assertEqual(arms.__str__(), f"Medium Armor: <H:0, C:0, B:0, P:0, W:0>")

        # Test 2.a Testing dequip error for string value
        arms, _ = self.setup(False)

        self.assertIsNone(arms.dequip("jagiejoijga"))
        self.assertEqual(arms.__str__(), f"Medium Armor: <H:1, C:1, B:1, P:1, W:1>")

        # Test 3.a Dequipping an empty slot with string
        for item in ITEM_TYPES:
            self.assertIsNone(arms.dequip(item))

    def test_armor_details(self):
        # 1.a Test full armor details
        arms, _ = self.setup(False)
        self.assertIsNotNone(arms.details())
        self.assertIsInstance(arms.details(), str)

        arms, _ = self.setup()
        self.assertIsNotNone(arms.details())
        self.assertIsInstance(arms.details(), str)

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

    def test_armor_same_item_different_armors(self):
        arm1, equips = self.setup(raw=True)
        arm2, _ = self.setup(raw=True)

        arm1.equip(equips["head"])
        arm2.equip(equips["head"])

        self.assertNotEqual(arm1.head, arm2.head)
        self.assertNotEqual(id(arm1.head), id(arm2.head))
