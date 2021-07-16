#####################################################################################   
#   Programmer: Jevin Evans                                                         #
#	Date: 7/15/2021                                                                 #
#	Program: Armor Class                                                            #
#   Description: The Armor class is made to store equipment itmes for a character.  #      
#####################################################################################

import json
try:
    from core.equipment import Equipment
    from utils.types import getItemType, getArmorType
except:
    from FUNCLG.core.equipment import Equipment
    from FUNCLG.utils.types import getItemType, getArmorType

class Armor():
    numArm = 0

    def __init__(self, armorType:int=0, head:Equipment=None, chest:Equipment=None, back:Equipment=None, pants:Equipment=None, weapon:Equipment=None):
        self.name = "Armor_"+str(numArm)
        self.armorType = armorType
        
        # Requires that th
        self.head = head if getArmorType(head) == getArmorType(self.armorType) or head.armorType == None else None
        self.chest = chest if getArmorType(chest) == getArmorType(self.armorType) or chest.armorType == None else None
        self.back = back if getArmorType(back) == getArmorType(self.armorType) or back.armorType == None else None
        self.pants = pants if getArmorType(pants) == getArmorType(self.armorType) or pants.armorType == None else None
        self.weapon = weapon if getArmorType(weapon) == getArmorType(self.armorType) or weapon.armorType == None else None
        numArm += 1

    def __str__(self):
        temp = "Armor: <"
        temp += "H:1, " if self.head else "H:0, "
        temp += "C:1, " if self.chest else "C:0, "
        temp += "B:1, " if self.back else "B:0, "
        temp += "P:1, " if self.pants else "P:0, "
        temp += "W:1>" if self.weapon else "W:0>"
        return temp

    # TODO: Need to test if I need to copy equipment or it will link right
    # TODO: Consider if this should be one method or multiples for each type
    def equip(self, item:Equipment):
        if getItemType(item.itemType) == "Helmet":
            self.head 
        elif getItemType(item.itemType) == "Chest":
            self.chest
        elif getItemType(item.itemType) == "Back":
            self.back
        elif getItemType(item.itemType) == "Pants":
            self.pants
        elif getItemType(item.itemType) == "Weapon":
            self.weapon
        else:
            print(f"{item}, is not compatable with this armor")
    
    def dequip(self, item):
        temp = None
        if getItemType(item.itemType) == "Helmet":
            temp, self.head = self.head, None
        elif getItemType(item.itemType) == "Chest":
            temp, self.chest = self.chest, None
        elif getItemType(item.itemType) == "Back":
            temp, self.back = self.back, None
        elif getItemType(item.itemType) == "Pants":
            temp, self.pants = self.pants, None
        elif getItemType(item.itemType) == "Weapon":
            temp, self.weapon = self.weapon, None
        else:
            print("Not a valid dequip spot.")
        
        return temp

    # def details(self):

    def printToFile(self):
        with open(self.name+".json", "w") as oFile:
            json.dump(self.__dict__, oFile)

    # def export(self):

