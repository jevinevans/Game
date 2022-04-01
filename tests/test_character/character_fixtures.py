from string import ascii_letters, digits

import pytest

from FUNCLG.character.abilities import Abilities

# from unittest.mock import patch, call
# Local Imports
from FUNCLG.character.modifiers import Modifier
from FUNCLG.utils.types import DAMAGE_TYPES

# from random import randint, choice


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
        "name": "Test Export",
        "adds": add_mods["valid"],
        "mults": mult_mods["valid"],
    }


@pytest.fixture
def modifier_str_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base = f"""{' '*indent}Modifier: Output Test:
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
@pytest.fixture
def abilities_all_types():
    all_abilities = []
    for index, d_type in enumerate(DAMAGE_TYPES):
        all_abilities.append(
            Abilities(
                name=f"Ability_{index}",
                damage_type=d_type,
                effect=50,
                description=f"{d_type} ability",
            )
        )

    all_abilities.append(
        Abilities(
            name=f"Ability_{len(all_abilities)}",
            damage_type="Error",
            effect=50,
            description=f"{d_type} ability",
        )
    )
    return all_abilities


@pytest.fixture
def abilities_str_expectation(abilities_all_types):
    ability_strings = []
    for ability in abilities_all_types:
        ability_strings.append(f"{ability.name} ({ability.damage_type}): {ability.effect}")
    return ability_strings


@pytest.fixture
def abilities_export_expectation(abilities_all_types):
    ability_exports = []
    for ability in abilities_all_types:
        ability_exports.append(
            {
                "name": ability.name,
                "damage_type": ability.damage_type,
                "ability_group": ability.ability_group,
                "effect": ability.effect,
                "description": ability.description,
            }
        )
    return ability_exports


@pytest.fixture
def abilities_detail_expectation(abilities_all_types):
    ability_details = []
    for indent, ability in enumerate(abilities_all_types):
        base = f"""
{' '*indent}{ability.name}
{' '*indent}{'-'*len(ability.name)}
{' '*indent}Description: {ability.description}
{' '*indent}Type: {ability.damage_type} ({ability.ability_group})
{' '*indent}Effect: {ability.effect}"""
        ability_details.append(base)
    return ability_details


# Armor Fixtures

# Role Fixtures

# Character Fixtures

# Helper Function

# def randomName(length=7):
#     return ''.join(choice(ascii_letters+digits) for _ in range(length))
