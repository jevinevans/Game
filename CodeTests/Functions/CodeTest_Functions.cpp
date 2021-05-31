#include "../../Includes/Functions.h"

const char* EQUIP_FILE = "./Equipment_Print_Results.txt";

int main()
{
    //Testing printToFile (Equipment)
    cout << "----- printToFile(Equipment) -----" << endl;
    
    // Create equipment to print to file
    Equipment* wep1 = new Equipment("Test Sword", 4,1,2,5,"Simple persons sword", 50);
    Equipment* wep2 = new Equipment("Test Knife", 4,1,3,6,"Simple persons Knief", 50);
    Equipment* wep3 = new Equipment("Test Wand", 4,1,1,7,"Simple persons Wand", 50);

    // Create list to store equipment items
    LinkedList<Equipment*>* inventory = new LinkedList<Equipment*>();
    
    // Adding Equipment to linkedlist
    inventory->appendNode(wep1);
    inventory->appendNode(wep2);
    inventory->appendNode(wep3);

    try
    {
        try
        {
            if (inventory->getLength() != 3)
            {
                throw inventory->getLength();
            }
        }
        catch(int length)
        {
            cout << "LinkedList length incorrect: it is " << length << " and should be 3." << endl;
            cout << "Exiting for other error" << endl;
            delete wep1;
            delete wep2;
            delete wep3;
            delete inventory;
            cout << "printToFile (Equipment) -----> failed" << endl;
        }
        cout << "Inventory Length: " << inventory->getLength() << endl; //Remove

        printToFile(inventory, EQUIP_FILE);

        ifstream f(EQUIP_FILE);
        if(!f.good())
            throw EQUIP_FILE;

        cout << "printToFile (Equipment) -----> passed" << endl;
    }
    catch(const char* file)
    {
        cout << file << " does not exist and was not created" << endl;
        cout << "printToFile (Equipment) -----> failed" << endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        cout << "MAJOR ERROR" << endl;
        cout << "printToFile (Equipment) -----> failed" << endl;
    }
    delete wep1;
    delete wep2;
    delete wep3;
    delete inventory;
    //Testing printToFile (Roles)
    //Testing readEquipment
    //Test readRoles
    cout << "Finished Testing" << endl;
    return 0;
}