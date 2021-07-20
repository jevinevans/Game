#/bin/sh

#Variables
REPORT="TEST_REPORT.txt"
TODAY=$(date)

echo -e "######TESTING REPORT######\n\nDate: $TODAY \n\n---UNITTEST---\n" > $REPORT

python -m unittest tests/test* -v 2>> $REPORT

echo -e "\n---Flake 8----\n" >> $REPORT

flake8 --count --format=pylint . >> $REPORT

less $REPORT
