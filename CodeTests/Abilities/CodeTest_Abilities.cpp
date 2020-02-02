#include "../../Includes/Abilities.h"

int main()
{
    Abilities* a = new Abilities("Strike", 1, 50);
    Abilities* b = new Abilities();
    Abilities* c = new Abilities(b);

    ofstream file;
    file.open(".\\AbilitiesList.txt");

    cout << "Created Abilities" << endl;
    
    a->PRINT();
    b->PRINT();
    c->PRINT();

    cout << "Editing Ability" << endl;
    b->setAbilityType(0);
    b->setName("Fireball");
    b->setDamageEffect(100);
    c->setName("Ability C");


    cout << "Printing Abilities" << endl;
    b->PRINT();
    c->PRINT();

    a->printToFile(file);
    b->printToFile(file);

    delete a;
    delete b;
    delete c;

    cout << "DONE" << endl;

    return 0;
}