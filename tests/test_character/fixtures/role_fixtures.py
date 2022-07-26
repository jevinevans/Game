from unittest.mock import patch

import pytest

from funclg.character.abilities import Abilities
from funclg.character.roles import Roles


@pytest.fixture
def mage_test_role():

    obj_ids = [
        "ABILITY-12345-FADJ-67890",
        "ABILITY-12345-FADD-67891",
        "ABILITY-12345-FEFS-67892",
        "ABILITY-12345-EODS-67893",
        "ABILITY-12345-FADJ-67890",
        "ABILITY-12345-FADD-67891",
        "ABILITY-12345-FEFS-67892",
        "ABILITY-12345-EODS-67893",
        "ROLES-12345-JFEIOJ-67890",
    ]
    with patch("funclg.utils.data_mgmt.id_gen", side_effect=obj_ids):
        test_damage_types = ["Magic", "Healing", "Buff", "Debuff"]
        example_abilities = []
        for d_type in test_damage_types:
            example_abilities.append(
                Abilities(
                    name=d_type + " Test Ability",
                    damage_type=d_type,
                    effect=15,
                    description=f"Testing {d_type} ability.",
                )
            )

        return Roles(
            name="Mage Class",
            description="Test Mage Class",
            armor_type=1,
            damage_types=test_damage_types,
            abilities=example_abilities,
        )


@pytest.fixture
def mage_export_expectation():
    return {
        "_id": "ROLES-12345-JFEIOJ-67890",
        "name": "Mage Class",
        "description": "Test Mage Class",
        "armor_type": 1,
        "damage_types": ["Magic", "Healing", "Buff", "Debuff"],
        "abilities": [
            {
                "name": "Magic Test Ability",
                "damage_type": "Magic",
                "ability_group": "Damage",
                "effect": -15,
                "description": "Testing Magic ability.",
                "_id": "ABILITY-12345-FADJ-67890",
            },
            {
                "name": "Healing Test Ability",
                "damage_type": "Healing",
                "ability_group": "Boost",
                "effect": 15,
                "description": "Testing Healing ability.",
                "_id": "ABILITY-12345-FADD-67891",
            },
            {
                "name": "Buff Test Ability",
                "damage_type": "Buff",
                "ability_group": "Boost",
                "effect": 15,
                "description": "Testing Buff ability.",
                "_id": "ABILITY-12345-FEFS-67892",
            },
            {
                "name": "Debuff Test Ability",
                "damage_type": "Debuff",
                "ability_group": "Damage",
                "effect": -15,
                "description": "Testing Debuff ability.",
                "_id": "ABILITY-12345-EODS-67893",
            },
        ],
    }


@pytest.fixture
def mage_str_expectation():
    return "Class: Mage Class | Class Type(s): Magic, Healing, Buff, Debuff | Armor Type: Medium | Abilities: 4"


@pytest.fixture
def roles_detail_expectation_with_abilities(mage_test_role):
    role_details = []
    for indent in range(5):
        base = f"""
{' '*indent}Class: {mage_test_role.name}
{' '*indent}-----------------
{' '*indent}Armor Type: Medium
{' '*indent}Description: {mage_test_role.description}
{' '*indent}Role Abilities:
{mage_test_role.abilities[0].details(indent+2)}
{mage_test_role.abilities[1].details(indent+2)}
{mage_test_role.abilities[2].details(indent+2)}
{mage_test_role.abilities[3].details(indent+2)}
"""
        role_details.append(base)
    return role_details


@pytest.fixture
def roles_detail_expectation_no_abilities(mage_test_role):
    indent = 0
    return f"""
{' '*indent}Class: {mage_test_role.name}
{' '*indent}-----------------
{' '*indent}Armor Type: Medium
{' '*indent}Description: {mage_test_role.description}
{' '*indent}Role Abilities:
{' '*(indent+2)}No Abilities"""
