"""
Description: This module is to unit test the funclg.managers.roles_manager module
Developer: Jevin Evans
Date: 11/12/2022
"""

from unittest.mock import patch
import pytest
import funclg.managers.roles_manager as role_man

@pytest.fixture
def test_mage():
    return {
        "name": "Mage",
        "description": "Wielders of magic",
        "armor_type": 1,
        "ability_types": [
            "Magic",
            "Restore",
            "Buff",
            "Debuff"
        ],
        "abilities": [{
                "name": "Fireball",
                "description": "Throws a fireball at target",
                "ability_type": "Magic",
                "_target": "enemy",
                "mod": {
                    "adds": {
                        "defense": -446
                    },
                    "mults": {}
                },
                "_id": "ABILITY-16650-OKNG-98180"
            },
            {
                "name": "Heal",
                "description": "Heals the users mod",
                "ability_type": "Restore",
                "_target": "self",
                "mod": {
                    "adds": {},
                    "mults": {
                        "energy": 0.45
                    }
                },
                "_id": "ABILITY-16650-DOTD-98286"
            },
            {
                "name": "Empower",
                "description": "Strengthens player",
                "ability_type": "Buff",
                "_target": "self",
                "mod": {
                    "adds": {},
                    "mults": {
                        "defense": 0.98
                    }
                },
                "_id": "ABILITY-16650-DXUF-98274"
            },
            {
                "name": "Weaken",
                "description": "Weakens an enemy",
                "ability_type": "Debuff",
                "_target": "enemy",
                "mod": {
                    "adds": {},
                    "mults": {
                        "defense": -0.83
                    }
                },
                "_id": "ABILITY-16660-TXKX-31305"
            }
        ],
        "_id": "ROLES-16683-UAJMFU-16064"
    }

def test_no_abilities():
    return {
        "name": "Mage",
        "description": "Wielders of magic",
        "armor_type": 1,
        "ability_types": [
            "Magic",
            "Restore",
            "Buff",
            "Debuff"
        ],
        "abilities": [{
                "name": "Fireball",
                "description": "Throws a fireball at target",
                "ability_type": "Magic",
                "_target": "enemy",
                "mod": {
                    "adds": {
                        "defense": -446
                    },
                    "mults": {}
                },
                "_id": "ABILITY-16650-OKNG-98180"
            },
            {
                "name": "Heal",
                "description": "Heals the users mod",
                "ability_type": "Restore",
                "_target": "self",
                "mod": {
                    "adds": {},
                    "mults": {
                        "energy": 0.45
                    }
                },
                "_id": "ABILITY-16650-DOTD-98286"
            },
            {
                "name": "Empower",
                "description": "Strengthens player",
                "ability_type": "Buff",
                "_target": "self",
                "mod": {
                    "adds": {},
                    "mults": {
                        "defense": 0.98
                    }
                },
                "_id": "ABILITY-16650-DXUF-98274"
            },
            {
                "name": "Weaken",
                "description": "Weakens an enemy",
                "ability_type": "Debuff",
                "_target": "enemy",
                "mod": {
                    "adds": {},
                    "mults": {
                        "defense": -0.83
                    }
                },
                "_id": "ABILITY-16660-TXKX-31305"
            }
        ],
        "_id": "ROLES-16683-UAJMFU-16064"
    }