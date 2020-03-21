/*
    Test Code for Equipment Class
    - Creation(2)
    - Print(1)
    - getItemType(1)
    - printToFile(1)
    - setters(7)
    - getters(7) - inside of PRINT method

    Total: 19 Test
*/

#include "../../Includes/Functions.h"

int main()
{
	/*
		Equipment Creation Test
		-----------------------
		1. No Argurments Constructor
		2. Full Arguments Constructor
	*/
	Equipment* hat = new Equipment("Gold Cap", 1, 1, 0, 5, "Simple persons hat", 10);
	Equipment* shirt = new Equipment("Gold Chestplate", 2, 1, 0, 5, "Simple persons chestplate", 10);
	Equipment* weapon1 = new Equipment("Gold Sword", 4,1,2,5,"Simple persons sword", 50);
	Equipment* weapon2 = new Equipment("Gold Knief", 4,1,3,6,"Simple persons Knief", 50);
	Equipment* weapon3 = new Equipment("Gold Wand", 4,1,1,7,"Simple persons Wand", 50);
	Equipment* pants = new Equipment("Gold Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);
	Equipment* blank = new Equipment();

	Equipment* EQ[] = {hat, shirt, weapon1, weapon2, weapon3, pants, blank};

	for(int i = 0; i < 7; i++)
	{
		EQ[i]->PRINT();
	}

	blank->setName("Melitas Wand");
	blank->setIT(4);
	blank->setAT(1);
	blank->setWT(1);
	blank->setLevel(6);
	blank->setDescription("Magical wand handed down through the generations of powerful white witches.");
	blank->setAbilityPts(36);

	blank->PRINT();

	const char* filename = "../_TestFiles/EquipmentTest.txt";

	ofstream file;
	file.open(filename);
	for(int i = 0; i < 7; i++)
		EQ[i]->printToFile(file);

	file.close();

	delete hat;
	delete shirt;
	delete weapon1;
	delete weapon2;
	delete weapon3;
	delete pants;
	delete blank;
	
	return 0;
}