import pytest

from FUNCLG.character.abilities import Abilities
from FUNCLG.utils.types import DAMAGE_TYPES

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
