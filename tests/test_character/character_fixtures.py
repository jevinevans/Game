import pytest


# Local Imports
from FUNCLG.character.modifiers import Modifier

# Modifier Fixtures
@pytest.fixture
def add_mods():
    return {
        "valid": {"attack": 43, "defense": -20},
        "invalid": {"attack": -34, "error": -32, "energy": 20,},
    }


@pytest.fixture
def mult_mods():
    return {
        "valid": {"health": 0.33, "energy": -0.6},
        "invalid": {"health": -0.10, "error": 23, "defense": 0.4,},
    }


@pytest.fixture
def modifier_str_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base =f"""{' '*indent}Modifier: Output Test:
{' '*(indent+2)}Attack
  {' '*(indent+2)}+43\n
{' '*(indent+2)}Defense
  {' '*(indent+2)}-20\n
{' '*(indent+2)}Health
  {' '*(indent+2)}+33.0%\n
{' '*(indent+2)}Energy
  {' '*(indent+2)}-60.0%\n
"""
        expectations.append(base)
    return expectations

# Stat Fixtures

# Equipment Fixtures

# Abilities Fixtures

# Armor Fixtures

# Role Fixtures

# Character Fixtures
