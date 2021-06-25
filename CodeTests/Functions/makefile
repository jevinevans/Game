.PHONY: all clean

all	:	FunctionsTest

FunctionsTest	:	CodeTest_Functions.o Functions.o
							g++ -o CodeTest_FunctionsTest.exe CodeTest_Functions.o Functions.o

CodeTest_Functions.o	:	CodeTest_Functions.cpp
							g++ -I ./ -c CodeTest_Functions.cpp

Functions.o : ../../Functions.cpp
				g++ -I ../../Includes/ -c ../../Functions.cpp

clean		:	CodeTest_FunctionsTest.exe
				del *.o
				del *.exe