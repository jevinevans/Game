#include "../../Includes/Stats.h"

using namespace std;

int main()
{
    Stats* blankConstr = new Stats();

    blankConstr->setHPMAX(500);
    blankConstr->setHPNOW(230);
    blankConstr->setMPMAX(300);
    blankConstr->setMPNOW(250);
    blankConstr->setStrength(50);
    blankConstr->setSpeed(33);
    blankConstr->setIntel(40);

    Stats* fullConstr = new Stats(100, 150, 60, 43, 52);
    Stats* copyConstr = new Stats(blankConstr);

    copyConstr->levelup(.25);
    copyConstr->levelup(.25);

    cout << "Blank Construct\n"; blankConstr->PRINT();
    cout << "Full Consytruct\n"; fullConstr->PRINT();
    cout << "70% Increase of Full -> Copy\n"; copyConstr->PRINT();
    
    cout << "\nPoint Damage Test: 20pt" << endl;
    fullConstr->damage(20, false);
    fullConstr->PRINT();

    cout << "Partial Heal Test: 10pt" << endl;
    fullConstr->heal(10, false);
    fullConstr->PRINT();

    cout << "\nPercentage Damage Test: 50%" << endl;
    fullConstr->damage(50, true);
    fullConstr->PRINT();

    cout << "\nFull Percentage Heal Test: 100%" << endl;
    fullConstr->heal(100, true);
    fullConstr->PRINT();

    cout <<"\nFull Heal Test: 1000pts heal after 75pt damage" << endl;
    fullConstr->damage(75, false);
    fullConstr->PRINT();
    fullConstr->heal(1000, false);
    fullConstr->PRINT();

    delete blankConstr;
    delete fullConstr;
    delete copyConstr;

    return 0;
}