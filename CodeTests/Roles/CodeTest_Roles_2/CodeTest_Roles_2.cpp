/*
This is to test three classes with the same ability
*/

#include "../../../Includes/Functions.h"

---- BROKEN TEST -----

int main()
{
    LinkedList<Roles*> *Classes = new LinkedList<Roles*>();

    Abilities* ability = new Abilities("Stab", 1, 52);

    Classes->appendNode(new Roles("Thief",0,1));
    Classes->appendNode(new Roles("Mage",1,1));
    Classes->appendNode(new Roles("Warrior",2,1));

    for(int i = 1; i <= Classes->getLength(); i++)
    {    
        ability->setDamageEffect(ability->getDamageEffect()*i);
        Classes->getNodeValue(i)->addPower(ability);
    }

    for(int i = 1; i <= Classes->getLength(); i++)
    {
        Classes->getNodeValue(i)->PRINT();
    }

    for(int i = 1; i <= Classes->getLength(); i++)
        delete Classes->getNodeValue(i);

    delete ability;
    delete Classes;
    cout << "Test Complete" << endl;
    return 0;
}