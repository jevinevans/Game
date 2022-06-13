from funclg.character.equipment import BodyEquipment, WeaponEquipment


def build_weapon():
    print("TODO: Build New Weapon Section")


def build_body_armor():
    print("TODO: Build New Body Armor Section")


def edit_weapon():
    print("TODO: Build Edit Weapon Section")


def edit_body_armor():
    print("TODO: Build Edit Body Armor Section")


def delete_weapon():
    print("TODO: Build Delete Weapon Section")


def delete_body_armor():
    print("TODO: Build Delete Body Armor Section")


EQUIPMENT_MENU = {
    "name": "Manage Equipment",
    "sub-menu": {
        "1": {
            "name": "Manage Weapons",
            "sub-menu": {
                "1": {"name": "New Weapon", "function": build_weapon},
                "2": {"name": "Edit Weapon", "function": edit_weapon},
                "3": {"name": "Delete Weapon", "function": delete_weapon},
            },
        },
        "2": {
            "name": "Manage Body Armor",
            "sub-menu": {
                "1": {"name": "New Body Armor", "function": build_body_armor},
                "2": {"name": "Edit Body Armor", "function": edit_body_armor},
                "3": {"name": "Delete Body Armor", "function": delete_body_armor},
            },
        },
    },
}
