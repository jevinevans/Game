cls

@echo off

make CodeTests 2> CodeTestErrors.txt

@echo off

rem Add conditional for if CodeTestErrors is not empty so that we do not attempt to compile

CodeTestErrors.txt

rem Need to update file name locations

cd ./Tests/Equipment/
EquipmentTest.exe > "../Code Results/EquipmentResults.txt"

cd ../Roles/
RolesTest.exe < TestCase_Roles.txt > "../Code Results/RolesResults.txt"

cd ../Code Results/
EquipmentResults.txt
RolesResults.txt

cd ../..

