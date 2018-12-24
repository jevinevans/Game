/*
    Test Code for Equipment Class
    - Creation(2)
    - Print(1)
    - getItemType(1)
    - printToFile(1)
    - setters(7)
    - getters(7)

    Total: 19 Test
*/

#include "Functions.h"

int main()
{
	//Equipment Creation Test
	Equipment* hat = new Equipment("Gold Cap", 1, 1, 3, 5, "Simple persons hat", 10);
	Equipment* shirt = new Equipment("Gold Chestplate", 2, 1, 3, 5, "Simple persons chestplate", 10);
	Equipment* weapon = new Equipment("Gold Sword", 0,1,2,5,"Simple persons sword", 50);
	Equipment* weapon1 = new Equipment("Gold Knief", 0,1,3,6,"Simple persons sword", 50);
	Equipment* pants = new Equipment("Gold Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);
	
	Equipment* inventory[] = {hat, shirt, weapon, weapon1, pants};
	int SIZE = 5;
	
	
	delete hat;
	delete shirt;
	delete weapon;
	delete weapon1;
	delete pants;
	
	return 0;
}