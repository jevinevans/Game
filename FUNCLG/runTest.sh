#/bin/sh

#Variables
REPORT="TEST_REPORT.txt"
TODAY=$(date)

echo -e "######TESTING REPORT######\n\nDate: $TODAY \n\n---UNITTEST---\n" > $REPORT

python -m unittest tests/test* -v 2>> $REPORT

echo -e "\n---Flake 8----\n" >> $REPORT

IGNS="E231,E266,E401,E501,W293"

flake8 --ignore=$IGNS --count . | sort >> $REPORT
