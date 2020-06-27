#Makefile For Test

all	:		FUNCLG

FUNCLG	:		FUNCLG.o Functions.o
			g++ -o FUNCLG.exe FUNCLG.o Functions.o
				
				
FUNCLG.o	:	FUNCLG.cpp
				g++ -I ./Includes/ -c FUNCLG.cpp

Functions.o	:	Functions.cpp
					g++ -I ./Includes/ -c Functions.cpp

CodeTest	:
	make -C CodeTest

clean		:	FUNCLG.exe
				del *.o
				del *.exe

