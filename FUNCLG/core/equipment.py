#####################################################################################
#   Programmer: Jevin Evans                                                         #
#   Date: 7/13/2021                                                                 #
#   Program: Equipment Class                                                        #
#   Description: The Equipment class allows for creation of objects in the game     #
#       to be used by characters and placed inside of the armor or in other         #
#       holders/storage containers inside of the game.                              #
#####################################################################################

import json

try:
    import utils.types as uTypes
except ImportError:
    import FUNCLG.utils.types as uTypes


class Equipment():

    def __init__(self, name='', description='', armorType=None, itemType=None, weaponType=None, level=0, abilityPoints=0):
        """
            Creates an equipment item
        """
        
        self.name = name
        self.description = description
        self.armorType = armorType
        self.itemType = itemType
        self.weaponType = weaponType
        self.level = level
        self.abilityPoints = abilityPoints
        # self.stats = #STAT Object
    
    def __str__(self):
        return f"{self.name} (lvl. {self.level}) {self.getItemDescription()}"

    def details(self):
        titleLen = 2 + len(self.name)
        desc = f"\n {self.name} \n{''.join(['-' for x in range(titleLen)])}"
        desc += f"\nLevel:{self.level:3d} | Ability Pts: {self.abilityPoints} "
        desc += "ATK" if self.getItemType() == "Weapon" else "DEF"
        desc += f"\nType: {self.getItemDescription()}"
        desc += f"\nDescription: {self.description}"
        return desc

    def printToFile(self):
        with open(self.name + ".json", "w") as oFile:
            json.dump(self.__dict__, oFile)
    
    def export(self):
        return self.__dict__

    def getItemType(self):
        return uTypes.getItemType(self.itemType)
    
    def getArmorType(self):
        return uTypes.getArmorType(self.armorType)
    
    def getWeaponType(self):
        return uTypes.getWeaponType(self.weaponType)
    
    def getItemDescription(self):
        return uTypes.getItemDescription(self.itemType, self.armorType, self.weaponType)

    # def getStats(self):

# def main():
#     tempE = Equipment("excelsior", "This is a temp example is used to describe a simple sword.", itemType=4, weaponType=0, level=52, abilityPoints=500)
#     print(tempE)

#     print(tempE.__dict__)
#     print()
#     print(tempE.export())
