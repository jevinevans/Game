#/bin/sh

#Variables
REPORT="TEST_REPORT.txt"
OUTPUT="TEST_OUTPUT.txt"
TODAY=$(date)

echo -e "######TESTING REPORT######\n\nDate: $TODAY \n\n---PYTEST---\n" > $REPORT

printf "\n*****Running Tests*****\n"
poetry run pytest --cov=funclg/ --cov-branch tests/ --disable-pytest-warnings >> $REPORT
printf "*****DONE*****\n"

# echo -e "\n---Flake 8----\n" >> $REPORT

# IGNS="E231,E266,E401,E501,W293"

# flake8 --ignore=$IGNS --count ./funclg | sort >> $REPORT

poetry run python Scan_Directories.py

echo -e "\n---Code Quality Report---\n" >> $REPORT
echo -e "\n-----BANDIT-----\n" >> $REPORT
echo -e "\n-----BANDIT-----\n"
poetry run bandit -rq -ii -ll ./funclg &>> $REPORT
echo -e "\n-----PYLINT-----\n" >> $REPORT
echo -e "\n-----PYLINT-----\n"
poetry run pylint ./funclg &>> $REPORT
# echo -e "\n-----PYRIGHT-----\n" >> $REPORT
# echo -e "\n-----PYRIGHT-----\n"
# export NODE\_OPTIONS=--experimental-worker
# poetry run pyright ./funclg &>> $REPORT

echo -e "\n-----SAFETY-----\n"
poetry run safety scan >> $REPORT
