#/bin/sh

#Variables
REPORT="TEST_REPORT.txt"
TODAY=$(date)

echo -e "######TESTING REPORT######\n\nDate: $TODAY \n\n---UNITTEST---\n" > $REPORT

printf "\n*****Running Unittest*****\n"
poetry run python -m unittest tests/test* -v 2>> $REPORT
printf "*****DONE*****\n"

printf "\n*****Running Black formatter*****\n"
black ./FUNCLG
printf "*****DONE*****\n"

printf "\n*****Running Isort*****\n"
isort ./FUNCLG
printf "*****DONE*****\n"

echo -e "\n---Flake 8----\n" >> $REPORT

IGNS="E231,E266,E401,E501,W293"

flake8 --ignore=$IGNS --count ./FUNCLG | sort >> $REPORT

poetry run python Scan_Directories.py
