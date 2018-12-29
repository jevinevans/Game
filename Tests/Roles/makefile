
all	:	RolesTest

RolesTest	:	CodeTest_Roles.o
							g++ -o RolesTest.exe CodeTest_Roles.o

CodeTest_Roles.o	:	CodeTest_Roles.cpp
							g++ -I ./ -c CodeTest_Roles.cpp

clean :	RolesTest.exe
		del *.o
		del RolesTest.exe
