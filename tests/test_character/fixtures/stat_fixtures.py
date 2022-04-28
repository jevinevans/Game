from ast import Mod
from sre_parse import State
import pytest

from FUNCLG.character.stats import Stats
from FUNCLG.character.modifiers import Modifier

@pytest.fixture
def base_stat_no_mods():
    return Stats()

def base_mods():
    return [Modifier("Mod_1", {"energy":50}, {"health":.5}), Modifier("Mod_2", mults={"attack":.25})]

@pytest.fixture
def base_stat_with_mods():
    return Stats({"level":30, "attack":4, "health": 10, "energy":5}, base_mods())


@pytest.fixture
def base_stat_export_expectation():
    return {
        "level":30,
        "attack":4,
        "health":10,
        "energy":5,
        "mods":{
            "Mod_1":{
                "adds":{"energy":50},
                "mults":{"health":0.5}
            },
            "Mod_2":{
                "adds":{},
                "mults":{"attack":0.25}
            }
        }
    }