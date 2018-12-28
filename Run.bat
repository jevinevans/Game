make clean

cls

make 2> TestErrors.txt

Test.exe > TestResults.txt 2>TestLogicErrors.txt

TestErrors.txt
TestResults.txt