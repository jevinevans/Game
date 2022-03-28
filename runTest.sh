#/bin/sh

#Variables
REPORT="TEST_REPORT.txt"
OUTPUT="TEST_OUTPUT.txt"
TODAY=$(date)

echo -e "######TESTING REPORT######\n\nDate: $TODAY \n\n---PYTEST---\n" > $REPORT

printf "\n*****Running Tests*****\n"
poetry run pytest --cov=FUNCLG/ tests/ >> $REPORT
printf "*****DONE*****\n"

echo -e "\n---Flake 8----\n" >> $REPORT

IGNS="E231,E266,E401,E501,W293"

flake8 --ignore=$IGNS --count ./FUNCLG | sort >> $REPORT

poetry run python Scan_Directories.py

echo -e "\n---Code Quality Report---\n" >> $REPORT
echo -e "\n-----ISORT-----\n" >> $REPORT
echo -e "\n-----ISORT-----\n"
poetry run isort ./FUNCLG &>> $REPORT
echo -e "\n-----BLACK-----\n" >> $REPORT
echo -e "\n-----BLACK-----\n"
poetry run black ./FUNCLG &>> $REPORT
echo -e "\n-----BANDIT-----\n" >> $REPORT
echo -e "\n-----BANDIT-----\n"
poetry run bandit -rq -ii -ll ./FUNCLG &>> $REPORT
echo -e "\n-----XENON-----\n" >> $REPORT
echo -e "\n-----XENON-----\n"
poetry run xenon --max-absolute B ./FUNCLG &>> $REPORT
echo -e "\n-----PYLINT-----\n" >> $REPORT
echo -e "\n-----PYLINT-----\n"
poetry run pylint ./FUNCLG &>> $REPORT
echo -e "\n-----PYRIGHT-----\n" >> $REPORT
echo -e "\n-----PYRIGHT-----\n"
poetry run pyright ./FUNCLG &>> $REPORT