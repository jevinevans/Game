#Makefile For Test

all	:		Test

Test:		Test.o
			g++ -o Test.exe Test.o
				
				
Test.o	:	Test.cpp
				g++ -I ./ -c Test.cpp

				

clean		:	Test.exe
				del *.o
				del Test.exe