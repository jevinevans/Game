#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/15/2021                                                                 #
#   Program: Equipment Class Test                                                   #
#   Description: The is a unit test for the equipment class.                        #
#####################################################################################


import unittest, os
from core.equipment import Equipment
# from utils.types import *


class EquipmentTest(unittest.TestCase):

    def setup(self):
        return Equipment("Test_Equipment", "This is a test for the equipment class", 0, 0, None, 2, 50)

    def test_init(self):
        equipObj = self.setup()
        # Testing proper initialization
        self.assertEqual(equipObj.name, "Test_Equipment")
        self.assertEqual(equipObj.description, "This is a test for the equipment class")
        self.assertEqual(equipObj.armorType, 0)
        self.assertEqual(equipObj.itemType, 0)
        self.assertIsNone(equipObj.weaponType)
        self.assertGreater(equipObj.abilityPoints, 0)
        self.assertGreater(equipObj.level, 0)

    def test__str__(self):
        equipObj = self.setup()
        self.assertEqual(equipObj.__str__(), "Test_Equipment (lvl. 2) [Light Helmet]")
        """ Testing Different Level and Armor Type"""
        equipObj.level = 50
        equipObj.armorType = 1
        self.assertEqual(equipObj.__str__(), "Test_Equipment (lvl. 50) [Medium Helmet]")
        
    def test_details(self):
        equipObj = self.setup()
        eDetails = equipObj.details()
        self.assertIn("-" * (2 + len(equipObj.name)), eDetails)
        self.assertIn(equipObj.name, eDetails)
        self.assertIn(str(equipObj.level), eDetails)
        self.assertIn(str(equipObj.abilityPoints), eDetails)
        self.assertIn(equipObj.getItemType(), eDetails)
        self.assertIn(equipObj.getItemDescription(), eDetails)
        self.assertIn(equipObj.description, eDetails)

    def test_printToFile(self):
        equipObj = self.setup()
        equipObj.printToFile()
        filename = f"{equipObj.name}.json"
        self.assertTrue(os.path.exists(filename), "PrintToFile Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_export1(self):
        equipObj = self.setup()
        self.assertEqual(equipObj.export(), equipObj.__dict__)
    
    def test_export2(self):
        equipObj = self.setup()
        equipObj.weaponType = 2
        self.assertEqual(equipObj.export(), equipObj.__dict__)

    # def test_getStats(self:)


def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
