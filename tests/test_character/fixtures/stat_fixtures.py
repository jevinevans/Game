from ast import Mod
from sre_parse import State

import pytest

from funclg.character.modifiers import Modifier
from funclg.character.stats import Stats


@pytest.fixture
def base_stat_no_mods():
    return Stats()


def base_mods():
    return [
        Modifier("Mod_1", {"energy": 50}, {"health": 0.5}),
        Modifier("Mod_2", mults={"attack": 0.25}),
    ]


@pytest.fixture
def base_stat_with_mods():
    return Stats({"level": 30, "attack": 4, "health": 10, "energy": 5}, base_mods())


@pytest.fixture
def base_stat_export_expectation():
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
    return """
 Stats 
-------
Level: 30
Health: 15.0
Energy: 55
Attack: 5.0
Defense: 0"""
