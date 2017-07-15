#! /bin/bash

find . -path "$(dirname $0)/*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "$(dirname $0)/*/migrations/*.pyc"  -delete

COMMAND=""
COMMAND="$COMMAND DROP DATABASE medinox;"
COMMAND="$COMMAND CREATE DATABASE medinox CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
echo $COMMAND | python3 $(dirname $0)/manage.py dbshell

python3 $(dirname $0)/manage.py makemigrations cart
python3 $(dirname $0)/manage.py makemigrations main
python3 $(dirname $0)/manage.py makemigrations payment
python3 $(dirname $0)/manage.py makemigrations catalog
python3 $(dirname $0)/manage.py makemigrations product
python3 $(dirname $0)/manage.py makemigrations root
python3 $(dirname $0)/manage.py makemigrations sender
python3 $(dirname $0)/manage.py makemigrations session
python3 $(dirname $0)/manage.py makemigrations translator
python3 $(dirname $0)/manage.py makemigrations user

python3 $(dirname $0)/manage.py migrate
bash $(dirname $0)/load.sh