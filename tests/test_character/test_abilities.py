"""
Programmer: Jevin Evans
Date: 1.8.2022
Description: The is a unit test for the abilties class.
"""

from unittest.mock import patch

from funclg.character.abilities import Abilities
from funclg.utils.types import DAMAGE_TYPES

from .fixtures.abilities_fixtures import (
    abilities_all_types,
    abilities_detail_expectation,
    abilities_export_expectation,
    abilities_str_expectation,
)


def test_abilities_init(abilities_all_types):
    # Testing proper effect type
    for ability in abilities_all_types:
        if DAMAGE_TYPES.get(ability.damage_type, None)[1] > 0:
            assert ability.effect > 0
        elif DAMAGE_TYPES.get(ability.damage_type, None)[1] < 0:
            assert ability.effect < 0
        elif DAMAGE_TYPES.get(ability.damage_type, None)[1] == 0:
            assert ability.effect == 0


def test_abilities_incorrect_damage_type():
    """Tests for incorrect ability types"""
    t1 = Abilities("Error Type", "Error", -23, "Random string")

    assert t1.damage_type == "None"
    assert t1.effect == 0


def test_abilities_str(abilities_all_types, abilities_str_expectation):
    for index, ability in enumerate(abilities_all_types):
        assert ability.__str__() == abilities_str_expectation[index]


def test_abilities_details(abilities_all_types, abilities_detail_expectation):
    for index, ability in enumerate(abilities_all_types):
        assert ability.details(index) == abilities_detail_expectation[index]


def test_abilities_export(abilities_all_types, abilities_export_expectation):
    for index, ability in enumerate(abilities_all_types):
        assert ability.export() == abilities_export_expectation[index]


@patch("builtins.open")
@patch("json.dump")
def test_abilities_print_to_file(m_dump, m_open, abilities_all_types):
    test_ability = abilities_all_types[0]
    test_ability.print_to_file()

    m_open.assert_called_once_with(test_ability.name + ".json", "w", encoding="utf-8")
    m_dump.assert_called_with(test_ability.export(), m_open.return_value.__enter__())


def test_abilities_copy(abilities_all_types):
    repair_1 = abilities_all_types[0]
    repair_2 = repair_1.copy()

    # Test object difference
    assert repair_1 != repair_2
    assert id(repair_1) != id(repair_2)

    # Test Information is the same
    assert repair_1.name == repair_2.name
    assert repair_1.damage_type == repair_2.damage_type
    assert repair_1.ability_group == repair_2.ability_group
    assert repair_1.effect == repair_2.effect
    assert repair_1.description == repair_2.description
