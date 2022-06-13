from funclg.character.abilities import Abilities


def build_ability():
    print("TODO: Build New Ability Section")


def edit_ability():
    print("TODO: Build Edit Ability Section")


def delete_ability():
    print("TODO: Build Delete Ability Section")


ABILITY_MENU = {
    "name": "Manage Abilities",
    "sub-menu": {
        "1": {"name": "Add New Ability", "function": build_ability},
        "2": {"name": "Edit Ability", "function": edit_ability},
        "3": {"name": "Delete Ability", "function": delete_ability},
    },
}
