#include "../../../Includes/Stats.h"

using namespace std;

int main()
{
    cout << "Testing Stats Class" << endl;

    cout << "\nTesting Constructors: Blank, Full, and Copy" << endl;
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

    cout << "\nBlank Construct\n"; blankConstr->PRINT();
    cout << "Full Consytruct\n"; fullConstr->PRINT();
    cout << "70% Increase of Full -> Copy\n"; copyConstr->PRINT();

    cout << "\nBegin damage and heal Tests\n";
    //HP TESTS  
    cout << "\nPoint Damage Test: 20pt" << endl;
    fullConstr->damage(20, false);
    fullConstr->PRINT();

    cout << "Partial Heal Test: 10pt" << endl;
    fullConstr->heal(10, false);
    fullConstr->PRINT();

    cout << "\nPercentage Damage Test: 50%" << endl;
    fullConstr->damage(50, true);
    fullConstr->PRINT();

    cout << "\nFull Percentage Heal Test: 100%";
    fullConstr->heal(100, true);
    fullConstr->PRINT();

    cout <<"\nFull Heal Test: 1000pts heal after 75pt damage";
    fullConstr->damage(75, false);
    fullConstr->PRINT();
    fullConstr->heal(1000, false);
    fullConstr->PRINT();

    //MP TESTS
    cout << "\nBegin mpUse and mpRestore Tests\n";
    cout << "\nPoint Mana Test: 20pt";
    fullConstr->mpUse(20, false);
    fullConstr->PRINT();

    cout << "\nPartial MP Restore Test: 10pt";
    fullConstr->mpRestore(10, false);
    fullConstr->PRINT();

    cout << "\nPercentage MP Use Test: 50%";
    fullConstr->mpUse(50, true);
    fullConstr->PRINT();

    cout << "\nFull Percentage MP restore Test: 100%";
    fullConstr->mpRestore(100, true);
    fullConstr->PRINT();

    cout <<"\nFull MP Restore Test: 1000pts MP restore after 75pt Using MP";
    fullConstr->mpUse(75, false);
    fullConstr->PRINT();
    fullConstr->mpRestore(1000, false);
    fullConstr->PRINT();

    cout << "\nTesting getAllStats function\n" << endl;
    int* fullStat = fullConstr->getAllStats();
    int* copyStat = copyConstr->getAllStats();

    for(int i = 0; i < 7; i++)
        cout << fullStat[i] << endl;

    for(int i = 0; i < 7; i++)
        cout << copyStat[i] << endl;

    cout << "\nTesting Adding of Stats\n";

    Stats* combined = new Stats();
    combined->addStats(fullConstr);
    combined->addStats(copyConstr);
    combined->PRINT();
    combined->levelup(.25);
    combined->PRINT();

    cout << "\nTesting Removing of Stats\n";
    cout << "Combined Stats is currently" << endl;
    combined->PRINT();
    cout << "Now removing the stats from fullConstr from Combined" << endl;
    fullConstr->PRINT();
    cout << "Results\n----------" << endl;
    combined->removeStats(fullConstr);
    combined->PRINT();

    delete blankConstr;
    delete fullConstr;
    delete copyConstr;

    cout << endl << "Test Complete" << endl;
    return 0;
}