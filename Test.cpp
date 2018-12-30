#include "Functions.h"

int main()
{	
	const char* filename= "./Data/TempEList.txt";
	LinkedList<Equipment*> *inventory = new LinkedList<Equipment*>();
	LinkedList<Equipment*> Weps;
	
	//Add to CodeTest_Functions.cpp
	readEquipment(inventory, filename);
	
	for(int i = 1; i <= inventory->getLength(); i++)
		cout << inventory->getNodeValue(i)->getName() << endl;
	
	cout << endl << endl;
	
	for(int i = 1; i <= inventory->getLength();i++)
		inventory->getNodeValue(i)->PRINT();

	cout << endl << endl;
	//Armor Class Test of Equipment
	Armor<Equipment*> body;
	
	body.isFull();
	//Loading Equipment into Armor

	for(int i = 1; i <= inventory->getLength(); i++)
	{
		body.equip(inventory->getNodeValue(i));
		if(inventory->getNodeValue(i)->getIT() == 0)
			Weps.appendNode(inventory->getNodeValue(i));
	}

/*
	Issues with putting equipment node value into an array going to try
	and fix another day need to complete more objects, for now just going 
	to use new linkedlist to hold values


	cout << "There are " << wepCount << " weapons" << endl;
	Equipment** Weps = new Equipment*[wepCount];
	Equipment* temp;

	Weps[0]->PRINT();

	for(int i = 1; i <= inventory->getLength();i++)
	{
		if(inventory->getNodeValue(i)->getIT() == 0)
		{	
			temp = inventory->getNodeValue(i);
			temp->PRINT();
			Weps[i-1] = temp;
		}
	}
	 
	cout << "------------------" << endl;
	for(int i = 0; i < wepCount; i++)
		Weps[i]->PRINT();
	cout << "------------------" << endl; 
*/
	cout << Weps.getLength() << endl;

	body.PRINT();
	
	body.dequip(0); //12/29/18 - Need to change the way things are dequiped because when i delete it, it is deleted from the LinkedList.
	
	body.PRINT();
	
	body.equip(Weps.getNodeValue(1));
	body.PRINT();
	
	Equipment* temp = Weps.getNodeValue(2);

	//body.change(temp, Weps.getNodeValue(2)->getIT());

	body.stats();
	
	body.isFull();	//not printing out needs to be worked on  ++++++++++
	body.dequip(4);
	body.PRINT();
	body.dequip(3);
	body.PRINT();
	body.isFull();
	
	//inventory->getNodeValue(4)->PRINT();

	printToFile(inventory,filename);

	Roles *Mage = new Roles("Mage", 0, 4);
	/* Mage->addPower();
	Mage->addPower();
	cout << Mage->getNumPowers() << endl; */
	Mage->PRINT();
	
	cout << endl << endl;
	
	Mage->printPowers();

	delete Mage;
	delete inventory;
	return 0;
}