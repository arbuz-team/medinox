#! /bin/bash

python3 $(dirname $0)/setting/script/update_language.py
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/main.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/product.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/root.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/sites.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/translator.json
python3 $(dirname $0)/manage.py loaddata $(dirname $0)/setting/data/user.json
