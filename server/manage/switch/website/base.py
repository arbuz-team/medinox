from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from server.service.file.views import *
from server.manage.switch.paths import *
from server.manage.switch.settings import *
from server.service.sql.views import *

from abc import ABCMeta, abstractmethod
import string, time


class Base_Website(metaclass=ABCMeta):

    def Render_HTML(self, file_name, form_name = '', additional_form_name=''):

        # example: EN/user/sign_in.html
        template = self.request.session['translator_language'] \
                   + '/' + file_name

        self.content['form_name'] = form_name
        self.content['additional_form_name'] = additional_form_name
        return render(self.request, template, self.content)

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
    def To_URL(text):
        text = text.replace(' ', '_').lower()
        return Base_Website.Convert_Polish_To_Ascii(text)

    @staticmethod
    def Generate_Random_Chars(length, letters=True,
                              digits=True, punctuation=True):

        permitted_chars = ''
        result = ''

        permitted_chars += string.ascii_letters if letters else ''
        permitted_chars += string.digits if digits else ''
        permitted_chars += string.punctuation if punctuation else ''

        for char_number in range(0, length):
            result += random.choice(permitted_chars)

        return result

    @staticmethod
    def Generate_Passwrod(length):
        return Base_Website.Generate_Random_Chars(length)

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

            path_manager = Path_Manager(self)
            status += self.Get_Text_Cell('URL: ', margin=2)
            status += path_manager.Get_Path(current_language=True) + '\n'

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
            if any(key.startswith(self.short_app_name) for key in keys):

                variables = []
                status += self.Get_Text_Cell('Session: ', margin=2)

                for key in keys:
                    if key.startswith(self.short_app_name):

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

        self.app_name = self.__module__.rsplit('.', 1)[0]
        self.short_app_name = self.app_name.rsplit('.', 1)[1]

