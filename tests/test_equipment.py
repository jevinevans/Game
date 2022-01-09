"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""


import os
import unittest
from typing import Any
from FUNCLG.character.equipment import Equipment


class EquipmentTest(unittest.TestCase):
    def setup(self) -> Equipment:
        return Equipment(
         name="Test_Equipment",
            description="This is a test for the equipment class",
            armorType=0,
            itemType=0,
            weaponType=None,
            level=2,
            abilityPoints=50,
        )

    def test_equipment_init(self):
        equipObj = self.setup()
        # Testing proper initialization
        self.assertEqual(equipObj.name, "Test_Equipment")
        self.assertEqual(equipObj.description, "This is a test for the equipment class")
        self.assertEqual(equipObj.armorType, 0)
        self.assertEqual(equipObj.itemType, 0)
        self.assertIsNone(equipObj.weaponType)
        self.assertGreater(equipObj.abilityPoints, 0)
        self.assertGreater(equipObj.level, 0)

    def test_equipment_str(self):
        equipObj = self.setup()
        self.assertIsNotNone(equipObj.__str__())
        self.assertIsInstance(equipObj.__str__(), str)

    def test_equipment_details(self):
        equipObj = self.setup()
        self.assertIsNotNone(equipObj.details())
        self.assertIsInstance(equipObj.details(), str)

    def test_equipment_print_to_file(self):
        equipObj = self.setup()
        equipObj.print_to_file()
        filename = f"{equipObj.name}.json"
        self.assertTrue(os.path.exists(filename), "Equipment: print_to_file Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_equipment_export(self):
        # Testing of null value
        equipObj = self.setup()
        self.assertIsNotNone(equipObj.export())
        self.assertIsInstance(equipObj.export(), dict)

    def test_equipment_output_examples(self):
        equipObj = self.setup()  
        print(f"\n{'Equipment Example Output'.center(80, '-')}")
        print(f"\n__str__ Output:\n{equipObj}")
        print(f"\ndetails Output: {equipObj.details()}")
        print(f"\nexport Output:\n{equipObj.export()}")
        print(f"\n{'Done'.center(80, '-')}")
    # TODO: def test_equipment_getStats(self:)
