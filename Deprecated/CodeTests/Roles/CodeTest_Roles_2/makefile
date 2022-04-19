
all	:	RolesTest

RolesTest	:	CodeTest_Roles_2.o
							g++ -o CodeTest_Roles_2Test.exe CodeTest_Roles_2.o

CodeTest_Roles_2.o	:	CodeTest_Roles_2.cpp
							g++ -I ./ -c CodeTest_Roles_2.cpp

clean :	CodeTest_Roles_2Test.exe
		del *.o
		del *.exe
