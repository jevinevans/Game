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
    cout << "ARMOR TEST" << endl << "----------------------" << endl;
    Armor<Equipment*>* myBody = new Armor<Equipment*>();

    cout << "\nTesting isFull Method" << "\n----------------------" << endl;
    myBody->isFull();

    Equipment* hat = new Equipment("Brave Cap", 1, 1, 0, 5, "Simple persons hat", 10);
	Equipment* shirt = new Equipment("Brave Chestplate", 2, 1, 0, 5, "Simple persons chestplate", 10);
	Equipment* weapon1 = new Equipment("Brave Sword", 4,1,2,5,"Simple persons sword", 50);
	Equipment* weapon3 = new Equipment("Charming Wand", 4,1,1,7,"Simple persons Wand", 50);
	Equipment* pants = new Equipment("Brave Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);

    cout << "\nTesting Equip Method" << "\n----------------------" << endl;

    myBody->equip(hat);
    myBody->equip(shirt);

    myBody->stats();

    myBody->equip(weapon1);
    myBody->equip(pants);

    cout << "\nTesting Print Method" << "\n----------------------" << endl;
    myBody->PRINT();

    delete hat;

    cout << "\nTesting isFull Method 2" << "\n----------------------" << endl;
    myBody->isFull();

    cout << "\nTesting dequip and isFull Method 3" << "\n----------------------" << endl;
    // Removing Items
    myBody->dequip(4, true);
    myBody->isFull();
    myBody->equip(weapon3);
    myBody->isFull();
    
    cout << "\nTesting stats Method" << "\n----------------------" << endl;
    myBody->stats();

    cout << "\nTesting Copy Constructor" << "\n----------------------" << endl;
    Armor<Equipment*>* myBody2 = new Armor<Equipment*>(myBody);

    cout << "\nSecond Armor" << endl;
    myBody2->stats();

    cout << "\nChanging Second Armor and Printing Both Armors" << endl;
    myBody2->equip(weapon1);

    cout << "Armor 2" << endl;
    myBody2->stats();
    cout << "Armor 1" << endl;
    myBody->stats();
    

    delete shirt;
    delete weapon1;
    delete weapon3;
    delete pants;
    delete myBody;

    cout << "-----ARMOR TEST COMPLETED-----" << endl;
    return 0;
}