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

const char* ARMOR_FILE = "./Armor_Print_Results.txt";

bool fullArmorCheck(Armor<Equipment*>* arm)
{  
    bool success = true;

    if(arm->getHead() == NULL)
        success = false;
    if(arm->getChest() == NULL)
        success = false;
    if(arm->getPants() == NULL)
        success = false;
    if(arm->getWeapon() == NULL)
        success = false;

    return success;
}

Armor<Equipment*>* constructorTest(Equipment* head, Equipment* chest, Equipment* weapon, Equipment* pants)
{
    // Test Constructor, setters
    
    // Create Armor
    Armor<Equipment*>* arm = new Armor<Equipment*>();
    try
    {
        arm->setHead(head);
        arm->setChest(chest);
        arm->setPants(pants);
        arm->setWeapon(weapon);
    }
    catch(const std::exception& e)
    {
        cout << e.what() << '\n';
        cout << "ERROR: Armor creation or setter issue" << endl;
    }

    return arm;
}

bool copyContructorTest(Armor<Equipment*> arm)
{
    // Test Copy Constructor
    Armor<Equipment*>* copyArm = new Armor<Equipment*>(arm);

    return fullArmorCheck(copyArm);
}

// bool equipTest()
// {

// }
// bool dequipTest()
// {

// }
// bool printToFileTest(Armor<Equipment*>* arm)
// {

// }

int main()
{
    int passed, failed = 0;
    cout << "----- Armor.h CodeTest -----" << endl;

    Equipment* head = new Equipment("Brave Cap", 1, 1, 0, 5, "Simple persons hat", 10);
	Equipment* chest = new Equipment("Brave Chestplate", 2, 1, 0, 5, "Simple persons chestplate", 10);
	Equipment* wep1 = new Equipment("Brave Sword", 4,1,2,5,"Simple persons sword", 50);
	Equipment* wep2 = new Equipment("Charming Wand", 4,1,1,7,"Simple persons Wand", 50);
	Equipment* pants = new Equipment("Brave Trousers", 3, 1, 3, 5, "Simple persons trousers", 10);

    Armor<Equipment*>* arm = constructorTest(head, chest, wep1, pants);

    cout << "\tConstructor (Blank): ";
    if(fullArmorCheck(arm))
    {
        cout << "Passed!" << endl;
        passed++;
    }
    else
    {
        cout << "Failed!" << endl;
        failed++;
    }

    cout << "\tConstructor (Copy): ";
    if(copyContructorTest(arm))
    {
        cout << "Passed!" << endl;
        passed++;
    }
    else
    {
        cout << "Failed!" << endl;
        failed++;
    }

//----------------------

    cout << "\nTesting Equip Method" << "\n----------------------" << endl;


    // myBody->equip(hat);
    // myBody->equip(shirt);

    // myBody->stats();

    // myBody->equip(weapon1);
    // myBody->equip(pants);

    // cout << "\nTesting Print Method" << "\n----------------------" << endl;
    // myBody->PRINT();

    // delete hat;
    // delete shirt;

    // delete pants;
    // // Removing Items
    // myBody->dequip(4, true);
    // myBody->equip(weapon3);
    
    // cout << "\nTesting stats Method" << "\n----------------------" << endl;
    // myBody->stats();

    // cout << "\nTesting Copy Constructor" << "\n----------------------" << endl;
    // Armor<Equipment*>* myBody2 = new Armor<Equipment*>(myBody);

    // cout << "\nSecond Armor" << endl;
    // myBody2->stats();

    // cout << "\nChanging Second Armor and Printing Both Armors" << endl;
    // myBody2->equip(weapon1);
    // myBody->dequip(2, true);

    // cout << "Armor 2" << endl;
    // myBody2->stats();
    // cout << "Armor 1" << endl;
    // myBody->stats();
    

    delete head;
    delete chest;
    delete pants;
    delete wep1;
    delete wep2;
    delete arm;

    cout << "-----ARMOR TEST COMPLETED-----" << endl;
    return 0;
}