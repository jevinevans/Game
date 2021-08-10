#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/15/2021                                                                 #
#   Program: Equipment Class Test                                                   #
#   Description: The is a unit test for the equipment class.                        #
#####################################################################################


import unittest, os
from core import equipment
# from utils.types import *


class EquipmentTest(unittest.TestCase):

    def setup(self):
        return equipment.Equipment("Test_Equipment", "This is a test for the equipment class", 0, 0, None, 2, 50)

    def test_init(self):
        equip = self.setup()
        # Testing proper initialization
        self.assertEqual(equip.name, "Test_Equipment")
        self.assertEqual(equip.description, "This is a test for the equipment class")
        self.assertEqual(equip.armorType, 0)
        self.assertEqual(equip.itemType, 0)
        self.assertIsNone(equip.weaponType)
        self.assertGreater(equip.abilityPoints, 0)
        self.assertGreater(equip.itemLevel, 0)

    def test_printToFile(self):
        equip = self.setup()
        equip.printToFile()
        self.assertTrue(os.path.exists(equip.name + ".json"), "PrintToFile Failed")
        if os.path.exists(f"{equip.name}.json"):
            os.remove(f"{equip.name}.json")

    def test__str__(self):
        equip = self.setup()
        self.assertEqual(equip.__str__(), "Test_Equipment (lvl. 2) [Light Helmet]")
        
    # def test_details(self):
    # def test_export(self):
    # def test_getStats(self:)


def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
