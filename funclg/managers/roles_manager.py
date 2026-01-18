"""
Description: A manager class for creating, updating, and removing roles.
Developer: Jevin Evans
Date: 6.19.2022
"""

from loguru import logger

import funclg.managers.stats_manager as stats_man
from funclg.character.abilities import Abilities
from funclg.character.roles import Roles
from funclg.managers.abilities_manager import AbilitiesManager
from funclg.managers.manager import BaseManager, SingletonMeta
from funclg.utils.types import ABILITY_TYPES, ARMOR_TYPES


class RolesManager(BaseManager, metaclass=SingletonMeta):
    """
    A manager class for creating, updating, and removing roles.
    """

    def __init__(self):
        """Initialize the RolesManager."""
        super().__init__(name="Roles", filename="roles.json")
        self.menu["menu_items"] = [
            {"title": "New Role", "value": self.build_role},
            # {"title": "Edit Role", "value": self.edit_role},
            {"title": "View Role Details", "value": self.show_role},
            {"title": "Delete Role", "value": self.delete_role},
        ]

        logger.debug("RolesManager initialized.")
        self.load_data()
        logger.debug(f"RolesManager data loaded {len(self.data)} roles.")

    def update_data(self):
        for _id, data in self.data.items():
            if _id not in self.objects:
                obj_abilities = []
                for _ability in data["abilities"]:
                    obj_abilities.append(Abilities(**_ability))
                new_data = data.copy()
                new_data["abilities"] = obj_abilities
                self.objects[_id] = Roles(**new_data)
        super().update_data()

    def export_data(self):
        for _id, data in self.objects.items():
            self.data[_id] = data.export()

        super().export_data()

    def _select_ability_types(self):
        """Allows the user to select the ability types they want to add to the role"""
        a_types = []
        available_types = ABILITY_TYPES.copy()

        continue_selection = True

        while continue_selection:
            print(
                "Lets add some ability types to your role!\n\nWhat ability type(s) would you like this class to have?"
            )
            # Add description print out
            for _a_type, data in available_types.items():
                print(f"{_a_type}\n\tAvailable Mods: {', '.join(data['mods'])}")

            a_type = self.get_selection("Choose from the above:", available_types)
            a_types.append(a_type)

            print(f"Current Ability Types: {' '.join(a_types)}")
            if self.get_confirmation("Would you like to add another type?"):
                del available_types[a_type]
                continue
            continue_selection = False

        return a_types

    def _select_role_abilities(self, a_types: list) -> list[Abilities]:
        """
        Guides the user through ability selection for a role.
        """

        def _display_abilities():
            print(f"You can choose abilities from the following types: {', '.join(a_types)}")

            for _atype, _abilities in available_abilities.items():
                print(f"{_atype}:")
                for _ability in _abilities:
                    print(f"\t{_ability}")

            a_choice = self.get_selection(
                "Select ability type:",
                list(available_abilities.keys()),
                display_attr="",
                return_attr="",
            )
            if available_abilities[a_choice]:
                new_ability_name = self.get_selection(
                    "Select ability to add:", [a.name for a in available_abilities[a_choice]]
                )

                new_ability = [
                    a for a in available_abilities[a_choice] if a.name == new_ability_name
                ][0]

                if self.get_confirmation(f"Do you want to add {new_ability.name} to this role?"):
                    # Remove added ability from available options and return
                    available_abilities[new_ability.ability_type].remove(new_ability)
                    return new_ability
                return None
            print(f"\nThere are no more {a_choice} abilities available.\n")
            return None

        print(
            "Now lets add some abilities!\n\nYou can add 5 abilities max, which would you like to add (see available below)?"
        )

        role_abilities = []
        available_abilities = AbilitiesManager().filter_abilities_by_types(a_types)

        # Show available abilities created, filtered by the ability types selcted
        while len(role_abilities) < 5:
            new_ability = _display_abilities()
            if new_ability:
                role_abilities.append(new_ability)

            print("This role currently have the following abilities:")
            for ability in role_abilities:
                print(f"\n\t- {ability}")
            print(f"\nYou can still add more {5-len(role_abilities)} abilities.")

            if not self.get_confirmation("Would you like to add another ability?"):
                break

        return role_abilities

    def build_role(self):
        """Dialog for building a new character role"""

        print("\nStarting Role Creation")
        role_name = self.get_string("What would you like to name this new Role?", "Name")
        role_desc = self.get_string(f"How would you describe {role_name}?", "Description")
        armor_type = self.get_selection(
            f"What type of armor would you like to make the {role_name}?", ARMOR_TYPES
        )

        a_types = self._select_ability_types()

        r_abilities = self._select_role_abilities(a_types)

        role_stats = stats_man.build_stats()

        new_role = Roles(
            name=role_name,
            description=role_desc,
            armor_type=ARMOR_TYPES.index(armor_type),
            ability_types=a_types,
            abilities=r_abilities,
            stats=role_stats,
        )

        if self.get_confirmation(f"You created:\n{new_role.details()}\nSave new role?"):
            self.data[new_role.id] = new_role.export()
            self.update_data()
            print(f"{new_role.name} has been saved!!!")
            return

        print("Oh well..., no roles to add to this awesome adventure!!!")
        del new_role

    def sort_roles_by_armor_type(self):
        sorted_roles = {}

        for index, armor_type in enumerate(ARMOR_TYPES):
            sorted_roles[armor_type] = [
                role for role in self.objects.values() if role.armor_type == index
            ]

        sorted_roles = {armor_type: data for armor_type, data in sorted_roles.items() if data}

        return sorted_roles

    def select_role(self):
        if self.data:
            return self.get_selection("Select a role:", self.data, "name", "_id")
        logger.warning("There are no roles available.")
        return None

    def show_role(self):
        show_role_id = self.select_role()
        if show_role_id:
            _show_role = self.objects[show_role_id]
            print(_show_role.details())
            return
        logger.warning("There are no roles available to show.")

    def delete_role(self):
        del_role_id = self.select_role()
        if del_role_id:
            del_role = self.data[del_role_id]
            if self.get_confirmation(f"Do you want to delete \"{del_role['name']}\"?"):
                print(f"Deleteing {del_role['name']}")
                del self.data[del_role_id]
                del self.objects[del_role_id]
                self.update_data()
                return
            print("Keeping all roles in the vault...")
            return
        logger.warning("There are no roles to delete.")
