#####################################################################################   
#   Programmer: Jevin Evans                                                         #
#	Date: 7/15/2021                                                                 #
#	Program: Armor Class                                                            #
#   Description: The Armor class is made to store equipment itmes for a character.  #      
#####################################################################################

import json
try:
    from core.equipment import Equipment
except:
    from FUNCLG.core.equipment import Equipment

class Armor():
    numArm = 0

    def __init__(self, head:Equipment=None, chest:Equipment=None, back:Equipment=None, pants:Equipment=None, weapon:Equipment=None):
        self.name = "Armor_"+str(numArm)
        self.head = head
        self.chest = chest
        self.back = back
        self.pants = pants
        self.weapon = weapon
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
        
    # def dequip(self, position):

    # def details(self):

    def printToFile(self):
        with open(self.name+".json", "w") as oFile:
            json.dump(self.__dict__, oFile)

    # def export(self):

