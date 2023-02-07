echo "-----ISORT-----"
poetry run isort $1
echo "-----BLACK-----"
poetry run black $1
echo "-----BANDIT-----"
poetry run bandit -rq -ii -ll $1
echo "-----XENON-----"
poetry run xenon --max-absolute B $1
echo "-----PYLINT-----"
poetry run pylint $1
# echo "-----PYRIGHT-----"
# export NODE\_OPTIONS=--experimental-worker
# poetry run pyright $1

