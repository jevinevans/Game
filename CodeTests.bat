cls

make CodeTests 2> CodeTestErrors.txt

CodeTestErrors.txt

cd ./Tests/Equipment/
EquipmentTest.exe > "../Code Results/EquipmentResults.txt"
move EquipmentResults.txt ../Code Results/


cd ../Code Results/
EquipmentResults.txt

cd ../..

