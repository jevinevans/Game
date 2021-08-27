#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/15/2021                                                                 #
#   Program: Armor Class Test                                                       #
#   Description: The is a unit test for the armor class and its interations         #
#       with the equipment class.                                                   #
#####################################################################################

import unittest, os
from random import randint
from core.armor import Armor
from core.equipment import Equipment


class ArmorTest(unittest.TestCase):
    def setup(self, raw=True):
        armorType = 1
        equips = {}
        equips['armorType'] = armorType
        equips['head'] = Equipment("Gold Head", "Head piece for Armor Test.", armorType, 0, None, randint(0,100), randint(0,500))
        equips['chest'] = Equipment("Gold Chest", "Chest piece for Armor Test.", armorType, 1, None, randint(0,100), randint(0,500))
        equips['back'] = Equipment("Gold Cape", "Back piece for Armor Test.", armorType, 2, None, randint(0,100), randint(0,500))
        equips['pants'] = Equipment("Gold pants", "Pants piece for Amror Test", armorType, 3, None, randint(0,100), randint(0,500))
        equips['sword'] = Equipment("Gold Sword", "Sword weapon for Armor Test", armorType, 4, 0, randint(0,100), randint(0,500))
        equips['wand'] = Equipment("Gold Wand", "Wand weapon for Armor Test", armorType + 1, 4, 1, randint(0,100), randint(0,500))
        equips['knife'] = Equipment("Gold Knife", "Knife weapon for Armor Test", armorType, 4, 2, randint(0,100), randint(0,500))

        if raw:
            """Returns new Armor and dict of equipments"""
            return Armor(armorType), equips
        else:
            """Returns full equiped Armor plus other weapon"""
            return Armor(armorType, equips['head'], equips['chest'], equips['back'], equips['pants'], equips['sword']), equips

    def test_init(self):
        # Testing blank armor initialization

        arm, equips = self.setup()
        self.assertEqual(arm.armorType, equips['armorType'])
        self.assertIsNone(arm.head, "Armor Equipment field is not none")
        self.assertIsNone(arm.chest, "Armor Equipment field is not none")
        self.assertIsNone(arm.back, "Armor Equipment field is not none")
        self.assertIsNone(arm.pants, "Armor Equipment field is not none")
        self.assertIsNone(arm.weapon, "Armor Equipment field is not none")

        self.assertEqual(Armor._id, 1)
        
        # Testing creation of full armor initialization

        arm, equips = self.setup(False)
        self.assertEqual(arm.armorType, equips['armorType'])
        self.assertEqual(arm.head, equips["head"])
        self.assertEqual(arm.chest, equips["chest"])
        self.assertEqual(arm.back, equips["back"])
        self.assertEqual(arm.pants, equips["pants"])
        self.assertEqual(arm.weapon, equips["sword"])

        self.assertEqual(Armor._id, 2)

    def test_str(self):
        """
            Testing object print format
        """
        self.fail("Need to Create Test")

    def test_equip(self):
        """
            Testing that the equip function for success
        """
        # TODO: testing ability to equip items empty location
        self.fail("Need to Create Test")

        # TODO: testing ability to equip an item that is not empty and return it
        self.fail("Need to Create Test")

        # TODO: testing ability to not equip uncompatible items
        self.fail("Need to Create Test")

    def test_dequip(self):
        # TODO: test integer ability to dequip item
        self.fail("Need to Create Test")

        # TODO: test string ability to dequip
        self.fail("Need to Create Test")
        
        # TODO: test error dequip
        self.fail("Need to Create Test")

        # TODO: test attempt to dequip on empty Armor
        self.fail("Need to Create Test")

    def test_details(self):
        # TODO: test full armor detail
        self.fail("Need to Create Test")

        # TODO: test empty details
        self.fail("Need to Create Test")

    def test_printToFile(self):
        """
            Testing printToFile existance
        """
        arm, equips = self.setup(False)
        arm.printToFile()
        filename = f"{arm.name}.json"
        self.assertTrue(os.path.exists(filename), "PrintToFile Failed")
        if os.path.exists(filename):
            os.remove(filename)

    def test_export(self):
        # TODO: test against proper dict option and reload
        self.fail("Need to Create Test")

def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
