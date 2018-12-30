#ifndef ARMOR_H
#define ARMOR_H

#include "Equipment.h"
#include <iostream>
using namespace std;

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
			Slot* temp;
			temp = new Slot;
			temp->value = v;
			temp->empty = false;
			int place = temp->value->getIT();
			
			switch(place)
			{
				case 0:
					weapon = temp;
					break;
				case 1:
					head = temp;
					break;
				case 2:
					chest = temp;
					break;
				case 3:
					pants = temp;
					break;
			}
			cout << "Equipped: " << temp->value->getName() << endl << endl;
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
		void change(TYPE v, int spot)
		{
			cout << "start" << endl;
			cout << "Changing Current to: " << v->getName();
			dequip(spot);
			cout << "Done";
			cout << v->getName();
			equip(v);
		}
		void dequip(int o)
		{
			if(o > 3)
			{
				cout << "Slot does not exist" << endl;
				return;
			}
			Slot* temp;
			temp = new Slot();
			string tname = "nothing";

			switch(o)
			{
				case 0:
					if(!weapon->isEmpty())
					{	
						temp->value = weapon->value;
						weapon->value = NULL;
						weapon->empty = true;
						tname = temp->value->getName();
						delete temp->value;
					}
					else
						cout << "There is nothing equipped." << endl;
					break;
				case 1:
					if(!head->isEmpty())
					{
						temp->value = head->value;
						head->value = NULL;
						head->empty = true;
						tname = temp->value->getName();
						delete temp->value;
					}
					else
						cout << "There is nothing equipped." << endl;
					break;
				case 2:
					if(!chest->isEmpty())
					{
						temp->value = chest->value;
						chest->value = NULL;
						chest->empty = true;
						tname = temp->value->getName();
						delete temp->value;
					}
					else
						cout << "There is nothing equipped." << endl;
					break;
				case 3:
					if(!pants->isEmpty())
					{
						temp->value = pants->value;
						pants->value = NULL;
						pants->empty = true;
						tname = temp->value->getName();
						delete temp->value;
					}
					else
						cout << "There is nothing equipped." << endl;
					break;
			}
			cout << "Unequipped " << tname << "." << endl << endl;
			delete temp;
		}
		
		
		void PRINT()
		{
			cout << "ARMOR\n-----------------------";
			
			cout << "\nHead: ";
			if(!head->isEmpty())
				cout << head->value->getName();
			else
				cout << "This Slot is Empty";
			
			cout << "\nChest: ";
			if(!chest->isEmpty())
				cout << chest->value->getName();
			else
				cout << "This Slot is Empty";
			
			cout << "\nWeapon: ";
			if(!weapon->isEmpty())
				cout << weapon->value->getName();
			else
				cout << "This Slot is Empty";
			
			cout << "\nPants: ";
			if(!pants->isEmpty())
				cout << pants->value->getName();
			else
				cout << "This Slot is Empty";
			cout << endl << endl;
		}
		
		void stats()
		{
			cout << "\nARMOR STATISTIS\n------------------------\n------------------------\n";
			
			cout << "Head";
			if(!head->isEmpty())
				head->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "Chest";
			if(!chest->isEmpty())
				chest->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "Weapon";
			if(!weapon->isEmpty())
				weapon->value->PRINT();
			else
				cout << " is not equipped." << endl;
			
			cout << "Pants";
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
		void setWeapong(TYPE w){weapon =w;}
		void setChest(TYPE c){chest = c;}
		void setPants(TYPE p){pants = p;}
	
};


#endif