from server.manage.switch.settings import *

from django.utils.timezone import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from abc import ABCMeta, abstractmethod
import string, random, time

class Base:

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

