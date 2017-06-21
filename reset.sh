#! /bin/bash

rm -rf $(dirname $0)/server/cart/migrations
rm -rf $(dirname $0)/server/main/migrations
rm -rf $(dirname $0)/server/payment/migrations
rm -rf $(dirname $0)/server/catalog/migrations
rm -rf $(dirname $0)/server/product/migrations
rm -rf $(dirname $0)/server/root/migrations
rm -rf $(dirname $0)/server/sender/migrations
rm -rf $(dirname $0)/server/session/migrations
rm -rf $(dirname $0)/server/statement/migrations
rm -rf $(dirname $0)/server/translator/migrations
rm -rf $(dirname $0)/server/user/migrations

python3 $(dirname $0)/manage.py makemigrations cart
python3 $(dirname $0)/manage.py makemigrations main
python3 $(dirname $0)/manage.py makemigrations payment
python3 $(dirname $0)/manage.py makemigrations catalog
python3 $(dirname $0)/manage.py makemigrations product
python3 $(dirname $0)/manage.py makemigrations root
python3 $(dirname $0)/manage.py makemigrations sender
python3 $(dirname $0)/manage.py makemigrations session
python3 $(dirname $0)/manage.py makemigrations statement
python3 $(dirname $0)/manage.py makemigrations translator
python3 $(dirname $0)/manage.py makemigrations user

python3 $(dirname $0)/manage.py migrate
bash $(dirname $0)/load.sh