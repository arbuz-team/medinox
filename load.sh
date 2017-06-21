#! /bin/bash

python3 $(dirname $0)/server/manage/setting/script/update_language.py
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/main.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/root.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/sites.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/catalog.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/product.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/translator.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/user.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/manage/setting/data/payment.json
