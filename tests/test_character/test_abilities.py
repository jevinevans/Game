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
        if ability.ability_type == "Basic":
            assert ability.mod.base == {}
            assert ability.mod.percentage == {}
        else:
            assert ability.mod.base != {"base": {}, "percentage": {}}
            assert ability.mod.percentage != {"base": {}, "percentage": {}}

        assert ability.id.startswith("ABILITY")

    # Test incompatable ability and mod type: Magic - base and provided a percetage mod
    test_ability_1 = Abilities(
        name="Test",
        ability_type="Magic",
        description="Test incompatable mod",
        mod={"percentage": {"defense": 0.22}},
    )

    assert test_ability_1.mod.export() == {"base": {"health": 1}, "percentage": {}}

    # Test negative start
    test_ability_2 = Abilities(
        name="Test",
        ability_type="Magic",
        description="Test incompatable mod",
        mod={"base": {"defense": -0.22}},
    )

    assert test_ability_2.mod.export() == {"base": {"defense": -0.22}, "percentage": {}}

    # Test incompatable
    test_ability = Abilities(
        name="Test",
        ability_type="Magic",
        description="Test incompatable mod",
        modifier={"mults": {"defense": 0.22}},
    )
    print(test_ability.mod)
    assert test_ability.mod.export() == {"adds": {"health": 1}, "mults": {}}


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


def test_abilities_copy(abilities_all_types):
    repair_1 = abilities_all_types[0]
    repair_2 = repair_1.copy()

    print(abilities_gen_mods())
    print(abilities_all_types[0])

    # Test object difference
    assert repair_1 != repair_2
    assert id(repair_1) != id(repair_2)

    # Test Information is the same
    assert repair_1.name == repair_2.name
    assert repair_1.id == repair_2.id
    assert repair_1.ability_type == repair_2.ability_type
    assert repair_1.description == repair_2.description
    assert repair_1.mod.export() == repair_2.mod.export()


def test_ability_level_up(abilities_all_types):
    ability = abilities_all_types[0]
    ability_lvl = ability.copy()

    assert ability.id == ability_lvl.id

    ability_lvl.level_up()

    for add in ability.mod.base:
        assert abs(ability.mod.base[add] - ability_lvl.mod.base[add]) == 1
    for mult in ability.mod.percentage:
        assert (
            round(abs(ability.mod.percentage[mult] - ability_lvl.mod.percentage[mult]), 2) == 0.01
        )
