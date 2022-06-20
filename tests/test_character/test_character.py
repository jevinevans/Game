"""Unittest for Character Class"""

from unittest.mock import patch

import pytest

from funclg.character.character import Character


def test_character_init_no_armor_no_role():
    t_char = Character("Init No Role/Armor", 0)
    assert t_char.name == "Init No Role/Armor"
    assert t_char.armor != None
    assert t_char.armor.armor_type == 0
    assert t_char.role != None
    assert t_char.role.name == "Basic"
