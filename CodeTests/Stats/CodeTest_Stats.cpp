#include "../../Includes/Stats.h"

using namespace std;

int main()
{
    Stats testStat = new Stats();

    testStat.setHPMAX(500);
    testStat.setHPNOW(230);
    testStat.setMPMAX(300);
    testStat.setMPNOW(250);

    cout << "HP: " << testStat.getHPNOW() << "/" << testStat.getHPMAX() << endl;  
    cout << "MP: " << testStat.getMPNOW() << "/" << testStat.getMPNOW() << endl;

    return 0;
}