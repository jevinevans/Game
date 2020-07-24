#include "../../../Includes/Stats.h"

using namespace std;

int main()
{
    cout << "STATS TEST 2" << endl;
    cout << "This test focuses on the printToFile function" << endl;

    Stats* stat1 = new Stats(100, 150, 60, 43, 53);
    Stats* stat2 = new Stats(stat1);
    Stats* stat3 = new Stats(stat1);

    stat2->levelup(.25);
    stat3->levelup(1);

    cout << "Created Stats 3 Objects" << endl;
    cout << "________________________________" << endl;
    cout << "Stats 1" << endl;
    stat1->PRINT();
    cout << "Stats 2" << endl;
    stat2->PRINT();
    cout << "Stats 3" << endl;
    stat3->PRINT();

    cout << endl << "Now Creating and Printing to File..." << endl;
    cout << "_____________________________________________________" << endl;

    ofstream file;
    file.open("..\\..\\_Code_Results\\CodeTest_Stats_2_FilePrint_Results.txt");

    stat1->printToFile(file);
    file << endl;
    stat2->printToFile(file);
    file << endl;
    stat3->printToFile(file);
    file << endl;

    file.close();
    delete stat1;
    delete stat2;
    delete stat3;
    cout << endl << "Test Completed" << endl;
    return 0;
}