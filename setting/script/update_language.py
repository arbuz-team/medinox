import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(BASE_DIR))


def Convert_To_Json(file_path, model_name):

    file = open(BASE_DIR + file_path, encoding='utf-8')
    lines = file.read().splitlines()
    file.close()
    json = []

    for line in lines:

        number = line.split(':')[0]
        text = line.split(':')[1].replace('"', '\\"')

        json.append('{"model": "%s", "pk": %s, "fields": {"value": "%s"}}'
                    % (model_name, number, text))

    return ', '.join(json)


def Save_Result(json_list):

    file_name = '{0}/setting/data/translator.json'\
        .format(BASE_DIR)

    os.system('rm {0}'.format(file_name))
    file = open(file_name, encoding='utf-8', mode='w')
    file.write('[{0}]'.format(', '.join(json_list)))
    file.close()



json_en = Convert_To_Json('/translator/language/EN', 'translator.language_en')
json_pl = Convert_To_Json('/translator/language/PL', 'translator.language_pl')
# json_de = Convert_To_Json('/translator/language/DE', 'translator.language_de')
Save_Result([json_en, json_pl])
