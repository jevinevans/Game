#####################################################################################   
#   Programmer: Jevin Evans                                                         #
#	Date: 7/15/2021                                                                 #
#	Program: Equipment Class Test                                                   #
#   Description: The is a unit test for the equipment class.                        #      
#####################################################################################


import unittest, os
from core import equipment
from utils.types import *

class EquipmentTest(unittest.TestCase):

    
    def test_init(self):
        equip = equipment.Equipment("Test_Equipment", "This is a test for the equipment class", 0, 0, None, 2, 50)

        #Testing proper initialization
        self.assertEqual(equip.name, "Test_Equipment")
        self.assertEqual(equip.description, "This is a test for the equipment class")
        self.assertEqual(equip.armorType, 0)
        self.assertEqual(equip.itemType, 0)
        self.assertIsNone(equip.weaponType)
        self.assertGreater(equip.abilityPoints, 0)
        self.assertGreater(equip.itemLevel, 0)

    def test_printToFile(self):
        equip = equipment.Equipment("Test_Equipment", "This is a test for the equipment class", 0, 0, None, 2, 50)
        equip.printToFile()
        self.assertTrue(os.path.exists(equip.name+".json"), "PrintToFile Failed")

def run():
    unittest.main()

    