#include "Functions.h"

int main()
{	
	const char* filename= "./Data/EquipmentList.txt";
	LinkedList<Equipment*> *inventory = new LinkedList<Equipment*>();
	
	//Add to CodeTest_Functions.cpp
	readEquipment(inventory, filename);
	
	for(int i = 1; i <= inventory->getLength(); i++)
		cout << inventory->getNodeValue(i)->getName() << endl;
	
	//Armor Class Test of Equipment
	Armor<Equipment*> body;
	
	body.isFull();
	//Loading Equipment into Armor
	int wepCount = 0;

	cout << "Items Count is: " << inventory->getLength() << endl;
	cout << inventory->getNodeValue(inventory->getLength())->getName();

	for(int i = 1; i <= inventory->getLength(); i++)
	{
		body.equip(inventory->getNodeValue(i));
		if(inventory->getNodeValue(i)->getIT() == 0)
			wepCount++;
	}

	Equipment** Weps = new Equipment*[wepCount];

	for(int i = 1; i <= inventory->getLength();i++)
	{
		if(inventory->getNodeValue(i)->getIT() == 0)
			Weps[i-1] = inventory->getNodeValue(i);
	}
	

	body.PRINT();
	
	body.dequip(0);
	
	body.PRINT();
	
	body.equip(Weps[0]);
	body.PRINT();
	
	body.change(Weps[1], 0);

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

	delete Weps;
	delete Mage;
	delete inventory;
	return 0;
}