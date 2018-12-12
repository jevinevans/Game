#ifndef EQUIPMENT_H
#define EQUIPMENT_H

#include <iostream>
#include <fstream>
using namespace std;

class Equipment
{
	private:
		string name;				//Item Name
		int IT;						//Item Types: 0 - Weapon, 1 - Helmet, 2 - Chest, 3 - Pants,
		int AT;						//Armor Types: 0 - Light,1 - Medium,2 - Heavy
		int WT;						//Weapon Types: 0 - NULL, 1 - Wand, 2 - Sword, 3 - Knief
		int level;					//Item Level
		string desc;				//Description of Item
		int abilityPts;				//The amount of protection or damage a item can cause
	
	public:
		Equipment()				//Creates a blank weapon object
		{
			name = "NULL";
			IT = -1;
			AT = -1;
			WT = -1;
			level = -1;
			desc = "NULL";
			abilityPts = -1;
		}
		
		Equipment(string na, int it, int at, int wt, int le, string de, int aP)					//Creates a new Equipment object based on passed parameters
		{
			name = na;
			IT = it;
			AT = at;
			WT = wt;
			level = le;
			desc = de;
			abilityPts = aP;
		}
		
		
		void PRINT()
		{
			cout << "\n------------------------ ";
			cout << "\n Name: " << getName();
			cout << "\n Type: ";
			getItemType();
			cout << "\n Level: " << getLevel();
			cout << "\n Description: " << getDesc();
			cout << "\n Ability Points: " << getAbilityPts();
			
			if(IT == 0)
				cout << " ATK" << endl << endl;
			else
			cout << " DEF" << endl << endl;
		}

		void getItemType()
		{
			string item;
			switch(IT)
			{
				case 0:
					switch(WT)
					{
						case 0:
							item += "Knief";
							break;
						case 1:
							item += "Wand";
							break;
						case 2:
							item += "Sword";
							break;
						case 3:
							item += "";
							break;
					}
					break;
				case 1:
					item += "Helmet";
					break;
				case 2:
					item += "Chestplate";
					break;
				case 3:
					item += "Pants";
					break;
				default:
					item = "";
					break;
			}
			
			if( IT != 0)
			{
				switch(AT)
				{
					case 0:
						item = "Light " + item;
						break;
					case 1:
						item = "Medium " + item;
						break;
					case 2:
						item = "Heavy " + item;
						break;
				}
			}
			cout << item;
			}
		/*
			Function: printToFile
			Parameters: Ofstream reference variable
			Purpose: To print the data of a equipment object to a file that is passed in.
		*/
		void printToFile(ofstream &File)
		{
			cout << "Printing " << this->name << " to file" << endl;
			File << name << ",";
			File << IT << ",";
			File << AT << ",";
			File << WT << ",";
			File << level << ",";
			File << desc << ",";
			File << abilityPts << endl;
			cout << "Done with " << this->name << endl;
		}	
		
		
		void setName(string n){name = n;}
		void setIT(int i){IT = i;}
		void setAT(int a){AT = a;}
		void setWT(int w){WT = w;}
		void setLevel(int l){level = l;}
		void setDesc(string d){desc = d;}
		void setAbilityPts(int a){abilityPts = a;}
		
		string getName() const {return name;}
		int getIT() const{return IT;}
		int getAT() const {return AT;}
		int getWT() const {return WT;}
		int getLevel() const {return level;}
		string getDesc() const {return desc;}
		int getAbilityPts() const {return abilityPts;}
	
	
	
	
};


#endif