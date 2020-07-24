.PHONY: all

all	:	[Template]Test

[Template]Test	:	CodeTest_[Template].o
							g++ -o CodeTest_[Template]Test.exe CodeTest_[Template].o

CodeTest_[Template].o	:	CodeTest_[Template].cpp
							g++ -I ./ -c CodeTest_[Template].cpp

clean		:	CodeTest_[Template]Test.exe
				del *.o
				del *.exe