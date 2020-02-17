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
		int gender;				// 0--Male; 1--Female
		bool dead;
		int HP;
		int MP;
		int level;
		int EXP;
		int DEF;
		int ATK;
		int armorType;
		Armor<Equipment*>* body;
		Roles* role;
		
	public:
		Character()
		{
			this->name = "NEW_CHARACTER";
			this->gender = -1;
			this->level = 0;
			this->EXP = 0;
			this->HP = 1;
			this->MP = 1;
			this->DEF = 10;
			this->ATK = 10;
			this->armorType = -1;
			body = new Armor<Equipment*>;
			
			
		}
		Character(string name, int gender /*Add the rest of the needed calls*/)
		{}
		~Character()
		{}
	
};


#endif