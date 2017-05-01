from django.shortcuts import render
from django.core.urlresolvers import reverse, resolve
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from arbuz.settings import *
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from datetime import date
import base64, imghdr, os, string, random, time


class Dynamic_Base:

    def Render_HTML(self, file_name, form_name = ''):

        # example: EN/user/sign_in.html
        template = self.request.session['translator_language'] \
                   + '/' + file_name

        self.content['form_name'] = form_name
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
                  reverse(name, urlconf='arbuz.urls.en', kwargs=kwargs),

            'pl': secure + 'pl.' + domain +
                 reverse(name, urlconf='arbuz.urls.pl', kwargs=kwargs),

            # 'de': secure + 'de.' + domain +
            #      reverse(name, urlconf='arbuz.urls.de', kwargs=kwargs),
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
            'en': reverse(name, urlconf='arbuz.urls.en', kwargs=kwargs),
            'pl': reverse(name, urlconf='arbuz.urls.pl', kwargs=kwargs),
            # 'de': reverse(name, urlconf='arbuz.urls.de', kwargs=kwargs),
        }

        if language:
            return urls[language.lower()]

        if current_language:
            return urls[self.request.session['translator_language'].lower()]

        return urls

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
    def Generate_Image_Details(image_format):

        name = '{0}.{1}'.format(random.randrange(1000, 9999), image_format)
        path_root = '{0}/{1}'.format(MEDIA_ROOT, name)
        path_url = '{0}{1}'.format(MEDIA_URL, name)

        return {'name': name, 'path_root': path_root, 'path_url': path_url}

    @staticmethod
    def Check_If_Image(path):

        if imghdr.what(path) in ['jpeg', 'png']:
            return True

        return False

    @staticmethod
    def Save_Image_From_Base64(image):

        base64_image = image.split(',', 1)[1]
        base64_data = image.split(';', 1)[0]
        base64_format = base64_data.split('/')[1]

        image_details = Dynamic_Base.\
            Generate_Image_Details(base64_format)

        # file with the name exists
        if os.path.exists(image_details['path_root']):
            Dynamic_Base.Save_Image_From_Base64(image)

        with open(image_details['path_root'], "wb") as file:
            file.write(base64.b64decode(base64_image))

        # if file is not image
        if not Dynamic_Base.Check_If_Image(image_details['path_root']):
            os.remove(image_details['path_root'])
            image_details['path_url'] = ''

        return image_details['path_url']

    @staticmethod
    def Save_Image_From_URL(url):

        binary_file = BytesIO(urlopen(url).read())
        image = Image.open(binary_file)

        image_details = Dynamic_Base.\
            Generate_Image_Details(image.format.lower())

        # file with the name exists
        if os.path.exists(image_details['path_root']):
            Dynamic_Base.Save_Image_From_URL(image)

        image.save(image_details['path_root'])

        # if file is not image
        if not Dynamic_Base.Check_If_Image(image_details['path_root']):
            os.remove(image_details['path_root'])
            image_details['path_url'] = ''

        return image_details['path_url']

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
