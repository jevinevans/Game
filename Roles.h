#ifndef ROLES_H
#define ROLES_H

#include <iostream>
using namespace std;

class Abilities
{
	private: 
		string abilityName;
		int type;
		/*
				Class Types
					0 - Magical
					1 - Physical
		*/
		int damageEffect;
		
	public:
		Abilities(string n, int aT, int aD)
		{
			abilityName = n;
			type = aT;
			damageEffect = aD;
		}
		
		void PRINT()
		{
			cout << "\tName: " << this->abilityName << endl;
			cout << "\tType: ";

			if(this->type == 0)
				cout << "Magic Attack" << endl;
			else
				cout << "Physical Attack" << endl;

			cout << "\tEffect:" << this->damageEffect << endl << endl;
		}
		
		void setName(string n)
		{
			this->abilityName = n;
		}
		
		void setType(int t)
		{
			this->type = t;
		}
		
		void setDamageEffect(int dE)
		{
			this->damageEffect = dE;
		}
		
		string getName()
		{
			return abilityName;
		}
		
		int getType()
		{
			return type;
		}
		
		int getDamageEffect()
		{
			return damageEffect;
		}
};

class Roles
{
	private:
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
		void removePower(int n)
		{
			Abilities* abs;
			
			cout << "Removing Power "<< n << ": " << powers[n - 1]->getName() << " from the users powers list.";

			abs = powers[n-1];

			for(int i = n - 1; i < current - 1; i++)
			{
				powers[i] = powers[i+1];
			}

			delete abs;

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
			
			for(int i=0; i<current; i++)
			{
				cout << "Power " << i+1 << ":\n";
				powers[i]->PRINT();
			}
		}
		void addPower()
		{
			string n;
			int eff, ty;

			cout << "\nAdding a New Power to the " + this->roleName + " Role." << endl;
			cout << "New Power Name: ";
			getline(cin, n);
			cout << endl;
			cout << "New Power Type (Magic(0) or Physical(1)): ";
			cin >> ty;
			while(ty > 1 or ty < 0)
			{
				cout << "Retry: New Power Type (Magic(0) or Physical(1)): ";
				cin >> ty;
			}
			cout << endl;
			cout << "New Power Effect Number (0 - 1000): ";
			cin >> eff;
			while(eff < 0 or eff > 1000)
			{
				cout << "Error: Please enter a number from 0 - 1000: ";
				cin >> eff;
			}
			cin.ignore();
			cout << endl;
			
			Abilities* temp = new Abilities(n, ty, eff);

			if(current == Psize)
				resize();
			
			powers[current] = temp;

			cout << temp->getName() << " has been added to your abilities." << endl;

			current++;

		}
		void removePower()
		{
			int n = -1;
			cout << "Deleting a Power" << endl << "-------------------------"<< endl;
			printPowers();
			cout << "Please choose a number from 1 - " << current << ": ";
			cin >> n; 

			while(n < 1 || n > current)
			{
				char again = ' ';
				cout << "That is an invalid Power..." << endl << "Do you want to try again? (y or n) : ";
				cin >> again; 

				if(again == 'N' || again == 'n')
					return;
				
				cout << endl;
				printPowers();
				cout << "Please choose a number from 1 - " << current << ": ";
				cin >> n; 
			}

			removePower(n); //Calls private method;
			cout << "Current Powers" << endl;
			printPowers();
		}
		void printPowers()
		{
			cout << "\tPowers List" << endl;
			for(int i = 0; i < current; i++)
			{				
				cout << "Power " << i+1 << ":\n";
				powers[i]->PRINT();
				
			}
		}
		void setRoleName(string n)
		{
			roleName = n;
		}
		void setArmorType(int i)
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
		Abilities** getPowers()
		{
			return powers;
		}
		 
	
};
#endif