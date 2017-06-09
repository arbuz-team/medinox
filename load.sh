#! /bin/bash

python3 $(dirname $0)/server/setting/script/update_language.py
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/main.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/root.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/sites.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/catalog.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/product.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/translator.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/user.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/server/setting/data/payment.json
