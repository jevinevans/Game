from funclg.character.roles import Roles


def build_role():
    print("TODO: Build New Role Section")


def edit_role():
    print("TODO: Build Edit Role Section")


def delete_role():
    print("TODO: Build Delete Role Section")


ROLES_MENU = {
    "name": "Manage Roles",
    "sub-menu": {
        "1": {"name": "New Role", "function": build_role},
        "2": {"name": "Edit Role", "function": edit_role},
        "3": {"name": "Delete Role", "function": delete_role},
    },
}
