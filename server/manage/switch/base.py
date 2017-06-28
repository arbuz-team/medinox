from django.shortcuts import render
from django.core.urlresolvers import reverse, resolve
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from server.manage.switch.settings import *
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from datetime import date
import base64, imghdr, os, string, random, time
from enum import Enum


class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 4
    NONE = 8

class File(Enum):

    FILE = 0
    IMAGE = 1
    PDF = 2



class File_Manager:

    @staticmethod
    def Generate_Details(file_format):

        name = str(random.randrange(1000, 9999))
        if file_format: name += '.' + file_format

        path_root = '{0}/{1}'.format(MEDIA_ROOT, name)
        path_url = '{0}{1}'.format(MEDIA_URL, name)

        return [name, path_root, path_url]

    @staticmethod
    def Check_If_Image(path):

        if imghdr.what(path) in ['jpeg', 'png']:
            return True

        return False

    def Save_From_Base64_File(self):

        # get details
        name, path_root, path_url = self. \
            Generate_Details(self.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_Base64_File()

        # save file
        file = open(path_root, 'wb')
        file.write(base64.b64decode(self.base64_file))
        file.close()

        return name

    def Save_From_Base64_Image(self):

        name, path_root, path_url = self. \
            Generate_Details(self.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_Base64_Image()

        with open(path_root, 'wb') as file:
            file.write(base64.b64decode(self.base64_file))

        # if file is not image
        if not self.Check_If_Image(path_root):
            os.remove(path_root)
            name = ''

        return name

    def Save_From_Base64(self, _base64, file_name, file_type):

        self.base64_file = _base64.split(',', 1)[1]
        self.format = file_name.split('.', 1)[1] \
            if len(file_name.split('.', 1)) == 2 else ''

        if file_type == File.FILE:
            return self.Save_From_Base64_File()

        if file_type == File.IMAGE:
            return self.Save_From_Base64_Image()

    def Save_From_URL_Image(self):

        image = Image.open(self.binary_file)
        name, path_root, path_url = self. \
            Generate_Details(image.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_URL_Image()

        image.save(path_root)

        # if file is not image
        if not self.Check_If_Image(path_root):
            os.remove(path_root)
            name = ''

        return name

    def Save_From_URL_File(self):

        # get format file
        file_name = self.url.rsplit('/', 1)[-1]
        file_format = file_name.rsplit('.', 1)[-1] \
            if len(file_name.rsplit('.', 1)) > 1 else ''

        # get details
        name, path_root, path_url = self. \
            Generate_Details(file_format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_URL_File()

        # save file
        file = open(path_root, 'wb')
        file.write(self.binary_file.getvalue())
        file.close()

        return name

    def Save_From_URL(self, url, file_type):
        self.binary_file = BytesIO(urlopen(url).read())
        self.url = url

        if file_type == File.FILE:
            return self.Save_From_URL_File()

        if file_type == File.IMAGE:
            return self.Save_From_URL_Image()

    def __init__(self):
        self.format = None
        self.base64_file = None
        self.binary_file = None
        self.url = None



class Path_Manager:

    @staticmethod
    def Media_Root(file=''):
        return os.path.join(MEDIA_ROOT, file)

    @staticmethod
    def Static_Root(file=''):
        return os.path.join(STATICFILES_DIRS[0], file)

    @staticmethod
    def Static_URL(file=''):
        return os.path.join(STATIC_URL, file)



class Dynamic_Base:

    def Render_HTML(self, file_name, form_name = '', additional_form_name=''):

        # example: EN/user/sign_in.html
        template = self.request.session['translator_language'] \
                   + '/' + file_name

        self.content['form_name'] = form_name
        self.content['additional_form_name'] = additional_form_name
        return render(self.request, template, self.content)

    def Get_Urls(self, name=None, kwargs=None,
                 language=None, current_language=False):

        if not name:
            name = resolve(self.request.path_info).url_name
            kwargs = resolve(self.request.path_info).kwargs

        secure = 'https://' if self.request.is_secure() else 'http://'
        domain = self.request.get_host()

        if self.request.get_host()[:3] in ['en.', 'pl.', 'de.']:
            domain = self.request.get_host()[3:]

        urls = \
        {
            'en': secure + 'en.' + domain +
                  reverse(name, urlconf='server.manage.switch.urls.en', kwargs=kwargs),

            # 'pl': secure + 'pl.' + domain +
            #      reverse(name, urlconf='server.manage.switch.urls.pl', kwargs=kwargs),

            # 'de': secure + 'de.' + domain +
            #      reverse(name, urlconf='server.manage.switch.urls.de', kwargs=kwargs),
        }

        if language:
            return urls[language.lower()]

        if current_language:
            return urls[self.request.session['translator_language'].lower()]

        return urls

    def Get_Path(self, name=None, kwargs=None,
                 language=None, current_language=False):

        if not name:
            name = resolve(self.request.path_info).url_name
            kwargs = resolve(self.request.path_info).kwargs

        urls = \
        {
            'en': reverse(name, urlconf='server.manage.switch.urls.en', kwargs=kwargs),
            # 'pl': reverse(name, urlconf='server.manage.switch.urls.pl', kwargs=kwargs),
            # 'de': reverse(name, urlconf='server.manage.switch.urls.de', kwargs=kwargs),
        }

        if language:
            return urls[language.lower()]

        if current_language:
            return urls[self.request.session['translator_language'].lower()]

        return urls

    def Get_Post_Value(self, name):

        for key in self.request.POST.keys():

            # only other values
            if 'other_' in key:
                value = self.request.POST[key]

                # name:value
                if value.split(':')[0] == name:
                    return value.split(':')[1]

        # not found
        return ''

    def Validate_Period(self, session_name_date_from, session_name_date_to):

        date_from = self.request.session[session_name_date_from]
        date_to = self.request.session[session_name_date_to]

        # valid if string convert to date
        try: datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            self.request.session[session_name_date_from] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        # valid if string convert to date
        try: datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            self.request.session[session_name_date_to] = \
                datetime.today().strftime('%Y-%m-%d')

        # valid period
        if date_from > date_to:
            self.request.session[session_name_date_from] = \
                self.request.session[session_name_date_to]

    def Clear_Session(self, key_contain=''):

        keys = list(self.request.session.keys())
        for key in keys:
            if key_contain in key:
                del self.request.session[key]

    @staticmethod
    def Change_Model_Order(model, position, move=Direction.NONE):

        # get current object
        object_index = model.objects.get(position=position)

        # change with up element
        if move == Direction.UP:

            # swap - object up position 0
            object_up = model.objects.get(position=position-1)
            object_up_position = object_up.position + 1
            object_up.position = 0
            object_up.save()

            # save position
            object_up.position = object_up_position
            object_index.position -= 1

            object_index.save()
            object_up.save()

        # change with down element
        if move == Direction.DOWN:

            # swap - object down position 0
            object_down = model.objects.get(position=position+1)
            object_down_position = object_down.position - 1
            object_down.position = 0
            object_down.save()

            # save position
            object_down.position = object_down_position
            object_index.position += 1

            object_index.save()
            object_down.save()

    @staticmethod
    def Add_Model_Order(model, new_object, position, direction=Direction.NONE):
        greater_objects = None

        if direction == Direction.UP:

            # change greater elements positions
            greater_objects = model.objects.filter(position__gte=position)
            for greater_object in greater_objects:
                greater_object.position += 1

            # set position for new object
            new_object.position = position

        if direction == Direction.DOWN:

            # change greater elements positions
            greater_objects = model.objects.filter(position__gt=position)
            for greater_object in greater_objects:
                greater_object.position += 1

            # set position for new object
            new_object.position = position + 1

        for greater_object in greater_objects:
            greater_object.save()

    @staticmethod
    def To_URL(text):
        text = text.replace(' ', '_').lower()
        return Dynamic_Base.Convert_Polish_To_Ascii(text)

    @staticmethod
    def Generate_Passwrod(length):
        password = ''
        permitted_chars = string.ascii_letters + \
                          string.digits + \
                          string.punctuation

        for char_number in range(0, length):
            password += random.choice(permitted_chars)

        return password

    @staticmethod
    def Convert_Polish_To_Ascii(text):

        characters = {
            'ą': 'a', 'ć': 'c', 'ę': 'e',
            'ł': 'l', 'ń': 'n', 'ó': 'o',
            'ś': 's', 'ź': 'z', 'ż': 'z',

            'Ą': 'A', 'Ć': 'C', 'Ę': 'E',
            'Ł': 'L', 'Ń': 'N', 'Ó': 'O',
            'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z',
        }

        text_ascii = ''
        for char in text:
            if char in characters:
                char = characters[char]

            text_ascii += char

        return text_ascii

    @staticmethod
    def Encrypt(password):
        return make_password(password=password, salt='arbuz-team')

    @staticmethod
    def Get_Text_Cell(text, spaces=20, margin=0):
        spaces = ' ' * (spaces - len(text) - margin)
        margin = ' ' * margin
        return margin + text + spaces

    def Timer_Start(self):

        if DEBUG:
            self.start_time = time.time()

    def Display_Status(self, message=None):

        if DEBUG:

            if not DISPLAY_STATUS and not message:
                return

            status = '-' * 125 + '\n\n'
            status += self.Get_Text_Cell('Application: ')
            status += self.app_name

            if message: status += ' ({0}) \n\n'.format(message)
            else: status += '\n\n'

            duration = time.time() - self.start_time
            duration = str(int(duration * 1000))
            status += self.Get_Text_Cell('Duration: ', margin=2)
            status += duration + ' ms\n'

            status += self.Get_Text_Cell('URL: ', margin=2)
            status += self.Get_Path(current_language=True) + '\n'

            if self.request.POST:

                variables = []
                status += self.Get_Text_Cell('POST: ', margin=2)

                for key in self.request.POST:

                    variables.append(
                        self.Get_Text_Cell(key, 30) +
                        str(self.request.POST[key])
                    )

                separator = '\n' + self.Get_Text_Cell('')
                status += separator.join(variables) + '\n'

            keys = self.request.session.keys()
            if any(key.startswith(self.app_name) for key in keys):

                variables = []
                status += self.Get_Text_Cell('Session: ', margin=2)

                for key in keys:
                    if key.startswith(self.app_name):

                        variables.append(
                            self.Get_Text_Cell(key, 30) +
                            str(self.request.session[key])
                        )

                separator = '\n' + self.Get_Text_Cell('')
                status += separator.join(variables) + '\n'

            status += '\n' + '-' * 125 + '\n'
            print(status)

    def __init__(self, request):

        self.request = request
        self.start_time = 0
        self.content = {}

        last_dot = self.__module__.rfind('.')
        self.app_name = self.__module__[:last_dot]
