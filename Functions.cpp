// #include "Includes/Functions.h"
#include "Functions.h"

void printToFile(LinkedList<Equipment*> *inventory, const char* file)
{
	cout << "Opening File: " << file << endl;
	ofstream outFile;
	outFile.open(file);
	
	for(int i = 1; i <= inventory->getLength(); i++)
		inventory->getNodeValue(i)->printToFile(outFile);
	
	outFile << endl;
	cout << "Done" << endl;
	outFile.close();
	
	
	cout << "Printed to File" << endl;
	
}
void printToFile(LinkedList<Roles*> *Classes, const char* file)
{
	cout << "Opening File: " << file << endl;
	ofstream outFile;
	outFile.open(file);
	
	for(int i = 1; i <= Classes->getLength(); i++)
		Classes->getNodeValue(i)->printToFile(outFile);
	
	outFile << endl;
	cout << "Done" << endl;
	outFile.close();
	
	
	cout << "Printed to File" << endl;
	
}
void readEquipment(LinkedList<Equipment*> *Items, const char* file)
{
	string name, desc, line, temp;				
	int IT, AT, WT, level, abilityPts;
	Equipment* newItem;

	ifstream inFile;
	inFile.open(file);
	if(inFile.good())
	{
		getline(inFile, line);
		while(!inFile.eof())
		{
			string delim = ",";
			int pos = 0;
			
			if((pos = line.find(delim)) != string::npos)
			{
				name = line.substr(0,pos);
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos)
			{
				temp = line.substr(0,pos);
				IT = atoi(temp.c_str());
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos)
			{
				temp = line.substr(0,pos);
				AT = atoi(temp.c_str());
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos)
			{
				temp = line.substr(0,pos);
				WT = atoi(temp.c_str());
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos)
			{
				temp = line.substr(0,pos);
				level = atoi(temp.c_str());
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos)
			{
				desc = line.substr(0,pos);
				line.erase(0, pos + delim.length());
			}
			if((pos = line.find(delim)) != string::npos || line.length() != 0)
			{
				temp = line.substr(0,pos);
				abilityPts = atoi(temp.c_str());
				line.erase(0,pos + delim.length());
			}

			newItem = new Equipment(name, IT, AT, WT, level, desc, abilityPts);

			Items->appendNode(newItem);

			getline(inFile, line);
		}

	}
	inFile.close();
}
void readRoles(Roles** Classes, const char* file)
{
	string roleName, abilityName, line, temp;
	int abilityType, damageEffect, armorType, powerSize;
	Roles* newRole;

	ifstream inFile;
	inFile.open(file);
	if(inFile.good())
	{
		getline(inFile,line);
		while(!inFile.eof())
		{
			string delim = ",";
			int pos = 0;


		}
	}
}