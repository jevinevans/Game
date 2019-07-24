
all	:	EquipmentTest

EquipmentTest	:	CodeTest_Equipment.o
							g++ -o CodeTest_EquipmentTest.exe CodeTest_Equipment.o

CodeTest_Equipment.o	:	CodeTest_Equipment.cpp
							g++ -I ./ -c CodeTest_Equipment.cpp
clean		:	CodeTest_EquipmentTest.exe
				del *.o
				del *.exe