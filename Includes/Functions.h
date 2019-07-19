#ifndef FUNCTIONS_H
#define FUNCTIONS_H


#include "Armor.h"
#include "Roles.h"
#include "LinkedList.h"

#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

void printToFile(LinkedList<Equipment*>*, const char*);
void printToFile(LinkedList<Roles*>*, const char*);
void readEquipment(LinkedList<Equipment*>*, const char* file);
void readRoles(Roles**, const char* file);
//void sortEquipment();
#endif