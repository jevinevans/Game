cls

@echo off

make CodeTests 2> CodeTestErrors.txt

@echo off

CodeTestErrors.txt

cd ./Tests/Equipment/
EquipmentTest.exe > "../Code Results/EquipmentResults.txt"

cd ../Roles/
RolesTest.exe < TestCase_Roles.txt > "../Code Results/RolesResults.txt"

cd ../Code Results/
EquipmentResults.txt
RolesResults.txt

cd ../..

