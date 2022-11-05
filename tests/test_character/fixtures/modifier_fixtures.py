"""
Description: Pytest fixtures for the character.modifier module
Developer: Jevin Evans
Date: 11/5/2022
"""

import pytest


# Modifier Fixtures
@pytest.fixture
def add_mods():
    return {
        "valid": {"attack": 43, "defense": -20},
        "invalid": {
            "attack": -34,
            "error": -32,
            "energy": 20,
        },
    }


@pytest.fixture
def mult_mods():
    return {
        "valid": {"health": 0.33, "energy": -0.6},
        "invalid": {
            "health": -0.10,
            "error": 23,
            "defense": 0.4,
        },
    }


@pytest.fixture
def new_add_modifier():
    return {"health": 34, "defense": 60}


@pytest.fixture
def new_mult_modifier():
    return {"energy": 0.56, "attack": 0.25}


@pytest.fixture
def modifier_get_expectation(add_mods, mult_mods):
    return {"adds": add_mods["valid"], "mults": mult_mods["valid"]}


@pytest.fixture
def modifier_export_expectation(add_mods, mult_mods):
    return {
        "adds": add_mods["valid"],
        "mults": mult_mods["valid"],
    }


@pytest.fixture
def modifier_str_expectation():
    return "Attack +43, Defense -20, Health +33.0%, Energy -60.0%"


@pytest.fixture
def modifier_details_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base = f"""
{' '*(indent)}Attack: +43
{' '*(indent)}Defense: -20
{' '*(indent)}Health: +33.0%
{' '*(indent)}Energy: -60.0%
"""
        expectations.append(base)
    return expectations
