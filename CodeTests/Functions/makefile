.PHONY: all clean

all	:	FunctionsTest

FunctionsTest	:	CodeTest_Functions.o
							g++ -o CodeTest_FunctionsTest.exe CodeTest_Functions.o

CodeTest_Functions.o	:	CodeTest_Functions.cpp
							g++ -I ./ -c CodeTest_Functions.cpp

clean		:	CodeTest_FunctionsTest.exe
				del *.o
				del *.exe