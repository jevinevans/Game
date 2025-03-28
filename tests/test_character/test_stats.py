"""
Description: Testing the stats classes.
Developer: Jevin Evans
Date: 3.23.2022
Last Update: 10.10.2023
"""

from unittest.mock import patch

import pytest

from funclg.character.modifiers import Modifier
from funclg.character.stats import Stats


@pytest.fixture
def stat_no_mods():
    """Creates a base stat object"""
    return Stats()


@pytest.fixture
def stat_mods():
    """Creates a list of modifiers"""
    return [
        Modifier("Mod_1", {"energy": 50}, {"health": 0.5}),
        Modifier("Mod_2", percentage={"attack": 0.25}),
    ]


@pytest.fixture
def stat_with_mods(stat_mods):
    """Creates a Stats object with attributes and modifiers"""
    return Stats(attributes={"attack": 4, "health": 10, "energy": 5}, modifiers=stat_mods)


@pytest.fixture
def stat_with_mods_export_expectation():
    """Returns the string expectation of the Stats export"""
    return {
        "attributes": {"attack": 4, "health": 10, "energy": 5, "defense": 1},
        "modifiers": {
            "Mod_1": {"base": {"energy": 50}, "percentage": {"health": 0.5}},
            "Mod_2": {"base": {}, "percentage": {"attack": 0.25}},
        },
    }


@pytest.fixture
def stat_with_mods_str_expectation():
    """Returns the string expectation of the Stats __str__ function"""
    return """
Stats
-----
Health: 15.0
Attack: 5.0
Defense: 1
Energy: 55"""


@pytest.fixture
def stat_with_mods_details_expectation():
    expectations = []
    for indent in range(0, 4):
        base = f"""
{' '*indent}Stats [76.0]
{' '*indent}------------
{' '*(indent+2)}Health [10]: 15.0
{' '*(indent+2)}Attack [4]: 5.0
{' '*(indent+2)}Defense [1]: 1
{' '*(indent+2)}Energy [5]: 55"""
        expectations.append(base)
    return expectations


def test_stats_init(stat_no_mods, stat_with_mods):
    """Testing Init Processes"""

    assert stat_no_mods.power == 4

    assert getattr(stat_with_mods, "attack", False)
    assert getattr(stat_with_mods, "health", False)
    assert getattr(stat_with_mods, "energy", False)
    assert stat_with_mods.attack == 4


def test_stats_add_modifier_base_mod(stat_no_mods):
    """Test adding an add mod to a stat"""
    add = Modifier("add_test", {"attack": 53})
    assert stat_no_mods.mods == {}

    stat_no_mods.add_mod(add)
    assert getattr(stat_no_mods, "mods", False) == {add.name: add.get_mods()}
    # assert getattr(base_stat_no_mods, "attack", False) == 53


def test_stats_add_modifier_percentage_mod(stat_no_mods):
    """Test adding a percentage mod to a stat"""
    mult = Modifier("mult_test", percentage={"attack": 53})
    assert stat_no_mods.mods == {}

    stat_no_mods.add_mod(mult)
    assert getattr(stat_no_mods, "mods", False) == {mult.name: mult.get_mods()}


def test_stats_add_modifier_base_and_percentage_mod(stat_no_mods):
    """Test adding add and mult mods to a stat"""
    add = Modifier("add_test", {"attack": 53})
    mult = Modifier("mult_test", percentage={"attack": 53})
    assert stat_no_mods.mods == {}

    stat_no_mods.add_mod(add)
    stat_no_mods.add_mod(mult)

    assert getattr(stat_no_mods, "mods", False) == {
        add.name: add.get_mods(),
        mult.name: mult.get_mods(),
    }


@patch("loguru.logger.error")
def test_stats_add_modifier_duplicate_mod(m_log, stat_no_mods):
    """Test duplicate adding of an add mod to stat. Stat should reject the second"""
    add = Modifier("add_test", {"attack": 53})
    assert stat_no_mods.mods == {}

    stat_no_mods.add_mod(add)
    stat_no_mods.add_mod(add)
    assert getattr(stat_no_mods, "mods", False) == {add.name: add.get_mods()}
    m_log.assert_called_with("Modifier: add_test is not valid for this stat")


def test_stats_remove_stat_success(stat_with_mods, stat_mods):
    assert stat_with_mods.mods != {}
    stat_with_mods.remove_mod("Mod_1")
    mods = stat_mods[1]
    assert stat_with_mods.mods == {mods.name: mods.get_mods()}


@patch("loguru.logger.error")
def test_stats_remove_stat_failure(m_log, stat_with_mods, stat_mods):
    assert stat_with_mods.mods != {}
    stat_with_mods.remove_mod("Mod_3")

    assert stat_with_mods.mods == {
        stat_mods[0].name: stat_mods[0].get_mods(),
        stat_mods[1].name: stat_mods[1].get_mods(),
    }
    m_log.assert_called_with("This stat does not have the 'Mod_3' modifier.")


def test_stats_get_stat_success(stat_with_mods):
    assert stat_with_mods.get_stat("health") == 15


def test_stats_get_stat_failure(stat_with_mods):
    # Validates that only approved stats can be called
    assert stat_with_mods.get_stat("karma") is None


def test_stats_get_stats(stat_with_mods):
    assert stat_with_mods.get_stats() == {
        "attack": 5.0,
        "health": 15.0,
        "energy": 55,
        "defense": 1,
    }


def test_stats_export(stat_with_mods, stat_with_mods_export_expectation):
    assert stat_with_mods.export() == stat_with_mods_export_expectation


def test_stats_str(stat_with_mods, stat_with_mods_str_expectation):
    assert stat_with_mods.__str__() == stat_with_mods_str_expectation


def test_stats_details(stat_with_mods, stat_with_mods_details_expectation):
    for index, expectation in enumerate(stat_with_mods_details_expectation):
        assert stat_with_mods.details(index) == expectation


def test_stats_clear_mods(stat_with_mods):
    assert len(stat_with_mods.mods) == 2

    stat_with_mods.clear_mods()

    assert stat_with_mods.mods == {}
    assert len(stat_with_mods.mods) == 0


def test_stats_levelup(stat_no_mods):
    lvl_stats = Stats(stat_no_mods.copy())

    lvl_stats.level_up()

    for stat in Stats.BASE_ATTRIBUTES:
        assert abs(stat_no_mods.get_stat(stat) - lvl_stats.get_stat(stat)) == 1

    lvl_stats.level_up()
    lvl_stats.level_up()
    lvl_stats.level_up()
    lvl_stats.level_up()

    for stat in Stats.BASE_ATTRIBUTES:
        assert abs(stat_no_mods.get_stat(stat) - lvl_stats.get_stat(stat)) == 5


def test_stats_to_mod(stat_no_mods):
    full_stats = stat_no_mods.get_stats()

    stat_mod = stat_no_mods.to_mod(name="test")

    for stat, value in full_stats.items():
        assert stat_mod.base[stat] == value


def test_stats_copy(stat_with_mods):
    new_stat = stat_with_mods.copy()


def test_stats_comparisons(stat_with_mods, stat_no_mods):
    assert stat_with_mods > stat_no_mods
    assert not stat_with_mods < stat_no_mods
    assert not stat_with_mods <= stat_no_mods
    assert stat_with_mods >= stat_with_mods

    assert stat_with_mods == stat_with_mods
    assert stat_with_mods != stat_no_mods
