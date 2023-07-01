"""
Description: Pytest fixtures for the character.stats module
Developer: Jevin Evans
Date: 11/5/2022
"""

import pytest

from funclg.character.modifiers import Modifier
from funclg.character.stats import Stats


@pytest.fixture
def base_stat_no_mods():
    """Creates a base stat object"""
    return Stats()


def base_mods():
    """Creates a list of modifiers"""
    return [
        Modifier("Mod_1", {"energy": 50}, {"health": 0.5}),
        Modifier("Mod_2", mults={"attack": 0.25}),
    ]


@pytest.fixture
def base_stat_with_mods():
    """Creates a Stats object with attributes and modifiers"""
    return Stats({"level": 30, "attack": 4, "health": 10, "energy": 5}, base_mods())


@pytest.fixture
def base_stat_export_expectation():
    """Returns the string expectation of the Stats export"""
    return {
        "level": 30,
        "attack": 4,
        "health": 10,
        "energy": 5,
        "defense": 0,
        "mods": {
            "Mod_1": {"adds": {"energy": 50}, "mults": {"health": 0.5}},
            "Mod_2": {"adds": {}, "mults": {"attack": 0.25}},
        },
    }


@pytest.fixture
def base_stat_str_expectation():
    """Returns the string expectation of the Stats __str__ function"""
    return """
Stats
-----
Level: 30
Health: 15.0
Energy: 55
Attack: 5.0
Defense: 0"""
