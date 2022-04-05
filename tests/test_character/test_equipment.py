"""
Programmer: Jevin Evans
Date: 7.15.2021
Description: The is a unit test for the equipment class.
"""


import os
import unittest
import pytest
from random import randint

from FUNCLG.character.equipment import BodyEquipment, WeaponEquipment
from FUNCLG.character.modifiers import Modifier
from FUNCLG.utils.types import WEAPON_TYPES
from .fixtures.equipment_fixures import (
    bodyequipment_all_items_mods,
    bodyequipment_all_types,
    bodyequipment_mods,
    weaponequipment_all_types,
    equipment_str_expectation,
    bodyequipment_details_expectation,
)

BODY_ITEM_TYPE = randint(0, 3)
BODY_ARMOR_TYPE = randint(0, 2)

# =========================== #
# Testing Equipment Functions #
# =========================== #
def test_equipment_str(weaponequipment_all_types, bodyequipment_all_types, equipment_str_expectation):
    # Test Body Equipment 
    for name, body in bodyequipment_all_types.items():
        assert body.__str__() == equipment_str_expectation[name]

    # Test weapon Equipment 
    for name, weapon in weaponequipment_all_types.items():
        assert weapon.__str__() == equipment_str_expectation[name]

# ================================ #
# Testing Body Equipment Functions #
# ================================ #
def test_bodyequipment_init(bodyequipment_mods):
    # Test Body Equipment
    body = BodyEquipment("Init Test", None, "Testing Initialization", 0, 0)
    assert body.mods.name == "Init Test"
    assert body.mods.adds == {}
    assert body.mods.mults == {}
    
    # Test Modded Equipment
    mod_body = BodyEquipment("Init Mod Test", bodyequipment_mods['Back_mods'], "Testing modded  init", 2, 2)
    assert mod_body.mods.name == "Init Mod Test"
    assert mod_body.mods.adds == bodyequipment_mods['Back_mods']['adds']
    assert mod_body.mods.mults == bodyequipment_mods['Back_mods']['mults']

def test_bodyequipment_get_mods(bodyequipment_mods, bodyequipment_all_items_mods):
    for key, body in bodyequipment_all_items_mods.items():
        assert bodyequipment_mods[key] == body.get_mods()


def test_bodyequipment_copy(bodyequipment_all_items_mods):
    first_key = list(bodyequipment_all_items_mods.keys())[0]
    body_item = bodyequipment_all_items_mods[first_key].copy()
    new_item = body_item.copy()

    assert id(new_item) != id(body_item)
    assert new_item.name == body_item.name
    assert new_item.mods != body_item.mods
    assert isinstance(new_item.mods, Modifier)
    assert new_item.mods.adds == body_item.mods.adds
    assert new_item.mods.mults == body_item.mods.mults
    assert new_item.description == body_item.description
    assert new_item.armor_type == body_item.armor_type
    assert new_item.item_type == body_item.item_type

def test_bodyequipment_export(bodyequipment_all_items_mods):
    for _, item in bodyequipment_all_items_mods.items():
        exporter = item.export()
        assert exporter.get('mods', False)

def test_bodyequipment_details(bodyequipment_all_items_mods, bodyequipment_details_expectation):
    """Mostly test format and indention"""
    test_item = list(bodyequipment_all_items_mods.values())[0]
    print(test_item.details())
    for index, expectations in enumerate(bodyequipment_details_expectation):
        assert test_item.details(index) == expectations


# ================================== #
# Testing Weapon Equipment Functions #
# ================================== #
def test_weaponequipment_init(weaponequipment_all_types):
    for _, weapon in weaponequipment_all_types.items():
        assert weapon.get_weapon_type() in WEAPON_TYPES
    

# class EquipmentTest(unittest.TestCase):
#     @staticmethod
#     def get_body() -> BodyEquipment:
#         return BodyEquipment(
#             name="Test_Equipment",
#             description="This is a test for the equipment class",
#             item_type=BODY_ITEM_TYPE,
#             armor_type=BODY_ARMOR_TYPE,
#         )

#     @staticmethod
#     def get_weapon() -> WeaponEquipment:
#         return WeaponEquipment(
#             name="Test_Equipment",
#             description="This is a test for the equipment class",
#             armor_type=-1,
#             weapon_type=1,
#         )

#     @staticmethod
#     def get_equipment():
#         return [EquipmentTest.get_body(), EquipmentTest.get_weapon()]

#     def test_equipment_str(self):
#         for equip in EquipmentTest.get_equipment():
#             self.assertIsNotNone(equip.__str__())
#             self.assertIsInstance(equip.__str__(), str)

#     def test_equipment_details(self):
#         for equip in EquipmentTest.get_equipment():
#             self.assertIsNotNone(equip.details())
#             self.assertIsInstance(equip.details(), str)

#     def test_equipment_print_to_file(self):
#         equip_obj = self.get_body()
#         equip_obj.print_to_file()
#         filename = f"{equip_obj.name}.json"
#         self.assertTrue(os.path.exists(filename), "Equipment: print_to_file Failed")
#         if os.path.exists(filename):
#             os.remove(filename)

#     def test_equipment_export(self):
#         # Testing of null value
#         for equip in EquipmentTest.get_equipment():
#             self.assertIsNotNone(equip.export())
#             self.assertIsInstance(equip.export(), dict)

#     def test_equipment_output_examples(self):

#         print(f"\n{'Equipment Example Output'.center(80, '-')}")
#         for equip in EquipmentTest.get_equipment():
#             print(f"\n__str__ Output:\n{equip}")
#             print(f"\ndetails Output:\n{equip.details()}")
#             print(f"\nexport Output:\n{equip.export()}")
#         print(f"\n{'Done'.center(80, '-')}")

#     def test_equipment_duplicate_call(self):
#         e1 = self.get_weapon()
#         e2 = self.get_weapon()

#         self.assertNotEqual(e1, e2)
#         self.assertNotEqual(id(e1), id(e2))
#         print(e1.export())

    # TODO: def test_equipment_getStats(self:)


# TODO: When testing weapon export, test to make sure all of the weapon pieces are included
