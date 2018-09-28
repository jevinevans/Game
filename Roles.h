#ifndef ROLES_H
#define ROLES_H

#include <iostream>
using namespace std;

class Roles
{
	private:
		struct Abilities
		{
			string name;
			int effect;		//amount of damage per attack
			int type;		//Class type 
			/*
				Class Types
					0 - Magical
					1 - Physical
			*/
		};
		string roleName;
		int armorType;
		/*
		ArmorType's:
		0 - Light
		1 - Medium
		2 - Heavy
		*/
		Abilities* powers[];
		int current;
		int Psize;
		
		void resize()
		{
			int newSize = Psize * 2;
			Abilities* array = new Abilities*[newSize];

			for(int i = 0; i < current; i++)
			{
				array[i] = powers[i];
			}

			delete [] powers;

			powers = array;
			Psize = newSize;
			
			delete [] array;
		}
		
	public:
		Roles(string rn, int aT, int s)
		{
			roleName = rn;
			armorType = aT;
			Psize = s;
			powers = new Abilities*[Psize];
			current = 0;

		}
		Roles(int s)
		{
			this->Psize = s;
			powers = new Abilities*[this->Psize];
			current = 0;
		}
		~Roles()
		{
			Abilities* delPow;
			for(int i = 0; i < Psize; i++)
			{
				delPow = powers[i];
				delete delPow;
			}
			delete [] powers;
		}
		void PRINT()
		{
			cout << "Role: " << getRoleName() << endl;
			cout << "===============================\n";
			cout << "Armor Type: " << getArmorTypeName() << endl;
			cout << "-----Role Powers-----\n";
			printPowers();
			
			
		}
		void addPower()
		{
			Abilities* temp;
			string n;
			int eff, ty;
			temp = new Abilities;

			cout << "Adding a New Power" << endl;
			cout << "New Power Name: ";
			getline(cin, n);
			cout << endl;
			cout << "New Power Type (Magic(0) or Physical(1)): ";
			cin >> ty;
			cout << endl;
			cout << "New Power Effect: ";
			cin >> eff;
			cout << endl;

			temp->name = n;
			temp->type = ty;
			temp->effect = eff;

			if(current == Psize)
				resize();
			
			powers[current] = temp;

			cout << temp->name << " has been added to your abilities." << endl;

			current++;

		}
		void printPowers()
		{
			for(int i = 0; i < current; i++)
			{
				cout << "Power " << i+1 << ":\n";
				cout << "\tName: " << powers[i]->name << endl;
				cout << "\tType: ";

				if(powers[i]->type == 0)
					cout << "Magic Attack" << endl;
				else
					cout << "Physical Attack" << endl;

				cout << "\tEffect" << powers[i]->effect << endl << endl;
				
			}
		}
		setRoleName(string n)
		{
			roleName = n;
		}
		setArmorType(int i)
		{
			armorType = i;
		}
		string getRoleName()
		{
			return roleName;
		}
		int getArmorType()
		{
			return armorType;
		}
		string getArmorTypeName()
		{
			string aName;
			switch(armorType)
				{
					case 0:
						aName = "Light Armor";
						break;
					case 1:
						aName = "Medium Armor";
						break;
					case 2:
						aName = "Heavy Armor";
						break;
				}
			return aName;
		}
		
		Roles::Abilities* getPowers()
		{
			return powers;
		}
	
};


#endif