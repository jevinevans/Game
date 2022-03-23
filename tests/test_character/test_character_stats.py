"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the stats classes.
Last Update: 3.23.2022
"""

import unittest
from random import randint, random

from FUNCLG.character.modifiers import Modifier
from FUNCLG.character.stats import Stats


class StatsTest(unittest.TestCase):
    def test_stats_init(self):
        stat_1 = Stats(
            health=randint(1, 100),
            energy=randint(1, 100),
            attack=randint(0, 100),
            defense=randint(1, 100),
        )
        print(stat_1)
