from server.manage.switch.settings import *

from django.contrib.auth.hashers import make_password
from django.utils.timezone import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.shortcuts import render

from django.http.response import HttpResponse, JsonResponse, \
    HttpResponseRedirect, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseServerError

from abc import ABCMeta, abstractmethod
import string, random, time


class Base:

    def Render_To_String(self, file_name, form_name = '',
                         additional_form_name='', context=None):

        if context:
            self.context.update(context)

        # example: EN/user/sign_in.html
        template = self.request.session['translator_language'] \
                   + '/' + file_name

        self.context['form_name'] = form_name
        self.context['additional_form_name'] = additional_form_name
        return render_to_string(template, self.context, self.request)

    def Render_HTML(self, file_name, form_name = '', additional_form_name=''):

        # example: EN/user/sign_in.html
        template = self.request.session['translator_language'] \
                   + '/' + file_name

        self.context['form_name'] = form_name
        self.context['additional_form_name'] = additional_form_name
        return render(self.request, template, self.context)

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

    def __init__(self, _object):
        self.request = _object.request
        self.context = {}

