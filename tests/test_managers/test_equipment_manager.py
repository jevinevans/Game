"""
Description: The is a unit test for the equipmet manager class.
Developer: Jevin Evans
Date: 11.12.2022
"""

from unittest.mock import patch

import pytest

import funclg.managers.equipment_manager as eq_man
from funclg.utils.types import ARMOR_TYPES, ITEM_TYPES


@pytest.fixture
def test_equipment():
    return {
        "name": "Test Plate",
        "description": "Test Chest Plate",
        "item_type": 1,
        "armor_type": 0,
        "stats": {
            "attributes": {"defense": 10, "health": 1, "energy": 1, "attack": 1, "_power": 13}
        },
        "_id": "ARMOR-16342-QLERCA-36276",
    }


@pytest.fixture
def test_equipment_2():
    return {
        "name": "Test Head",
        "description": "Test Chest Head",
        "item_type": 0,
        "armor_type": 2,
        "stats": {
            "attributes": {"defense": 10, "health": 40, "energy": 1, "attack": 1, "_power": 53}
        },
        "_id": "ARMOR-16342-QLPBCA-36276",
    }


@pytest.fixture
def test_weapon():
    return {
        "name": "Test Spear",
        "description": "Test Spear",
        "item_type": 4,
        "armor_type": 2,
        "stats": {
            "attributes": {"defense": 10, "health": 1, "energy": 1, "attack": 27, "_power": 39}
        },
        "_id": "WEAPON-16151-OEGEFS-36126",
        "weapon_type": "Spear",
    }


@patch("funclg.utils.data_mgmt.update_data")
def test_equipment_manager_update_data(m_db, test_equipment, test_equipment_2, test_weapon):
    # Add Test Items to data
    eq_man.EQUIPMENT_DATA["data"] = {}
    eq_man.EQUIPMENT_DATA["objects"] = {}
    eq_man.EQUIPMENT_DATA["data"][test_equipment["_id"]] = test_equipment
    eq_man.EQUIPMENT_DATA["data"][test_equipment_2["_id"]] = test_equipment_2
    eq_man.EQUIPMENT_DATA["data"][test_weapon["_id"]] = test_weapon

    # Make sure data was loaded into objects but that there are new data items that need objects created

    eq_man.update_data()
    print(eq_man.EQUIPMENT_DATA["data"])

    assert len(eq_man.EQUIPMENT_DATA["data"]) == len(eq_man.EQUIPMENT_DATA["objects"])
    assert len(eq_man.EQUIPMENT_DATA["data"]) == 3
    assert len(eq_man.EQUIPMENT_DATA["objects"]) == 3
    assert m_db.called_once


@patch("funclg.utils.data_mgmt.update_data")
def test_equipment_manager_export_data(m_db, test_weapon, test_equipment, test_equipment_2):
    eq_man.EQUIPMENT_DATA["data"] = {}
    eq_man.EQUIPMENT_DATA["objects"] = {}
    eq_man.EQUIPMENT_DATA["objects"][test_weapon["_id"]] = eq_man.WeaponEquipment(**test_weapon)
    eq_man.EQUIPMENT_DATA["objects"][test_equipment["_id"]] = eq_man.BodyEquipment(**test_equipment)
    eq_man.EQUIPMENT_DATA["objects"][test_equipment_2["_id"]] = eq_man.BodyEquipment(
        **test_equipment_2
    )

    eq_man.export_data()
    assert len(eq_man.EQUIPMENT_DATA["data"]) == len(eq_man.EQUIPMENT_DATA["objects"])
    assert len(eq_man.EQUIPMENT_DATA["data"]) == 3
    assert len(eq_man.EQUIPMENT_DATA["objects"]) == 3

    assert test_weapon["_id"] in eq_man.EQUIPMENT_DATA["data"]
    assert m_db.called_once


@patch("funclg.managers.equipment_manager.logger")
@patch("funclg.managers.equipment_manager.selection_validation")
def test_equipment_manager_select_equipment(m_sel, m_log, test_equipment, test_weapon):
    # Test Weapon Select
    eq_man.EQUIPMENT_DATA["data"][test_weapon["_id"]] = test_weapon

    m_sel.side_effect = ["Weapons", test_weapon["_id"]]

    assert eq_man.select_equipment() == test_weapon["_id"]

    # Test Armor Select
    eq_man.EQUIPMENT_DATA["data"][test_equipment["_id"]] = test_equipment
    m_sel.side_effect = ["Armor", test_equipment["_id"]]

    assert eq_man.select_equipment() == test_equipment["_id"]

    # Test No Data
    eq_man.EQUIPMENT_DATA["data"] = {}
    eq_man.select_equipment()
    assert m_log.warning.called


@patch("builtins.print")
@patch("funclg.managers.equipment_manager.logger")
@patch("funclg.managers.equipment_manager.select_equipment")
def test_equipment_manager_show_equipment(m_eq_select, m_log, m_print, test_equipment):
    # Test Success
    teq = eq_man.BodyEquipment(**test_equipment)
    eq_man.EQUIPMENT_DATA["objects"][teq.id] = teq

    m_eq_select.return_value = teq.id
    eq_man.show_equipment()
    assert m_print.called_with(teq.details())

    # Fail Test
    m_eq_select.return_value = None
    eq_man.show_equipment()
    assert m_log.called_with("There are no equipment items to show.")
    assert m_log.warning.called


@patch("builtins.print")
@patch("funclg.managers.equipment_manager.logger")
@patch("funclg.managers.equipment_manager.confirmation")
@patch("funclg.managers.equipment_manager.update_data")
@patch("funclg.managers.equipment_manager.select_equipment")
def test_equipment_manager_delete_equipment(
    m_seleq, m_update, m_confirm, m_log, m_print, test_equipment
):
    # Yes Delete
    test_obj = eq_man.BodyEquipment(**test_equipment)
    eq_man.EQUIPMENT_DATA["data"][test_equipment["_id"]] = test_equipment
    eq_man.EQUIPMENT_DATA["objects"][test_obj.id] = test_obj

    m_seleq.return_value = test_equipment["_id"]
    m_confirm.return_value = True

    eq_man.delete_equipment()

    assert test_obj.id not in eq_man.EQUIPMENT_DATA["data"]
    assert test_obj.id not in eq_man.EQUIPMENT_DATA["objects"]
    assert m_print.called_with(f"Deleting {test_obj.name}")
    assert m_update.called

    # No Delete
    eq_man.EQUIPMENT_DATA["data"][test_equipment["_id"]] = test_equipment

    m_seleq.return_value = test_equipment["_id"]
    m_confirm.return_value = False
    eq_man.delete_equipment()
    assert m_print.called_with("Keeping all equipment in the vault...")

    # No Items Delete
    m_seleq.return_value = None
    eq_man.delete_equipment()
    assert m_log.warning.called


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.build_stats")
@patch("funclg.managers.equipment_manager.selection_validation")
@patch("funclg.managers.equipment_manager.string_validation")
def test_equipment_manager_new_weapon(m_str_val, m_sel, m_stats_gen, m_id, test_weapon):
    m_sel.return_value = test_weapon["weapon_type"]
    m_str_val.side_effect = [test_weapon["name"], test_weapon["description"]]
    m_stats_gen.return_value = test_weapon["stats"]
    m_id.return_value = test_weapon["_id"]

    test_object_weapon = eq_man.WeaponEquipment(**test_weapon)

    result_weapon = eq_man._new_weapon()

    assert result_weapon.id == test_object_weapon.id
    assert result_weapon.name == test_object_weapon.name
    assert result_weapon.description == test_object_weapon.description
    assert result_weapon.weapon_type == test_object_weapon.weapon_type
    assert result_weapon.stats == test_object_weapon.stats
    assert result_weapon.stats.get_stats() == test_object_weapon.stats.get_stats()


@patch("funclg.utils.data_mgmt.id_gen")
@patch("funclg.managers.stats_manager.build_stats")
@patch("funclg.managers.equipment_manager.selection_validation")
@patch("funclg.managers.equipment_manager.string_validation")
def test_equipment_manager_new_body_armor(m_str_val, m_sel, m_stats_gen, m_id, test_equipment):
    m_sel.side_effect = [
        ITEM_TYPES[test_equipment["item_type"]],
        ARMOR_TYPES[test_equipment["armor_type"]],
    ]
    m_str_val.side_effect = [test_equipment["name"], test_equipment["description"]]
    m_stats_gen.return_value = test_equipment["stats"]
    m_id.return_value = test_equipment["_id"]

    test_object_equipment = eq_man.BodyEquipment(**test_equipment)

    result_equipment = eq_man._new_body_armor()

    assert result_equipment.id == test_object_equipment.id
    assert result_equipment.name == test_object_equipment.name
    assert result_equipment.description == test_object_equipment.description
    assert result_equipment.item_type == test_object_equipment.item_type
    assert result_equipment.armor_type == test_object_equipment.armor_type
    assert result_equipment.stats == test_object_equipment.stats
    assert result_equipment.stats.get_stats() == test_object_equipment.stats.get_stats()


@patch("builtins.print")
@patch("funclg.managers.equipment_manager.update_data")
@patch("funclg.managers.equipment_manager._new_weapon")
@patch("funclg.managers.equipment_manager._new_body_armor")
@patch("funclg.managers.equipment_manager.confirmation")
@patch("funclg.managers.equipment_manager.selection_validation")
def test_equipment_manager_build_equipment(
    m_sel, m_confirm, m_new_body, m_new_wep, m_update, m_print, test_equipment, test_weapon
):
    # Test New Body Armor + Positive Valdiation Branch
    m_sel.return_value = "Armor"
    m_new_body.return_value = eq_man.BodyEquipment(**test_equipment)
    m_confirm.return_value = True

    eq_man.build_equipment()

    assert m_update.called
    assert test_equipment["_id"] in eq_man.EQUIPMENT_DATA["data"]

    # Test New Weapon + Negative Validation  Branch
    m_sel.return_value = "Weapon"
    m_new_wep.return_value = eq_man.WeaponEquipment(**test_weapon)
    m_confirm.return_value = False

    eq_man.build_equipment()

    assert m_print.called_with(f"{test_weapon['name']} has been saved!!")
    assert m_print.called_with("No new weapon, oh well...")


def test_equipment_manager_filter_equipment_by_armor_type(
    test_equipment, test_equipment_2, test_weapon
):
    armor_type_0 = eq_man.BodyEquipment(**test_equipment)
    weapon_type_2 = eq_man.WeaponEquipment(**test_weapon)
    armor_type_2 = eq_man.BodyEquipment(**test_equipment_2)
    del eq_man.EQUIPMENT_DATA["objects"]
    eq_man.EQUIPMENT_DATA.update(
        {
            "objects": {
                armor_type_0.id: armor_type_0,
                weapon_type_2.id: weapon_type_2,
                armor_type_2.id: armor_type_2,
            }
        }
    )
    armor_type_0_results = {
        "Head": {},
        "Chest": {armor_type_0.id: armor_type_0},
        "Back": {},
        "Pants": {},
        "Weapon": {},
    }
    armor_type_2_results = {
        "Head": {armor_type_2.id: armor_type_2},
        "Chest": {},
        "Back": {},
        "Pants": {},
        "Weapon": {weapon_type_2.id: weapon_type_2},
    }

    assert armor_type_0_results == eq_man.filter_equipment_by_armor_type(0)
    assert armor_type_2_results == eq_man.filter_equipment_by_armor_type(2)
