"""
Programmer: Jevin Evans
Date: 1.8.2022
Description: The is a unit test for the abilties class.
"""

from unittest.mock import patch

from funclg.character.abilities import Abilities

from .fixtures.abilities_fixtures import (
    abilities_all_types,
    abilities_detail_expectation,
    abilities_export_expectation,
    abilities_gen_mods,
    abilities_str_expectation,
    ability_ids,
)


def test_abilities_init(abilities_all_types):

    for ability in abilities_all_types:
        if ability.ability_type == "None":
            assert ability.mod.adds == {}
            assert ability.mod.mults == {}
        else:
            assert ability.mod.adds != {"adds": {}, "mults": {}}
            assert ability.mod.mults != {"adds": {}, "mults": {}}

        assert ability.id.startswith("ABILITY")

    # Test incompatable
    test_ability = Abilities(
        name="Test",
        ability_type="Magic",
        description="Test incompatable mod",
        mod={"mults": {"defense": 0.22}},
    )

    assert test_ability.mod.export() == {"adds": {"health": 1}, "mults": {}}

    # Test negativce start
    test_ability = Abilities(
        name="Test",
        ability_type="Magic",
        description="Test incompatable mod",
        mod={"adds": {"defense": -0.22}},
    )

    assert test_ability.mod.export() == {"adds": {"defense": -0.22}, "mults": {}}


def test_abilities_str(abilities_all_types, abilities_str_expectation):
    for index, ability in enumerate(abilities_all_types):
        assert ability.__str__() == abilities_str_expectation[index]


def test_abilities_details(abilities_all_types, abilities_detail_expectation):
    for index, ability in enumerate(abilities_all_types):
        assert ability.details(index) == abilities_detail_expectation[index]


def test_abilities_export(abilities_all_types, abilities_export_expectation):
    test_ids = ability_ids()
    for index, ability in enumerate(abilities_all_types):
        abilities_export_expectation[index]["_id"] = test_ids[index]
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
    assert repair_1.id == repair_2.id
    assert repair_1.ability_type == repair_2.ability_type
    assert repair_1.description == repair_2.description
    assert repair_1.mod.export() == repair_2.mod.export()
