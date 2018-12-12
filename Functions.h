#ifndef FUNCTIONS_H
#define FUNCTIONS_H


#include "Armor.h"
#include "Roles.h"

#include <iostream>
using namespace std;

void printToFile(Equipment**, const char*, int);
void readRoles(Roles** Classes, const char* file);
#endif