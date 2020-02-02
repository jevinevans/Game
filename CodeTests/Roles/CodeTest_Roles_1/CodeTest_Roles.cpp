/*
7/23/2019 -- This test case is considered a failure and a new test case will be drafted up this is left for records and hopefully will be able to be used as reference and recovered to become a valid test
    Test Code for Abilities Class
	- Creation (1)
	- PRINT (1)
	- printToFile (1)
	- setters (3)
	- getters (3)
	
	Test Code for Roles Class
	- Creation (2)
	- Deletion (1)
	- PRINT (1)
	- addPower (2)
	- removePower (2)
	- printPowers (1)
	- printToFile (1)
	- Resize (1) ?
	- setters (2)
	- getters (5)
	
    Total: 27 Test
*/

//Need to find a way to send copies of pointers and not the pointer itself

#include "../../../Includes/Functions.h"

int main()
{
	LinkedList<Abilities*>* Powers  = new LinkedList<Abilities*>();
	
	int numAbilities = 0;
	Abilities** pows;
	Abilities* ability = new Abilities("Stab", 1, 52);
    Abilities staticAbility("FireBlast", 0, 78);
    
    staticAbility.PRINT();
	ability->PRINT();
	
    ofstream kfile;
    kfile.open("Stab.txt");
    ability->printToFile(kfile);
    kfile.close();

    kfile.open("Fireblast.txt");
    staticAbility.printToFile(kfile);
    kfile.close();

	Powers->appendNode(ability);

    for(int i = 1; i <= Powers->getLength();i++)
        Powers->getNodeValue(i)->PRINT();

	
	Roles* Mage = new Roles("Mage", 1, 2);
	Roles* Warrior = new Roles("Warrior", 2, 1);
	Roles* Thief = new Roles("Thief",0,1);
	

    //-----Testing Pointer Value Copying-----//
    Abilities* tempS = Powers->getNodeValue(1);
    Abilities* temp = tempS;

    cout << Powers->getNodeValue(1) << endl;
    cout << tempS << endl;
    cout << temp << endl;

    //--------------------------------------//

	Mage->addPower(temp);
	Mage->addPower();
    Mage->addPower();

    Warrior->addPower();

    /* Thief->setRoleName("Thief");
    Thief->setArmorType(0);*/
    Thief->addPower(ability);

    //Test///
        ability->PRINT();
        Abilities** test = Thief->getPowers();

    for(int i = 0; i < Thief->getNumPowers(); i++)
        test[i]->setDamageEffect(99);


    Thief->PRINT();

    Warrior->PRINT();

    Mage->PRINT();
    Mage->removePower();
    cout << Mage->getNumPowers() << endl;

    cout << Thief->getRoleName() << endl;
    cout << Thief->getArmorTypeName() << " " << Thief->getArmorType() << endl;
    cout << Thief->getNumPowers() << " Powers" << endl;
    Thief->printPowers();

   

    /* Isssue with LinkedList and print Thief, 
    pows = Mage->getPowers();
    for(int i = 0; i < Mage->getNumPowers(); i++)
        Powers->appendNode(pows[i]);

    pows = Warrior->getPowers();
    for(int i = 0; i < Warrior->getNumPowers(); i++)
        Powers->appendNode(pows[i]);

    pows = Thief->getPowers();
    for(int i = 0; i < Thief->getNumPowers(); i++)
        Powers->appendNode(pows[i]);

    Classes->appendNode(Mage);
    Classes->appendNode(Warrior);
    Classes->appendNode(Thief);
    
    for(int i = 1; i <= Classes->getLength(); i++)
        Classes->getNodeValue(i)->PRINT();
	*/
    const char* PowerFile = "../_TestFiles/PowersTest.txt";
    const char* RolesFile = "../_TestFiles/RolesTest.txt";

    ofstream file;
    file.open(RolesFile);
    Mage->printToFile(file);
    Warrior->printToFile(file);
    file.close();

    //Test issue with printing ability out to file
    ofstream nfile;
    nfile.open("Ability.txt");
    ability->printToFile(nfile);
    nfile.close();
/*  
    file.open(PowerFile);
    for(int i = 1; i <= Powers->getLength(); i++)
    {
        Powers->getNodeValue(i)->printToFile(file);
        file << endl;
    }
    file.close();

    file.open(RolesFile);
    for(int i = 1; i <= Classes->getLength(); i++)
    {
        Classes->getNodeValue(i)->printToFile(file);
        file << endl;
    }
    file.close(); 
*/
    cout << Powers->getLength() << endl;
	delete ability;
	delete Mage;
	delete Warrior;
	delete Thief;
    
    
	delete Powers;

    cout << "Test Complete" << endl;

    return 0;	
}
