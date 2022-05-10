"""
Programmer: Jevin Evans
Date: 3.23.2022
Description: Testing the stats classes.
Last Update: 3.23.2022
"""

from audioop import mul
from email.mime import base
from random import randint, random
from unittest.mock import patch

import pytest

from funclg.character.modifiers import Modifier
from funclg.character.stats import Stats

from .fixtures.stat_fixtures import (
    base_stat_no_mods,
    base_stat_with_mods,
    base_mods,
    base_stat_export_expectation
)

def test_base_stat_init(base_stat_no_mods, base_stat_with_mods):
    """Testing Init Processes"""
    assert base_stat_no_mods.level == 0
    assert base_stat_with_mods.level == 30
    assert getattr(base_stat_with_mods, "attack", False)
    assert getattr(base_stat_with_mods, "health", False)
    assert getattr(base_stat_with_mods, "energy", False)
    assert base_stat_with_mods.attack == 4


def test_base_stat_add_modifier_adds_mod(base_stat_no_mods):
    """Test adding an add mod to a stat"""
    add = Modifier("add_test", {"attack":53})
    assert base_stat_no_mods.mods == {}

    base_stat_no_mods.add_mod(add)
    assert getattr(base_stat_no_mods, "mods", False) == {add.name:add.get_mods()}
    # assert getattr(base_stat_no_mods, "attack", False) == 53

def test_base_stat_add_modifier_mults_mod(base_stat_no_mods):
    """Test adding a mults mod to a stat"""
    mult = Modifier("mult_test", mults={"attack":53})
    assert base_stat_no_mods.mods == {}

    base_stat_no_mods.add_mod(mult)
    assert getattr(base_stat_no_mods, "mods", False) == {mult.name:mult.get_mods()}

def test_base_stat_add_modifier_adds_and_mults_mod(base_stat_no_mods):
    """Test adding add and mult mods to a stat"""
    add = Modifier("add_test", {"attack":53})
    mult = Modifier("mult_test", mults={"attack":53})
    assert base_stat_no_mods.mods == {}

    base_stat_no_mods.add_mod(add)
    base_stat_no_mods.add_mod(mult)

    assert getattr(base_stat_no_mods, "mods", False) == {add.name:add.get_mods(), mult.name:mult.get_mods()}

@patch("loguru.logger.warning")
def test_base_stat_add_modifier_duplicate_mod(m_log, base_stat_no_mods):
    """Test duplicate adding of an add mod to stat. Stat should reject the second"""
    add = Modifier("add_test", {"attack":53})
    assert base_stat_no_mods.mods == {}

    base_stat_no_mods.add_mod(add)
    base_stat_no_mods.add_mod(add)
    assert getattr(base_stat_no_mods, "mods", False) == {add.name:add.get_mods()}
    assert m_log.called_with("Modifier: add_test is not valid for this stat")


def test_base_stat_remove_stat_success(base_stat_with_mods):
    assert base_stat_with_mods.mods != {}
    base_stat_with_mods.remove_mod("Mod_1")
    mods = base_mods()[1]
    assert base_stat_with_mods.mods == {mods.name:mods.get_mods()}

@patch("loguru.logger.error")
def test_base_stat_remove_stat_failure(m_log, base_stat_with_mods):
    assert base_stat_with_mods.mods != {}
    base_stat_with_mods.remove_mod("Mod_3")
    mods = base_mods()

    assert base_stat_with_mods.mods == {mods[0].name:mods[0].get_mods(), mods[1].name:mods[1].get_mods()}
    assert m_log.called_with("This stat does not have the 'Mod_1' modifier.")


def test_base_stat_get_stat_success(base_stat_with_mods):
    assert base_stat_with_mods.get_stat("health") == 15

def test_base_stat_get_stat_failure(base_stat_with_mods):
    assert base_stat_with_mods.get_stat("karma") == None

def test_base_stat_get_stats(base_stat_with_mods):
    assert base_stat_with_mods.get_stats() == {"level":30, "attack":5, "health":15, "energy":55, "defense":1}

def test_base_stat_export(base_stat_with_mods, base_stat_export_expectation):
    assert base_stat_with_mods.export() == base_stat_export_expectation