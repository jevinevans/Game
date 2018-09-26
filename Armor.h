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
		}
		void isFull()			//not working and will not print off 
		{
			if(!head->isEmpty() and !chest->isEmpty() and !weapon->isEmpty() and !pants->isEmpty())
				cout << "!!!---Fully Equipped---!!!" << endl;
		}
		void change(TYPE v) // May not need or may just make dequip a private function and use this to allow the character to change equipment - 7/5/2018
		{
			//could take a new item, dequip the old and add the new in ??? 7/5/2018
			TYPE temp = this.value;
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
			switch(o)
			{
				case 0:
					temp->value = weapon->value;
					weapon->value = NULL;
					weapon->empty = true;
					break;
				case 1:
					temp->value = head->value;
					head->value = NULL;
					head->empty = true;
					break;
				case 2:
					temp->value = chest->value;
					chest->value = NULL;
					chest->empty = true;
					break;
				case 3:
					temp->value = pants->value;
					pants->value = NULL;
					pants->empty = true;
					break;
			}
			cout << "Unequiped: " << temp->value->getName() << endl << endl;
			delete temp->value;
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
				head->value->PRINT();
			cout << "Chest";
				chest->value->PRINT();
			cout << "Weapon";
				weapon->value->PRINT();
			cout << "Pants";
				pants->value->PRINT();
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