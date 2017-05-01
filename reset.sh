#! /bin/bash

python3 $(dirname $0)/manage.py makemigrations cart
python3 $(dirname $0)/manage.py makemigrations main
python3 $(dirname $0)/manage.py makemigrations payment
python3 $(dirname $0)/manage.py makemigrations product
python3 $(dirname $0)/manage.py makemigrations root
python3 $(dirname $0)/manage.py makemigrations sender
python3 $(dirname $0)/manage.py makemigrations session
python3 $(dirname $0)/manage.py makemigrations statement
python3 $(dirname $0)/manage.py makemigrations translator
python3 $(dirname $0)/manage.py makemigrations user

python3 $(dirname $0)/manage.py migrate
bash $(dirname $0)/load.sh