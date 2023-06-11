"""
Description: This is to unit test the FUNCLG character manager module
Developer: Jevin Evans
Date: 02.20.2023
"""

from unittest.mock import patch

import pytest

import funclg.managers.character_manager as char_man


@pytest.fixture
def test_character_mage():
    return {
        "name": "Test Char Mage",
        "armor_type": 1,
        "inventory": [],
        "armor": {
            "armor_type": 1,
            "stat": {
                "level": None,
                "health": 20,
                "energy": 20,
                "attack": 20,
                "defense": 20,
                "mods": {
                    "Basic Mage Tunic": {
                        "adds": {
                            "health": 100
                        },
                        "mults": {
                            "health": 0.45
                        }
                    },
                    "Calins Wand": {
                        "adds": {
                            "attack": 337
                        },
                        "mults": {
                            "energy": 1
                        }
                    }
                }
            },
            "head": None,
            "chest": {
                "name": "Basic Mage Tunic",
                "description": "Armor used by beginner mages",
                "item_type": 1,
                "armor_type": 1,
                "mod": {
                    "adds": {
                        "health": 100
                    },
                    "mults": {
                        "health": 0.45
                    }
                },
                "_id": "ARMOR-16809-BCWSVN-76675"
            },
            "back": None,
            "pants": None,
            "weapon": {
                "weapon_type": "Wand",
                "name": "Calins Wand",
                "description": "The original wand of Calin",
                "item_type": 4,
                "armor_type": 1,
                "mod": {
                    "adds": {
                        "attack": 337
                    },
                    "mults": {
                        "energy": 1
                    }
                },
                "_id": "WEAPON-16645-ACIGL-01214"
            }
        },"role": {
            "name": "Mage",
            "description": "Magic user",
            "armor_type": 1,
            "ability_types": [
                "Magic",
                "Buff",
                "Debuff",
                "Restore"
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
            "_id": "ROLES-16695-ZBLWXR-20642"
        },
        "_id": "CHARS-16809-QKLNBT-73916"
    }

@patch("funclg.utils.data_mgmt.update_data")
def test_char_manager_update_data(m_db, test_character_mage):
    char_man.CHARACTER_DATA['data'] = {}
    char_man.CHARACTER_DATA['data'][test_character_mage['_id']] = test_character_mage
    char_man.CHARACTER_DATA['objects'] = {}

    char_man.update_data()
    
    assert len(char_man.CHARACTER_DATA['data']) == len(char_man.CHARACTER_DATA['objects'])
    assert m_db.called_once

@patch("funclg.utils.data_mgmt.update_data")
def test_char_manager_export_data(m_db, test_character_mage):
    _test_char_mage = test_character_mage.copy()
    _test_char_mage = char_man._update_char_role(test_character_mage, _test_char_mage)
    _test_char_mage = char_man._update_char_armor(test_character_mage, _test_char_mage)
    char_man.CHARACTER_DATA['objects'][_test_char_mage['_id']] = char_man.Character(**_test_char_mage)
    char_man.CHARACTER_DATA['data'] = {}

    char_man.export_data()

    assert len(char_man.CHARACTER_DATA['data']) == len(char_man.CHARACTER_DATA['objects'])
    assert _test_char_mage["_id"] in char_man.CHARACTER_DATA['data']
    assert m_db.called_once


@patch("funclg.managers.character_manager.logger")
@patch("funclg.managers.character_manager.char_manager_choice_selection")
def test_char_manager_select_character(m_chr_sel, m_log, test_character_mage):
    # No Charater Data
    char_man.CHARACTER_DATA['data'] = {}
    assert char_man.select_character() is None
    assert m_log.warning.called

    # Character Data Exists
    char_man.CHARACTER_DATA['data'][test_character_mage['_id']] = test_character_mage
    m_chr_sel.return_value = test_character_mage["_id"]
    assert char_man.select_character() == test_character_mage['_id']

@patch("builtins.print")
@patch("funclg.managers.character_manager.logger")
@patch("funclg.managers.character_manager.select_character")
def test_char_manager_show_character(m_sel, m_log, m_print, test_character_mage):
    # No Data
    m_sel.return_value = None
    char_man.show_character()
    assert m_log.warning.called

    # Return Test Value
    m_sel.return_value = test_character_mage['_id']
    _test_char_mage = test_character_mage.copy()
    _test_char_mage = char_man._update_char_role(test_character_mage, _test_char_mage)
    _test_char_mage = char_man._update_char_armor(test_character_mage, _test_char_mage)
    char_man.CHARACTER_DATA['objects'][_test_char_mage['_id']] = char_man.Character(**_test_char_mage)

    char_man.show_character()
    assert m_print.called_with(char_man.CHARACTER_DATA['objects'][test_character_mage['_id']].details())


# @patch("builtins.print")
# @patch("funclg.managers.character_manager.logger")
# @patch("funclg.managers.character_manager.yes_no_validation")
# @patch("funclg.managers.character_manager.update_data")
# @patch("funclg.managers.character_manager.select_character")
# def test_roles_manager_delete_role(m_sel, m_update, m_yn, m_log, m_print, test_character_mage):
#     # Yes Delete
    

#     # No Delete