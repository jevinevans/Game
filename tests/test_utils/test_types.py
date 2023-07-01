"""
Description: Testing of the utils types module
Developer: Jevin Evans
Date: 11/5/2022
"""

import funclg.utils.types as f_types


def test_get_item_type():
    """Test get item function for all item types"""
    for index, item_type in enumerate(f_types.ITEM_TYPES):
        assert item_type == f_types.get_item_type(index)


def test_get_armor_type():
    """Test get armor function for all armor types"""
    for index, armor_type in enumerate(f_types.ARMOR_TYPES):
        assert armor_type == f_types.get_armor_type(index)


def test_get_item_description():
    "Test get item description for weapons, and armors of different types"
    # Test get item path for no armor
    assert f_types.get_item_description(item_type=2, armor_type=-1)

    # Test get item description path for weapon no weapon type
    assert f_types.get_item_description(item_type=4)

    # Test get item description path with weapon
    assert f_types.get_item_description(item_type=4, weapon_type="Knief")
