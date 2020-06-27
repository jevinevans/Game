#ifndef CHARACTER_H
#define CHARACTER_H

#include <iostream>
#include "Roles.h"
#include "Armor.h"

using namespace std;

class Character
{
	private:
		string name;
		char gender;				// M--Male; F-Female
		bool dead;
		int HP;
		int MP;
		int level;
		int EXP;
		int DEF;
		int ATK;
		int armorType;
		Armor<Equipment*>* body; 	//Blank new armor
		Roles* role;				//Most likely will be sent to the char based on premade role
		
	public:
		Character()
		{
			this->name = "NEW_CHARACTER";
			this->gender = 'X';
			this->level = 0;
			this->EXP = 0;
			this->HP = 1;
			this->MP = 1;
			this->DEF = 10;
			this->ATK = 10;
			body = new Armor<Equipment*>();
			role = new Roles();
			this->armorType = role->getArmorType();
			
		}
		Character(string name, int gender, int level, int EXP, int HP, int MP, int DEF, int ATK, Roles* role, Armor<Equipment*>* body)
		{
			// When adding a role, char need to get the armor type from the role then create a validation function so that when the character tries to add/equip an item it varifies on the top level versus later on 
		}
		// Character()
		~Character()
		{
			delete body;
			delete role;
		}
		void validation()
		{

		}
		bool addRole()
		{

		}
		bool addFullArmor()
		{
			
		}
};


#endif