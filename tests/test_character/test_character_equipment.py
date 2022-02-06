"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""


import os
import unittest
from random import randint

from FUNCLG.character.equipment import Equipment

BODY_ITEM_TYPE = randint(0, 3)
BODY_ARMOR_TYPE = randint(0, 2)


class EquipmentTest(unittest.TestCase):
    @staticmethod
    def get_body() -> Equipment:
        return Equipment(
            name="Test_Equipment",
            description="This is a test for the equipment class",
            item_type=BODY_ITEM_TYPE,
            armor_type=BODY_ARMOR_TYPE,
            weapon_type=-1,
            level=2,
            damage=50,
        )

    @staticmethod
    def get_weapon() -> Equipment:
        return Equipment(
            name="Test_Equipment",
            description="This is a test for the equipment class",
            item_type=4,
            armor_type=-1,
            weapon_type=1,
            level=2,
            damage=50,
        )

    @staticmethod
    def get_equipment():
        return [EquipmentTest.get_body(), EquipmentTest.get_weapon()]

    def test_equipment_init(self):
        # Testing body equip
        head = self.get_body()
        self.assertEqual(head.name, "Test_Equipment")
        self.assertEqual(head.description, "This is a test for the equipment class")
        self.assertEqual(head.item_type, BODY_ITEM_TYPE)
        self.assertEqual(head.armor_type, BODY_ARMOR_TYPE)
        self.assertEqual(head.weapon_type, -1)
        self.assertGreater(head.damage, 0)
        self.assertGreater(head.level, 0)

        weapon = self.get_weapon()
        # Testing proper initialization
        self.assertEqual(weapon.name, "Test_Equipment")
        self.assertEqual(weapon.description, "This is a test for the equipment class")
        self.assertEqual(weapon.item_type, 4)
        self.assertEqual(weapon.armor_type, -1)
        self.assertEqual(weapon.weapon_type, 1)
        self.assertGreater(weapon.damage, 0)
        self.assertGreater(weapon.level, 0)

    def test_equipment_str(self):
        for equip in EquipmentTest.get_equipment():
            self.assertIsNotNone(equip.__str__())
            self.assertIsInstance(equip.__str__(), str)

    def test_equipment_details(self):
        for equip in EquipmentTest.get_equipment():
            self.assertIsNotNone(equip.details())
            self.assertIsInstance(equip.details(), str)

    def test_equipment_print_to_file(self):
        equip_obj = self.get_body()
        equip_obj.print_to_file()
        filename = f"{equip_obj.name}.json"
        self.assertTrue(os.path.exists(filename), "Equipment: print_to_file Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_equipment_export(self):
        # Testing of null value
        for equip in EquipmentTest.get_equipment():
            self.assertIsNotNone(equip.export())
            self.assertIsInstance(equip.export(), dict)

    def test_equipment_output_examples(self):

        print(f"\n{'Equipment Example Output'.center(80, '-')}")
        for equip in EquipmentTest.get_equipment():
            print(f"\n__str__ Output:\n{equip}")
            print(f"\ndetails Output: {equip.details()}")
            print(f"\nexport Output:\n{equip.export()}")
        print(f"\n{'Done'.center(80, '-')}")

    # TODO: def test_equipment_getStats(self:)

    def test_equipment_duplicate_call(self):
        e1 = self.get_equipment()[0]
        e2 = self.get_equipment()[0]

        self.assertNotEqual(e1, e2)
        self.assertNotEqual(id(e1), id(e2))