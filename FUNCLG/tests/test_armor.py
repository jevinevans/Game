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
        equips['head'] = Equipment("Gold Head", "Head piece for Armor Test.", armorType, 0, None, randint(0,100), randint(0,500))
        equips['chest'] = Equipment("Gold Chest", "Chest piece for Armor Test.", armorType, 1, None, randint(0,100), randint(0,500))
        equips['back'] = Equipment("Gold Cape", "Back piece for Armor Test.", armorType, 2, None, randint(0,100), randint(0,500))
        equips['pants'] = Equipment("Gold pants", "Pants piece for Amror Test", armorType, 3, None, randint(0,100), randint(0,500))
        equips['sword'] = Equipment("Gold Sword", "Sword weapon for Armor Test", armorType, 4, 0, randint(0,100), randint(0,500))
        equips['wand'] = Equipment("Gold Wand", "Wand weapon for Armor Test", armorType + 1, 4, 1, randint(0,100), randint(0,500))

        if raw:
            """Returns new Armor and dict of equipments"""
            return Armor(armorType), equips
        else:
            """Returns full equiped Armor plus other weapon"""
            return Armor(armorType, equips['head'], equips['chest'], equips['back'], equips['pants'], equips['sword']), equips['wand']

    def test_init(self):
        # TODO: Complete Test
        self.fail("Incomplete Test")

    def test_equip(self):
        # TODO: Complete Test
        self.fail("Incomplete Test")

    def test_dequip(self):
        # TODO: Complete Test
        self.fail("Incomplete Test")

    def test_printToFile(self):
        arm, _w = self.setup(False)
        arm.printToFile()
        filename = f"{arm.name}.json"
        self.assertTrue(os.path.exists(filename), "PrintToFile Failed")
        if os.path.exists(filename):
            os.remove(filename)


def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
