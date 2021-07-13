cls

@echo off

make CodeTests 2> CodeTestErrors.txt

@echo off

CodeTestErrors.txt

cd ./CodeTests/Abilities/
REM run.bat

rem NOT MADE YET
rem cd ../Armor/
rem run.bat

cd ../Equipment
run.bat

cd ../Roles/CodeTest_Roles_1
run.bat

cd ../CodeTest_Roles_2
run.bat

cd ../../Code Results/
*.txt

cd ../..

