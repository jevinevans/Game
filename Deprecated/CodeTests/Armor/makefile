.PHONY: all clean

all	:	CodeTest_Armor

CodeTest_Armor	:	CodeTest_Armor.o
							g++ -o CodeTest_Armor.exe CodeTest_Armor.o

CodeTest_Armor.o	:	CodeTest_Armor.cpp
							g++ -I ./ -c CodeTest_Armor.cpp

clean :	CodeTest_Armor.exe
		del *.o
		del CodeTest_Armor.exe