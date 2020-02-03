#Makefile For Test

all	:		Test

Test	:		Test.o Functions.o
			g++ -o Test.exe Test.o Functions.o
				
				
Test.o	:	Test.cpp
				g++ -I ./Includes/ -c Test.cpp

Functions.o	:	Functions.cpp
					g++ -I ./Includes/ -c Functions.cpp

CodeTests	:
	make -C CodeTests

clean		:	Test.exe
				del *.o
				del *.exe