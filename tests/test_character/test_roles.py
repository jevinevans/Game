"""Unittest for Roles Class"""

from unittest.mock import patch

import pytest

from funclg.character.abilities import Abilities
from funclg.character.roles import Roles

from .fixtures.roles_fixtures import (
    mage_export_expectation,
    mage_str_expectation,
    mage_test_role,
    roles_detail_expectation_no_abilities,
    roles_detail_expectation_with_abilities,
)


@patch("builtins.open")
@patch("json.dump")
def test_roles_print_to_file(m_dump, m_open, mage_test_role):
    mage_test_role.print_to_file()

    m_open.assert_called_once_with(mage_test_role.name + ".json", "w", encoding="utf-8")
    m_dump.assert_called_with(mage_test_role.export(), m_open.return_value.__enter__())


def test_roles_export(mage_test_role, mage_export_expectation):
    assert mage_export_expectation == mage_test_role.export()


def test_roles_str(mage_test_role, mage_str_expectation):
    assert mage_str_expectation == mage_test_role.__str__()


def test_roles_add_ability_valid_power(mage_test_role):
    healing_2 = Abilities(
        name="Healing 2",
        ability_type="Restore",
        mod={"adds": {"health": 50}},
        description="New healing ability",
    )

    assert len(mage_test_role.abilities) == 4
    assert mage_test_role.add_ability(healing_2) is True
    assert len(mage_test_role.abilities) == 5

    char_power = mage_test_role.abilities[-1]
    assert char_power.name == healing_2.name
    assert char_power.ability_type == healing_2.ability_type
    assert char_power.mod.export() == healing_2.mod.export()
    assert char_power.description == healing_2.description


def test_roles_add_ability_valid_power_max_reached(mage_test_role):
    buff = Abilities(
        name="Buff 2",
        ability_type="Buff",
        mod={"mults": {"defense": 0.5}},
        description="New Buff ability",
    )
    healing_2 = Abilities(
        name="Healing 2",
        ability_type="Restore",
        mod={"adds": {"health": 50}},
        description="New healing ability",
    )

    assert len(mage_test_role.abilities) == 4
    assert mage_test_role.add_ability(healing_2) is True
    assert len(mage_test_role.abilities) == 5

    assert mage_test_role.add_ability(buff) is False
    assert len(mage_test_role.abilities) == 5
    assert mage_test_role.abilities[-1].name == healing_2.name


def test_roles_add_ability_invalid_power(mage_test_role):
    stomp = Abilities(
        name="Stomp",
        ability_type="Physical",
        mod={"adds": {"attack": 50}},
        description="stomp ability",
    )

    assert len(mage_test_role.abilities) == 4
    assert mage_test_role.add_ability(stomp) is False
    assert len(mage_test_role.abilities) == 4


def test_roles_get_ability(mage_test_role):
    test_damage_types = ["Magic", "Restore", "Buff", "Debuff"]
    for ability in range(len(mage_test_role.abilities)):
        assert mage_test_role.get_ability(ability).ability_type == test_damage_types[ability]


@patch("loguru.logger.warning")
def test_role_get_ability_out_of_range(m_log, mage_test_role):
    for index in range(4, 10):
        assert mage_test_role.get_ability(index) is None
        assert m_log.called
        assert m_log.called_with("There is no power in this slot.")


def test_role_remove_ability_valid(mage_test_role):
    "testing removing the healing ability slot 1"
    assert mage_test_role.remove_ability(1) is True
    assert mage_test_role.get_ability(1).name == "Buff Test Ability"


def test_role_remove_ability_invalid(mage_test_role):
    "testing removing the healing ability slot 1"
    assert mage_test_role.remove_ability(5) is False
    assert mage_test_role.get_ability(1).name == "Restore Test Ability"


def test_role_details_no_abilities(roles_detail_expectation_no_abilities):
    mage = Roles(
        name="Mage Class",
        description="Test Mage Class",
        armor_type=1,
        ability_types=["Magic", "Restore", "Buff", "Debuff"],
    )
    assert roles_detail_expectation_no_abilities == mage.details()


def test_role_details_with_abilities(roles_detail_expectation_with_abilities, mage_test_role):
    for indent in range(5):
        assert roles_detail_expectation_with_abilities[indent] == mage_test_role.details(indent)


def test_roles_copy(mage_test_role):
    copy_test = mage_test_role.copy()

    assert copy_test.name == mage_test_role.name
    assert copy_test.id == mage_test_role.id

    assert copy_test != mage_test_role
    assert id(copy_test) != id(mage_test_role)
