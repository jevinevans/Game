
all	:	RolesTest

RolesTest	:	CodeTest_3Classes.o
							g++ -o CodeTest_3ClassesTest.exe CodeTest_3Classes.o

CodeTest_3Classes.o	:	CodeTest_3Classes.cpp
							g++ -I ./ -c CodeTest_3Classes.cpp

clean :	CodeTest_3ClassesTest.exe
		del *.o
		del *.exe
