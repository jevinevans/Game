"""Unittest for Roles Class"""
import os
import unittest
from random import randint

from FUNCLG.character.abilities import Abilities
from FUNCLG.character.roles import Roles


class RolesTest(unittest.TestCase):
    """Unittest for Roles Class"""

    @staticmethod
    def create_abiities():
        """Creates a set of test abilities for the roles"""
        test_abilities = {}
        test_abilities["Magic"] = Abilities(
            name="Fireball",
            damage_type="Magic",
            effect=randint(1, 50),
            description="A blazing ball of fire",
        )
        test_abilities["Physical"] = Abilities(
            name="Slash",
            damage_type="Physical",
            effect=randint(1, 50),
            description="A slashing strike with a sharp weapon",
        )
        test_abilities["Healing"] = Abilities(
            name="Holy Light",
            damage_type="Healing",
            effect=randint(1, 50),
            description="Heals the user",
        )
        test_abilities["Buff"] = Abilities(
            name="Buff Test",
            damage_type="Buff",
            effect=randint(1, 50),
            description="Boost self attribute",
        )
        test_abilities["Buff_2"] = Abilities(
            name="Armor Buff",
            damage_type="Buff",
            effect=randint(1, 50),
            description="Adds extra defense",
        )
        test_abilities["Debuff"] = Abilities(
            name="Debuff Test",
            damage_type="Debuff",
            effect=randint(1, 50),
            description="Reduces enemy defenses",
        )
        test_abilities["Debuff_2"] = Abilities(
            name="Drain",
            damage_type="Debuff",
            effect=randint(1, 50),
            description="Reduces enemy mana",
        )
        return test_abilities

    @staticmethod
    def get_warrior():
        """Heavy Armor, and Physical, Healing, Buff, and Debuff, 2 Correct Abilities"""
        test_abilities = RolesTest.create_abiities()
        return Roles(
            name="Warrior",
            description="Sword whielding champions that defend the lang",
            armor_type=2,
            damage_types=["Buff", "Physical", "Debuff", "Healing"],
            abilities=[test_abilities["Physical"], test_abilities["Healing"]],
        )

    @staticmethod
    def get_mage():
        """Medium Armor, and Magic, Buff, Debuff, and Invalid_Type, No Abilities"""
        return Roles(
            name="Mage",
            description="Blessed individuals that can command and control the aspects of magic",
            armor_type=1,
            damage_types=["Buff", "Magic", "Debuff", "Invalid_Type"],
        )

    @staticmethod
    def get_rouge():
        """light Armor, Class Types Physical, Buff, Debuff, 1 right and 1 wrong Ability to start"""
        test_abilities = RolesTest.create_abiities()
        return Roles(
            name="Rouge",
            description="Agile knife wheilders that are quick and deadly",
            armor_type=0,
            damage_types=["Buff", "Debuff", "Physical"],
            abilities=[test_abilities["Magic"], test_abilities["Debuff"]],
        )

    @staticmethod
    def get_roles():
        return [RolesTest.get_warrior(), RolesTest.get_rouge(), RolesTest.get_mage()]

    def test_roles_init(self):
        warrior, rouge, mage = self.get_roles()

        # Test All Good Init
        self.assertEqual(len(warrior.damage_types), 4)
        self.assertEqual(len(warrior.abilities), 2)

        # Test Invalid Class Type Validation on Init
        self.assertEqual(len(mage.damage_types), 3)

        # Test Invalid Ability Validation on Init
        self.assertEqual(len(rouge.abilities), 1)

    def test_roles_str(self):
        for role in self.get_roles():
            self.assertIsNotNone(role.__str__())
            self.assertIsInstance(role.__str__(), str)

    def test_roles_add_power(self):
        test_abilities = self.create_abiities()
        warrior = self.get_warrior()

        # Test normal power add
        for power in [test_abilities["Buff"], test_abilities["Debuff"], test_abilities["Buff_2"]]:
            self.assertEqual(warrior.add_power(power), 0)

        # Test Invalid Ability Add
        self.assertEqual(warrior.add_power(test_abilities["Magic"]), 1)

        # Test Max Power
        self.assertEqual(warrior.add_power(test_abilities["Debuff_2"]), 3)

    def test_roles_get_power(self):
        warrior = self.get_warrior()
        mage = self.get_mage()

        # Test Good Call
        self.assertIsInstance(warrior.get_power(1), Abilities)
        self.assertEqual(len(warrior.abilities), 2)

        # Test invalid small index
        self.assertIsNone(warrior.get_power(1000))

        # Test invalid large index
        self.assertIsNone(warrior.get_power(-124))

        # Test no abilities call
        self.assertIsNone(mage.get_power(0))

    def test_roles_remove_power(self):
        warrior = self.get_warrior()
        ability_count = len(warrior.abilities)

        # Test Valid Remove
        while ability_count:
            self.assertTrue(warrior.remove_power(ability_count - 1))
            ability_count -= 1

        # Test remove ability from empty list
        for _ in range(2):
            self.assertFalse(warrior.remove_power(-1))

    def test_roles_details(self):
        for role in self.get_roles():
            self.assertIsNotNone(role.details())
            self.assertIsInstance(role.details(), str)

    def test_roles_export(self):
        for role in self.get_roles():
            self.assertIsNotNone(role.export())
            self.assertIsInstance(role.export(), dict)

    def test_roles_print_to_file(self):
        for role in self.get_roles():
            role.print_to_file()
            filename = f"{role.name}.json"
            self.assertTrue(os.path.exists(filename), "Roles: print_to_file Failed")
            if os.path.exists(filename):
                os.remove(filename)

    def test_roles_output_examples(self):
        print(f"\n{'Roles Example Output'.center(80, '-')}")
        for role in self.get_roles():
            print(f"\n__str__ Output:\n{role}")
            print(f"\ndetails Output: {role.details()}")
            print(f"\nexport Output:\n{role.export()}")
        print(f"\n{'Done'.center(80, '-')}")

    def test_roles_duplicate_ability_assign(self):
        warrior = Roles(
            name="Warrior", armor_type=2, description="Warrior class", damage_types=["Physical"]
        )
        rouge = Roles(
            name="Rouge", armor_type=0, description="Rouge class", damage_types=["Physical"]
        )
        abilities = self.create_abiities()

        self.assertEqual(rouge.add_power(abilities["Physical"]), 0)
        self.assertEqual(warrior.add_power(abilities["Physical"]), 0)
        self.assertNotEqual(warrior.get_power(0), rouge.get_power(0))
