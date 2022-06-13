from funclg.character.character import Character


def build_new_character():
    print("TODO: Build New Character Section")


def edit_character():
    print("TODO: Build Edit Character Section")


def delete_character():
    print("TODO: Build Delete Character Section")


CHARACTER_MENU = {
    "name": "Manage Characters",
    "sub-menu": {
        "1": {"name": "New Character", "function": build_new_character},
        "2": {"name": "Edit Character", "function": edit_character},
        "3": {"name": "Delete Character", "function": delete_character},
    },
}
