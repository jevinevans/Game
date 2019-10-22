all	:	ArmorTest

ArmorTest	:	CodeTest_Armor.o
							g++ -o ArmorTest.exe CodeTest_Armor.o

CodeTest_Armor.o	:	CodeTest_Armor.cpp
							g++ -I ./ -c CodeTest_Armor.cpp

clean :	ArmorTest.exe
		del *.o
		del ArmorTest.exe