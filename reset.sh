#! /bin/bash

python3 $(dirname $0)/manage.py migrate cart zero
python3 $(dirname $0)/manage.py migrate main zero
python3 $(dirname $0)/manage.py migrate payment zero
python3 $(dirname $0)/manage.py migrate catalog zero
python3 $(dirname $0)/manage.py migrate product zero
python3 $(dirname $0)/manage.py migrate root zero
python3 $(dirname $0)/manage.py migrate sender zero
python3 $(dirname $0)/manage.py migrate session zero
python3 $(dirname $0)/manage.py migrate statement zero
python3 $(dirname $0)/manage.py migrate translator zero
python3 $(dirname $0)/manage.py migrate user zero

python3 $(dirname $0)/manage.py migrate
bash $(dirname $0)/load.sh