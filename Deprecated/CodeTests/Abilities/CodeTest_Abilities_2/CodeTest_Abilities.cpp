#include "../../../Includes/Abilities.h"

int main()
{
    Abilities* a = new Abilities("Strike", 1, 50);
    Abilities* b = new Abilities("Cool Blast", 0, 75);
    Abilities* c = new Abilities("Knifed", 1, 500);
    Abilities* d = new Abilities("Dark Light", 0, 80);
    
    ofstream file;
    file.open("..\\..\\_Code_Results\\CodeTest_Abilities_2_FilePrint_Results.txt");

    cout << "Print the following to the Results File" << endl;
    
    a->PRINT();
    b->PRINT();
    c->PRINT();
    d->PRINT();

    a->printToFile(file);
    b->printToFile(file);
    c->printToFile(file);
    d->printToFile(file);

    file.close();
    delete a;
    delete b;
    delete c;
    delete d;

    cout << "DONE" << endl;

    return 0;
}