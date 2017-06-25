#! /bin/bash

rm -rf $(dirname $0)/server/manage/root/migrations
rm -rf $(dirname $0)/server/manage/session/migrations
rm -rf $(dirname $0)/server/manage/user/migrations
rm -rf $(dirname $0)/server/content/catalog/migrations
rm -rf $(dirname $0)/server/content/main/migrations
rm -rf $(dirname $0)/server/content/product/migrations
rm -rf $(dirname $0)/server/content/statement/migrations
rm -rf $(dirname $0)/server/page/cart/migrations
rm -rf $(dirname $0)/server/service/payment/migrations
rm -rf $(dirname $0)/server/service/sender/migrations
rm -rf $(dirname $0)/server/service/translator/migrations

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