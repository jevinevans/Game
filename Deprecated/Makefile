#Makefile For Test
.PHONY: all CodeTest CodeTestClean clean

all	:		FUNCLG

FUNCLG	:		FUNCLG.o Functions.o
			g++ -o FUNCLG.exe FUNCLG.o Functions.o
				
				
FUNCLG.o	:	FUNCLG.cpp
				g++ -I ./Includes/ -c FUNCLG.cpp

Functions.o	:	Functions.cpp
					g++ -I ./Includes/ -c Functions.cpp

clean		:	FUNCLG.exe
				del *.o
				del *.exe

