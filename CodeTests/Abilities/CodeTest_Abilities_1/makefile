.PHONY: all clean

all	:	CodeTest_Abilities

CodeTest_Abilities	:	CodeTest_Abilities.o
							g++ -o CodeTest_Abilities.exe CodeTest_Abilities.o

CodeTest_Abilities.o	:	CodeTest_Abilities.cpp
							g++ -I ./ -c CodeTest_Abilities.cpp

clean :	CodeTest_Abilities.exe
		del *.o
		del CodeTest_Abilities.exe