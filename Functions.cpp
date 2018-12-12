#include "Armor.h"
#include "Roles.h"

void printToFile(Equipment** inventory, const char* file, int SIZE)
{
	cout << "Opening File: " << file << endl;
	ofstream outFile;
	outFile.open(file);
	
	for(int i = 0; i < SIZE; i++)
		inventory[i]->printToFile(outFile);
	
	cout << "Done" << endl;
	outFile.close();
	
	
	cout << "Printed to File" << endl;
	
}

void readRoles(Roles** Classes, const char* file)
{
	
}