#############################################################################
# Programmer: Jevin Evans                                                   #
# Date: 7/15/2021                                                           #
# Program: Armor Class                                                      #
# Description:    The Armor class is made to store equipment itmes for a    #
#                   character.                                              #
#############################################################################

import json

try:
    from core.equipment import Equipment
    from utils.types import ARMOR_TYPES, ITEM_TYPES
except ImportError:
    from FUNCLG.core.equipment import Equipment
    from FUNCLG.utils.types import ARMOR_TYPES, ITEM_TYPES


class Armor:

    _id = 0

    def __init__(
        self,
        armorType: int = 0,
        head: Equipment = None,
        chest: Equipment = None,
        back: Equipment = None,
        pants: Equipment = None,
        weapon: Equipment = None,
    ):
        self.name = "Armor_" + str(Armor._id)
        self.armorType = (
            armorType if armorType <= len(ARMOR_TYPES) and armorType >= 0 else 0
        )
        # self.stats = #Stat Object
        # Requires that the equipment is the same armor time
        self.head = (
            head if head is not None and head.armorType == self.armorType else None
        )
        self.chest = (
            chest if chest is not None and chest.armorType == self.armorType else None
        )
        self.back = (
            back if back is not None and back.armorType == self.armorType else None
        )
        self.pants = (
            pants if pants is not None and pants.armorType == self.armorType else None
        )
        self.weapon = (
            weapon
            if weapon is not None and weapon.armorType == self.armorType
            else None
        )

        # Call stats update function self.???
        Armor._id += 1

    def __str__(self):
        # Eventually add the stats to the class as well
        temp = f"{self.name}: <"
        temp += "H:1, " if self.head else "H:0, "
        temp += "C:1, " if self.chest else "C:0, "
        temp += "B:1, " if self.back else "B:0, "
        temp += "P:1, " if self.pants else "P:0, "
        temp += "W:1>" if self.weapon else "W:0>"
        return temp

    # TODO: Need to test if I need to copy equipment or it will link right
    # TODO: Consider if this should be one method or multiples for each type
    def equip(self, item: Equipment):
        temp = None
        if item is not None and item.armorType == self.armorType:
            if item.getItemType() == "Head":
                self.head, temp = item, self.head
            elif item.getItemType() == "Chest":
                self.chest, temp = item, self.chest
            elif item.getItemType() == "Back":
                self.back, temp = item, self.back
            elif item.getItemType() == "Pants":
                self.pants, temp = item, self.pants
            elif item.getItemType() == "Weapon":
                self.weapon, temp = item, self.weapon
        else:
            print(f"\n{item}, is not compatable with this armor")
            return item
        # Returns previously equiped item, if there was one
        if isinstance(temp, Equipment):
            return temp

    def dequip(self, item):
        """
        Removes the currently equiped item in the current position and wil return an item if there is something already equiped.
        """
        temp = None
        itemType = ""
        if isinstance(item, int):
            # If the user sends the item type value
            if item < 0 or item >= len(ITEM_TYPES):
                print("ERROR: Armor.Dequip Invalid dequip slot.")
                return
            itemType = ITEM_TYPES[item]
        elif isinstance(item, str):
            # If the user sends the name of the value
            itemType = item.capitalize()
            if itemType not in ITEM_TYPES:
                print("ERROR: Armor.Dequip Invalid dequip slot.")
                return
        # elif isinstance(item, Equipment):
        #     # Future for if the user selects the item to unequip may send item may remove all together
        #     itemType = item.getItemType()

        if itemType == "Head":
            temp, self.head = self.head, None
        elif itemType == "Chest":
            temp, self.chest = self.chest, None
        elif itemType == "Back":
            temp, self.back = self.back, None
        elif itemType == "Pants":
            temp, self.pants = self.pants, None
        elif itemType == "Weapon":
            temp, self.weapon = self.weapon, None
        else:
            print("Not a valid dequip spot.")

        return temp

    def details(self):
        desc = f"\n Armor \n{''.join(['-' for x in range(7)])}"
        desc += f"\nHead: {self.head.__str__()}" if self.head else "\nHead: None"
        desc += f"\nChest: {self.chest.__str__()}" if self.chest else "\nChest: None"
        desc += f"\nBack: {self.back.__str__()}" if self.back else "\nBack: None"
        desc += f"\nPants: {self.pants.__str__()}" if self.pants else "\nPants: None"
        desc += (
            f"\nWeapon: {self.weapon.__str__()}" if self.weapon else "\nWeapon: None"
        )
        return desc

    # TODO: Write tests and see if the below method works how I want and is more effcient
    # def details(self):
    #     desc = f"\n Armor \n{''.join(['-' for x in range(7)])}"
    #     desc += f"\nHead: {self.head.__str__()}"
    #     desc += f"\nChest: {self.chest.__str__()}"
    #     desc += f"\nBack: {self.back.__str__()}"
    #     desc += f"\nPants: {self.pants.__str__()}"
    #     desc += f"\nWeapon: {self.weapon.__str__()}"
    #     return desc

    def printToFile(self):
        with open(self.name + ".json", "w") as oFile:
            json.dump(self.export(), oFile)

    def export(self):
        exporter = self.__dict__
        for x, y in exporter.items():
            if isinstance(y, Equipment):
                exporter[x] = y.export()
        return exporter

    # def getStats(self):
    # Will be a sum of the equipment stats, may or may not display the name and stats


# def main():
# weapon = Equipment("excelsior", "Special sword of power", armorType=2, itemType=4, weaponType=0, level=5, abilityPoints=50)
# weapon1 = Equipment("Yldris Wand", "Special wand of power", armorType=2, itemType=4, weaponType=1, level=5, abilityPoints=60)
# head = Equipment("Shining Top", "Top hat that sparkles", 2, 0, None, 5, 40)
# chest = Equipment("Black suit", "Basic black suit", 2, 1, None, 1, 10)
# back = Equipment("Should cape", "Simple shoulder coat that cover shoulder", 2, 2, None, 2, 20)
# pants = Equipment("Suit pants", "Basic suit pant", 2, 3, None, 2, 15)

# newArm = Armor(2, chest=chest, pants=pants)
# print(newArm)

# newArm.equip(head)
# newArm.equip(back)
# newArm.equip(weapon)

# print(newArm)
# print(newArm.details())

# temp = newArm.dequip("weapon")

# print(f"\nDequiped: {temp}")
# print(newArm)
# print(newArm.details())

# temp = newArm.equip(temp)
# print(newArm.details())

# newArm.equip(weapon1)
# print(newArm.details())

# print()
# print(newArm.export())
