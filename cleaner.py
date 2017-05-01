from os import listdir, path, remove
from datetime import datetime

BASE_DIR = path.dirname(path.abspath(__file__))
IMG_DIR = BASE_DIR + '/_static/tmp/'

for file in listdir(IMG_DIR):
    if path.isfile(path.join(IMG_DIR, file)):

        modification_time = path.getmtime(path.join(IMG_DIR, file))
        modification_time = datetime.fromtimestamp(modification_time)

        exist_time = datetime.now() - modification_time
        if exist_time.seconds > 86400:
            remove(path.join(IMG_DIR, file))