#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/15/2021                                                                 #
#   Program: Armor Class Test                                                       #
#   Description: The is a unit test for the armor class and its interations         #
#       with the equipment class.                                                   #
#####################################################################################

import unittest
from core import armor
from utils.types import *


class ArmorTest(unittest.TestCase):
    
    def test_init(self):
        "temp"

    def test_equip(self):
        "temp"

    def test_dequip(self):
        "temp"

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
