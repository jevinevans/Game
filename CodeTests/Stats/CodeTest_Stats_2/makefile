.PHONY: all

all	:	Stats_2Test

Stats_2Test	:	CodeTest_Stats_2.o
							g++ -o CodeTest_Stats_2Test.exe CodeTest_Stats_2.o

CodeTest_Stats_2.o	:	CodeTest_Stats_2.cpp
							g++ -I ./ -c CodeTest_Stats_2.cpp

clean		:	CodeTest_Stats_2Test.exe
				del *.o
				del *.exe