import funclg.utils.types as f_types


# TODO: Check for POSSIBLE BAD TEST
def test_get_ability_effect_type():
    for damage_type, effect_value in f_types.DAMAGE_TYPES.items():
        assert effect_value == f_types.get_ability_effect_type(damage_type)


def test_get_item_type():
    for index, item_type in enumerate(f_types.ITEM_TYPES):
        assert item_type == f_types.get_item_type(index)


def test_get_armor_type():
    for index, armor_type in enumerate(f_types.ARMOR_TYPES):
        assert armor_type == f_types.get_armor_type(index)


def test_get_weapon_type():
    for index, weapon_type in enumerate(f_types.WEAPON_TYPES):
        assert weapon_type == f_types.get_weapon_type(index)


def test_get_item_description():
    # Test get item path for no armor
    assert f_types.get_item_description(item_type=2, armor_type=-1)

    # Test get item description path for weapon no weapon type
    assert f_types.get_item_description(item_type=4)

    # Test get item description path with weapon
    assert f_types.get_item_description(item_type=4, weapon_type=2)
