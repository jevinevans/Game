#include "Includes/Functions.h"
void SECTIONDIV()
{
	cout << endl <<  "--------------------------------------" << endl << endl;
}

int main()
{	

	LinkedList<int>* numTest = new LinkedList<int>();

	numTest->appendNode(25);
	numTest->appendNode(50);
	numTest->appendNode(90);
	numTest->appendNode(40);
	numTest->appendNode(30);
	numTest->appendNode(75);
	cout << endl;
	numTest->display();

	delete numTest;

	const char* filename= "./Data/TempEList.txt";
	LinkedList<Equipment*> *inventory = new LinkedList<Equipment*>();
	LinkedList<Equipment*> Weps;
	
	cout << "Reading Equipment in and printing names..." << endl;
	readEquipment(inventory, filename);
	
	for(int i = 1; i <= inventory->getLength(); i++)
		cout << inventory->getNodeValue(i)->getName() << endl;
	
	SECTIONDIV();
	
	// Prints FULL DETAIL OF EQUIPEMENT
	// for(int i = 1; i <= inventory->getLength();i++)
	// 	inventory->getNodeValue(i)->PRINT();

	//Armor Class Test of Equipment
	Armor<Equipment*> body;

	//Loading Equipment into Armor

	for(int i = 1; i <= inventory->getLength(); i++)
	{
		body.equip(inventory->getNodeValue(i));
		if(inventory->getNodeValue(i)->getIT() == 4)
			Weps.appendNode(inventory->getNodeValue(i));
	}
//Test
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
	cout << "Weapons Length: " << Weps.getLength() << endl;

	body.PRINT();
	
	body.dequip(0, true); //12/29/18 - Need to change the way things are dequiped because when i delete it, it is deleted from the LinkedList.
	
	body.PRINT();
	
	body.equip(Weps.getNodeValue(1));
	body.PRINT();
	
	Equipment* temp = Weps.getNodeValue(2);

	//body.change(temp, Weps.getNodeValue(2)->getIT());

	body.stats();
	
	body.dequip(4, true);
	body.PRINT();
	body.dequip(3, true);
	body.PRINT();
	
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
	cout << "Test Completed" << endl;
	cout << "Finished" << endl;
	return 0;
}