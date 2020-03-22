#ifndef ARMOR_H
#define ARMOR_H

#include "Equipment.h"
#include <iostream>
using namespace std;

const int ITEMMAX = 4;

template<typename TYPE>
class Armor
{
	private:
		struct Slot
		{
			bool empty;
			TYPE value;
			
			bool isEmpty()
			{
				if(this->empty)
				{
					return true;
				}
				else
					return false;
					
			}
		};
		Slot* head;
		Slot* chest;
		Slot* weapon;
		Slot* pants;
		
	public:
		Armor()
		{
			head = new Slot;
			chest = new Slot;
			weapon = new Slot;
			pants = new Slot;
			
			head->empty = chest->empty = weapon->empty = pants->empty = true;
			
		}

		Armor(Armor* arm)
		{
			cout << "Start";
			head->value = arm->head->value;
			cout << "head";
			chest->value = arm->chest->value;
			weapon->value = arm->weapon->value;
			pants->value = arm->pants->value;

			head->empty = chest->empty = weapon->empty = pants->empty = false;
		}
		
		~Armor()
		{
			delete head->value;
			delete head;
			delete chest->value;
			delete chest;
			delete weapon->value;
			delete weapon;
			delete pants->value;
			delete pants;
		}
		
		void equip(TYPE v)
		{
		
			TYPE t = new Equipment(v);
			Slot* temp;
			temp = new Slot;
			temp->value = t;
			temp->empty = false;
			
			switch(temp->value->getIT())
			{
				case 1:
					if(!head->isEmpty())
						dequip(1, false);
					head = temp;
					break;
				case 2:
					if(!chest->isEmpty())
							dequip(2, false);
					chest = temp;
					break;
				case 3:
				if(!pants->isEmpty())
						dequip(3, false);
					pants = temp;
					break;
				case 4:
				if(!weapon->isEmpty())
						dequip(4, false);
					weapon = temp;
					break;
			}
			cout << "Equipped: " << temp->value->getName() << endl;
		}
		void isFull()			//not working and will not print off 
		{
			if(!head->isEmpty() and !chest->isEmpty() and !weapon->isEmpty() and !pants->isEmpty())
				cout << "!!!---Fully Equipped---!!!" << endl;
			else
			{
				if(head->isEmpty())
					cout << "The head slot is empty" << endl;
				if(chest->isEmpty())
					cout << "The chest slot is empty" << endl;
				if(weapon->isEmpty())
					cout << "The weapon slot is empty" << endl;
				if(pants->isEmpty())
					cout << "The pants slot is empty" << endl;
			}
		}

		void dequip(int o, bool print)
		{
			if(o > ITEMMAX)
			{
				cout << "Slot does not exist" << endl;
				return;
			}
			Slot* temp;
			temp = new Slot();
			string tname = "";

			switch(o)
			{
				case 1:
					tname = "Head";
					if(!head->isEmpty())
					{
						temp->value = head->value;
						head->value = NULL;
						head->empty = true;
						tname = temp->value->getName();
					}
					break;
				case 2:
					tname = "Chest";
					if(!chest->isEmpty())
					{
						temp->value = chest->value;
						chest->value = NULL;
						chest->empty = true;
						tname = temp->value->getName();
					}
					break;
				case 3:
					tname = "Pants";
					if(!pants->isEmpty())
					{
						temp->value = pants->value;
						pants->value = NULL;
						pants->empty = true;
						tname = temp->value->getName();
					}
					break;
				case 4:
					tname = "Weapon";
					if(!weapon->isEmpty())
					{	
						temp->value = weapon->value;
						weapon->value = NULL;
						weapon->empty = true;
						tname = temp->value->getName();
					}
					break;
			}
			if(print)
				cout << "Dequipped: " << tname << endl;
			delete temp;
		}
		
		
		void stats()
		{
			cout << "\n----------------------\n|     ARMOR STATS    |\n----------------------";
			
			cout << "\nHead: ";
			if(!head->isEmpty())
				cout << head->value->getStats();
			else
				cout << "Empty";
			
			cout << "\nChest: ";
			if(!chest->isEmpty())
				cout << chest->value->getStats();
			else
				cout << "Empty";
			
			cout << "\nWeapon: ";
			if(!weapon->isEmpty())
				cout << weapon->value->getStats();
			else
				cout << "Empty";
			
			cout << "\nPants: ";
			if(!pants->isEmpty())
				cout << pants->value->getStats();
			else
				cout << "Empty";
			cout << endl << endl;
		}
		
		void PRINT()
		{
			cout << "\n-------------------------\n|   ARMOR DESCRIPTION   |\n-------------------------\n";
			
			cout << "\tHEAD";
			if(!head->isEmpty())
				head->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "\tCHEST";
			if(!chest->isEmpty())
				chest->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "\tWEAPON";
			if(!weapon->isEmpty())
				weapon->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "\tPANTS";
			if(!pants->isEmpty())
				pants->value->PRINT();
			else
				cout << " is not equipped." << endl;

			cout << endl;
		}
		
		Slot* getHead(){return head;}
		Slot* getChest(){return chest;}
		Slot* getWeapon(){return weapon;}
		Slot* getPants(){return pants;}
		
		void setHead(TYPE h){head = h;}
		void setWeapong(TYPE w){weapon = w;}
		void setChest(TYPE c){chest = c;}
		void setPants(TYPE p){pants = p;}
		
		string getName(){return "Armor";}
};


#endif