#ifndef ROLES_H
#define ROLES_H

#include <iostream>
#include "Abilities.h"
using namespace std;

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
			cout << "Resizing Powers" << endl;
			int newSize = Psize * 2;
			Abilities** array = new Abilities*[newSize];

			for(int i = 0; i < current; i++)
			{
				array[i] = powers[i];
			}

			delete [] powers;

			powers = array;
			Psize = newSize;
			
		}
		void removePower(int n)
		{
			Abilities* abs;
			
			cout << "\nRemoving Power "<< n << ": " << powers[n - 1]->getName() << " from the users powers list.";

			abs = powers[n-1];

			for(int i = n - 1; i < current - 1; i++)
			{
				powers[i] = powers[i+1];
			}

			powers[current-1] = NULL;
			
			current--;

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
			Psize = 1;
			powers = new Abilities*[Psize];
			current = 0;
		}
		~Roles()
		{
			cout << "Deleting Role: " << this->roleName << endl;
			for(int i = 0; i < current; i++)
			{
				if(powers[i] == NULL)
					continue;

				cout << "Deleting Power: " << powers[i]->getName() << endl;
				delete powers[i];
			}
			delete [] powers;
			cout << "Deletion Done" << endl;
		}
		void PRINT()
		{
			cout << "\n===============================\n";
			cout << "Role: " << getRoleName() << endl;
			cout << "Armor Type: " << getArmorTypeName() << endl;
			cout << "-----Role Powers-----\n";
			if(current)
			{
				for(int i=0; i < current; i++)
				{
					cout << "Power " << i+1 << ": ";
					powers[i]->PRINT();
				}
			}
			else
				cout << "\tThere are no powers." << endl;
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

			cout << temp->getName() << " has been added to the " << this->roleName << " abilities." << endl;

			current++;

		}
		void addPower(Abilities* ability)
		{
			if(current == Psize)
				resize();

			powers[current] = ability;
			cout << ability->getName() << " has been added to " << this->roleName << " role." << endl;
			current++;
		}
		void removePower()
		{
			int n = -1;
			cout << "Deleting a Power" << endl << "-------------------------"<< endl;
			printPowers();
			cout << "\nPlease choose a number from 1 - " << current << ": ";
			cin >> n; 

			while(n < 1 || n > current)
			{
				char again = ' ';
				cout << "\nThat is an invalid Power..." << endl << "Do you want to try again? (y or n) : ";
				cin >> again; 

				if(again == 'N' || again == 'n')
					return;
				
				cout << endl;
				printPowers();
				cout << "\nPlease choose a number from 1 - " << current << ": ";
				cin >> n; 
			}

			removePower(n); //Calls private method;
			cout << "\n\nCurrent ";
			printPowers();
			cout << endl << endl;
		}
		void printPowers()
		{
			if(current)
			{
				cout << "Powers List" << endl << "---------------" << endl;
				for(int i = 0; i < current; i++)
				{				
					cout << "Power " << i+1 << ": " << powers[i]->getName() << endl;
				}
			}
			else
				cout << " \nThere are no powers." << endl;
		}
		void printToFile(ofstream &File)
		{
			File << this->roleName << ",";
			File << this->armorType << ",";
			File << this->Psize << ",";
			for(int i = 0; i < current; i++)
				powers[i]->printToFile(File);
			File << endl;
			cout << "Printed Role: " << this->roleName << " to file." << endl;
		}
		void setRoleName(string n)
		{
			this->roleName = n;
		}
		void setArmorType(int i)
		{
			this->armorType = i;
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