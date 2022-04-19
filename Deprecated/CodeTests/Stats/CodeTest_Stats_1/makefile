.PHONY: all clean

all	:	StatsTest

StatsTest	:	CodeTest_Stats.o
							g++ -o CodeTest_StatsTest.exe CodeTest_Stats.o

CodeTest_Stats.o	:	CodeTest_Stats.cpp
							g++ -I ./ -c CodeTest_Stats.cpp

clean		:	CodeTest_StatsTest.exe
				del *.o
				del *.exe