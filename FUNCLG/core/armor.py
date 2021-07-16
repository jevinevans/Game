#####################################################################################   
#   Programmer: Jevin Evans                                                         #
#	Date: 7/15/2021                                                                 #
#	Program: Armor Class                                                            #
#   Description: The Armor class is made to store equipment itmes for a character.  #      
#####################################################################################

import json
from core.equipment import Equipment

class Armor():

    def __init__(self, head:Equipment=None, chest:Equipment=None, back:Equipment=None, pants:Equipment=None, weapon:Equipment=None):
        self.head = head
        self.chest = chest
        self.back = back
        self.pants = pants
        self.weapon = weapon

    def __str__(self):
        temp = "Armor: <"
        temp += "H:1, " if self.head else "H:0, "
        temp += "C:1, " if self.chest else "C:0, "
        temp += "B:1, " if self.back else "B:0, "
        temp += "P:1, " if self.pants else "P:0, "
        temp += "W:1>" if self.weapon else "W:0>"
        return temp

    def equip(self, item:Equipment):
        
    # def details(self):

    def printToFile(self):
        with open(self.name+".json", "w") as oFile:
            json.dump(self.__dict__, oFile)
            
    # def export(self):

