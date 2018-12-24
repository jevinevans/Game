#ifndef FUNCTIONS_H
#define FUNCTIONS_H


#include "Armor.h"
#include "Roles.h"
#include "LinkedList.h"

#include <iostream>
using namespace std;

void printToFile(LinkedList<Equipment*>*, const char*, int);
void readEquipment(Equipment**, const char* file);
void readRoles(Roles**, const char* file);
#endif