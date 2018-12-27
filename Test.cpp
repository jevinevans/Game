#include "Functions.h"

int main()
{	
	const char* filename= "./Data/EquipmentList.txt";

	LinkedList<Equipment*> *inventory = new LinkedList<Equipment*>();
	
	readEquipment(inventory, filename);

	for(int i = 1; i <= inventory->getLength(); i++)
		cout << inventory->getNodeValue(i)->getName() << endl;
	
	//Armor Class Test of Equipment
	Armor<Equipment*> body;
	
	body.isFull();
	//Loading Equipment into Armor
	for(int i = 1; i <= inventory->getLength(); i++)
		body.equip(inventory->getNodeValue(i));
	
	Equipment *weapon = inventory->getNodeValue(3);
	Equipment *weapon1 = inventory->getNodeValue(4);

	body.PRINT();
	
	body.dequip(0);
	
	body.PRINT();
	
	body.equip(weapon);
	body.PRINT();
	
	body.change(weapon1, 0);

	body.stats();
	
	body.isFull();	//not printing out needs to be worked on  ++++++++++
	body.dequip(4);
	body.PRINT();
	body.dequip(3);
	body.PRINT();
	body.isFull();
	
	printToFile(inventory,filename);

	Roles *Mage = new Roles("Mage", 0, 4);
	/* Mage->addPower();
	Mage->addPower();
	cout << Mage->getNumPowers() << endl; */
	Mage->PRINT();
	
	cout << endl << endl;
	
	Mage->printPowers();

	delete weapon;
	delete weapon1;
	delete Mage;
	delete inventory;
	return 0;
}