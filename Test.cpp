//#include "Roles.h"
#include "Armor.h"

#include <iostream>

using namespace std;
void printToFile(Equipment**, const char*);

int main()
{
	/*
	//Equipment Creation Test
	Equipment* hat = new Equipment("Gold Cap", 1, 1, 3, 5, "Simple persons hat", 10);
	Equipment* shirt = new Equipment("Gold Chestplate", 2, 1, 3, 5, "Simple persons chestplate", 10);
	Equipment* weapon = new Equipment("Gold Sword", 0,1,2,5,"Simple persons sword", 50);
	Equipment* weapon1 = new Equipment("Gold Knief", 0,1,3,6,"Simple persons sword", 50);
	Equipment* pants = new Equipment("Gold Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);
	
	Equipment* inventory[] = {hat, shirt, weapon, weapon1, pants};
	int SIZE = 5;
	
	//Armor Class Test of Equipment
	Armor<Equipment*> body;
	
	//Loading Equipment into Armor
	for(int i = 0; i < SIZE; i++)
	body.equip(inventory[i]);
	
	body.PRINT();
	
	body.dequip(0);
	
	body.PRINT();
	
	body.equip(weapon);
	body.PRINT();
	
	body.stats();
	
	body.isFull();	//not printing out needs to be worked on  ++++++++++
	body.dequip(4);
	body.PRINT();
	body.dequip(3);
	body.PRINT();
	body.isFull();
	
	const char* filename= "./Data/TempEquipmentList.txt";
	printToFile(inventory,filename);
	
	delete hat;
	delete shirt;
	delete weapon;
	delete weapon1;
	delete pants;
	
	*/
	
	//Role Class Test
	Roles *Mage = new Roles("Mage", 0, 4);
	Mage->addPower();
	Mage->addPower();
	cout << Mage->getNumPowers() << endl;
	Mage->PRINT();
	
	delete Mage;
	
	return 0;
}

void printToFile(Equipment** inventory, const char* file)
{
	ofstream outFile;
	outFile.open(file);
	
	for(int i = 0; i < 5; i++)
		inventory[i]->printToFile(outFile);
	
	outFile.close();
	
	
	cout << "Printed to File" << endl;
}