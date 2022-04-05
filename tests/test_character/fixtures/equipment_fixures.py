"""
Equipment Fixtures for testing
"""

import pytest
from FUNCLG.character.equipment import BodyEquipment, WeaponEquipment
from FUNCLG.utils.types import ITEM_TYPES, ARMOR_TYPES, WEAPON_TYPES, MODIFIER_TYPES


@pytest.fixture
def bodyequipment_mods():
    item_mods = {}
    for index, item_type in enumerate(ITEM_TYPES):
        endex = -1* index%len(ITEM_TYPES)
        item_mods[item_type+"_mods"] = {
            "adds":{
                MODIFIER_TYPES[index]: 50
            }, 
            "mults":{
                MODIFIER_TYPES[endex]: 0.10
            }
        }

@pytest.fixture
def bodyequipment_all_types():
    # For each armor type creates an item of that type
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        for a_index, armor_type in enumerate(ARMOR_TYPES):
            # NO_Mods
            equipment[item_type+"_"+armor_type] = BodyEquipment(name=item_type+"_"+armor_type, description=f"{armor_type} {item_type}", armor_type=a_index, item_type=i_index)
    return equipment

@pytest.fixture
def bodyequipment_all_items_mods(bodyequipment_mods):
    equipment = {}
    for i_index, item_type in enumerate(ITEM_TYPES[:4]):
        equipment[item_type+"_mod"] = BodyEquipment(name=item_type+"_mod", description=f"Medium {item_type} with mods", armor_type=1, item_type=i_index, modifiers=bodyequipment_mods[item_type+"_mods"])
    return equipment

@pytest.fixture
def weaponequipment_all_types():
    # For each armor type, creates a weapon of that type
    weapons = {}
    for w_index, weapon_type in enumerate(WEAPON_TYPES):
        for a_index, armor_type in enumerate(ARMOR_TYPES):
            weapons[weapon_type+"_"+armor_type] = WeaponEquipment(name=weapon_type+"_"+armor_type, description=f"{armor_type} {weapon_type}", weapon_type=w_index, armor_type=a_index)
    return weapons
