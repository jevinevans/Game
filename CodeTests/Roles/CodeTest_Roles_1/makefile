
all	:	RolesTest

RolesTest	:	CodeTest_Roles.o
							g++ -o CodeTest_Roles.exe CodeTest_Roles.o

CodeTest_Roles.o	:	CodeTest_Roles.cpp
							g++ -I ./ -c CodeTest_Roles.cpp

clean :	CodeTest_Roles.exe
		del *.o
		del *.exe
