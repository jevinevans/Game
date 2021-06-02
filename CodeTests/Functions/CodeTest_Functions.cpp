#include "../../Includes/Functions.h"

const char* EQUIP_FILE = "./Equipment_Print_Results.txt";
const char* ROLES_FILE = "./Roles_Print_Results.txt";

bool printToFileEquipmentTest()
{   
    bool success = true;
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
            success = false;
        }

        printToFile(inventory, EQUIP_FILE);

        ifstream f(EQUIP_FILE);
        if(!f.good())
            throw EQUIP_FILE;
    }
    catch(const char* file)
    {
        cout << "ERROR:" << file << " does not exist and was not created" << endl;
        success = false;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        cout << "ERROR: UNKNOWN" << endl;
        success = false;
    }
    delete wep1;
    delete wep2;
    delete wep3;
    delete inventory;
    return success;
}

bool printToFileRolesTest()
{
    bool success = true; 
    // Create Roles to print to file
    Roles* role1 = new Roles("Warrior", 2, 2);
    Roles* role2 = new Roles("Mage", 1, 2);
    Roles* role3 = new Roles("Rouge", 0, 2);
    Roles* role4 = new Roles();

    // Create list to store Roles items
    LinkedList<Roles*>* rolesList = new LinkedList<Roles*>();
    
    // Adding Roles to linkedlist
    rolesList->appendNode(role1);
    rolesList->appendNode(role2);
    rolesList->appendNode(role3);
    rolesList->appendNode(role4);

    try
    {
        try
        {
            if (rolesList->getLength() != 4)
            {
                throw rolesList->getLength();
            }
        }
        catch(int length)
        {
            cout << "LinkedList length incorrect: it is " << length << " and should be 3." << endl;
            cout << "Exiting for other error" << endl;
            success = false;
        }

        printToFile(rolesList, ROLES_FILE);
        ifstream f(ROLES_FILE);
        if(!f.good())
            throw ROLES_FILE;
    }
    catch(const char* file)
    {
        cout << "ERROR:" << file << " does not exist and was not created" << endl;
        success = false;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        cout << "ERROR: UNKNOWN" << endl;
        success = false;
    }
    delete role1;
    delete role2;
    delete role3;
    delete role4; 
    delete rolesList;
    return success;
}

int main()
{
    int passed, failed = 0;

    //Testing printToFile (Equipment)
    cout << "----- Functions.h CodeTest -----" << endl;
    if (printToFileEquipmentTest())
    {
        cout << "\tprintTofile (Equipment): Passed!" << endl;
        passed++;
    }
    else
    {
        cout << "\tprintTofile (Equipment): Failed!" << endl;
        failed++;
    }
    
    if (printToFileRolesTest())
    {
        cout << "\tprintToFile (Roles): Passed!" << endl;
        passed++;
    }
    else
    {
        cout << "\tprintToFile (Roles): Failed!" << endl;
        failed++;
    }
    
    //Testing printToFile (Roles)
    //Testing readEquipment
    //Test readRoles
    cout << "\nFinished Testing" << endl;
    cout << "Passed: " << passed << " | Failed: " << failed << endl;
    return 0;
}