#include "Functions.h"

void printToFile(LinkedList<Equipment*> *inventory, const char* file, int SIZE)
{
	cout << "Opening File: " << file << endl;
	ofstream outFile;
	outFile.open(file);
	
	for(int i = 1; i <= inventory->getLength(); i++)
		inventory->getNodeValue(i)->printToFile(outFile);
	
	cout << "Done" << endl;
	outFile.close();
	
	
	cout << "Printed to File" << endl;
	
}
void readEquipment(Equipment** Items, const char* file)
{
	string name;				
	int IT;
	int AT;
	int WT;
	int level;
	string desc;
	int abilityPts;

	ifstream inFile;
	inFile.open(file);
	if(inFile.good())
	{

	}
}
void readRoles(Roles** Classes, const char* file)
{
	
}