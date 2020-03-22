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
    cout << "ARMOR TEST" << endl << "----------------------" << endl << endl;
    Armor<Equipment*>* myBody = new Armor<Equipment*>();

    Equipment* hat = new Equipment("Brave Cap", 1, 1, 0, 5, "Simple persons hat", 10);
	Equipment* shirt = new Equipment("Brave Chestplate", 2, 1, 0, 5, "Simple persons chestplate", 10);
	Equipment* weapon1 = new Equipment("Brave Sword", 4,1,2,5,"Simple persons sword", 50);
	Equipment* weapon3 = new Equipment("Charming Wand", 4,1,1,7,"Simple persons Wand", 50);
	Equipment* pants = new Equipment("Brave Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);

    cout << "Testing Equip" << "----------------------" << endl;
    



    return 0;
}