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
			string getName()
			{return name;}

		};
		string roleName;
		int armorType;
		/*
		ArmorType's:
		0 - Light
		1 - Medium
		2 - Heavy
		*/
		Abilities** powers;
		int current;
		int Psize;
		
		void resize()
		{
			int newSize = Psize * 2;
			Abilities** array = new Abilities*[newSize];

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
		Roles()
		{
			roleName = "New Role";
			armorType = -1;
			Psize = 5;
			powers = new Abilities*[Psize];
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
			cout << "\n===============================\n";
			cout << "Role: " << getRoleName() << endl;
			cout << "Armor Type: " << getArmorTypeName() << endl;
			cout << "-----Role Powers-----\n";
			printPowers();

			cout << "Done" << endl;
			
		}
		void addPower()
		{
			Abilities* temp;
			string n;
			int eff, ty;
			temp = new Abilities;

			cout << "\nAdding a New Power to the " + this->roleName + " Role." << endl;
			cout << "New Power Name: ";
			getline(cin, n);
			cout << endl;
			cout << "New Power Type (Magic(0) or Physical(1)): ";
			cin >> ty;
			cout << endl;
			cout << "New Power Effect: ";
			cin >> eff;
			while(eff < 0 or eff > 1000)
			{
				cout << "Error: Please enter a number from 0 - 1000: ";
				cin >> eff;
			}
			cin.ignore();
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
			cout << "Start" << endl;
			Abilities* pow;
			for(int i = 0; i < current; i++)
			{
				cout << i << endl;
				pow = powers[i];
				cout << i << endl;
				string nom = pow->name;
				
				cout << "Power " << i+1 << ":\n";
				cout << "\tName: " << nom << endl;
				cout << "\tType: ";

				if(pow->type == 0)
					cout << "Magic Attack" << endl;
				else
					cout << "Physical Attack" << endl;

				cout << "\tEffect" << pow->effect << endl << endl;
				
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
		int getNumPowers()
		{
			return current;
		}
		Roles::Abilities** getPowers()
		{
			return powers;
		}
	
};


#endif