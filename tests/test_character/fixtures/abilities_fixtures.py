"""
Description: Pytest fixtures for the character.abilities module
Developer: Jevin Evans
Date: 11/5/2022
"""

from unittest.mock import patch

import pytest

from funclg.character.abilities import Abilities
from funclg.utils.types import ABILITY_TYPES


def ability_ids():
    return [
        "ABILITY-12345-FEDW-67890",
        "ABILITY-12345-HEIJ-67891",
        "ABILITY-12345-HSEH-67892",
        "ABILITY-12345-CMEG-67893",
        "ABILITY-12345-EGJE-67894",
        "ABILITY-12345-OIJE-67895",
        "ABILITY-12345-HEHL-67896",
        "ABILITY-12345-GESG-67897",
    ]


def abilities_gen_mods():
    mods = {}
    for a_type, data in ABILITY_TYPES.items():
        if a_type == "Basic":
            mods[a_type] = {}
        else:
            mods[a_type] = {data["m_type"]: {data["mods"][0]: 50}}
    return mods


@pytest.fixture
def abilities_all_types():
    """Returns a list of all ability types"""

    ability_mods = abilities_gen_mods()

    with patch("funclg.utils.data_mgmt.id_gen", side_effect=ability_ids()):
        all_abilities = []
        for index, a_type in enumerate(ABILITY_TYPES):
            all_abilities.append(
                Abilities(
                    name=f"Ability_{index}",
                    ability_type=a_type,
                    description=f"{a_type} ability",
                    mod=ability_mods[a_type],
                )
            )

        all_abilities.append(
            Abilities(
                name="Ability_Error_NoMod",
                ability_type="Error",
                description="Error ability",
            )
        )
        return all_abilities


@pytest.fixture
def abilities_str_expectation(abilities_all_types):
    ability_strings = []
    for ability in abilities_all_types:
        if ability.mod.adds or ability.mod.mults:
            ability_strings.append(f"{ability.name} ({ability.ability_type}) - {ability.mod}")
        else:
            ability_strings.append(f"{ability.name} ({ability.ability_type})")
    return ability_strings


@pytest.fixture
def abilities_export_expectation(abilities_all_types):
    ability_exports = []
    for ability in abilities_all_types:
        ability_exports.append(
            {
                "name": ability.name,
                "ability_type": ability.ability_type,
                "_target": ability._target,
                "mod": ability.mod.export(),
                "description": ability.description,
                "level": 1,
            }
        )
    return ability_exports


@pytest.fixture
def abilities_detail_expectation(abilities_all_types):
    ability_details = []
    for indent, ability in enumerate(abilities_all_types):
        base = f"""
{' '*indent}{ability.name} [lvl {ability.level}]
{' '*indent}{'-'*(len(ability.name)+7+len(str(ability.level)))}
{' '*indent}Description: {ability.description}
{' '*indent}Ability Type: {ability.ability_type}
{' '*indent}Target: {ability._target.capitalize()}{ability.mod.details(indent+2)}"""
        ability_details.append(base)
    return ability_details
