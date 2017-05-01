from django.contrib.gis.geoip import GeoIP
from django.shortcuts import redirect
from arbuz.base import *
from translator.models import *


class Translator:

    @staticmethod
    def Translate_EN(pk):
        return Language_EN.objects.get(id=pk).value

    @staticmethod
    def Translate_PL(pk):
        return Language_PL.objects.get(id=pk).value

    @staticmethod
    def Translate_DE(pk):
        return Language_DE.objects.get(id=pk).value

    @staticmethod
    def Translate(language, pk):

        if not Language_EN.objects.filter(id=pk):
            raise Exception('This value does not exist. '
                            '<translator.Translator.Translate>')

        method = 'Translate_' + language
        return getattr(Translator, method)(pk)

    @staticmethod
    def Set_Subdomain_Language(request):

        url = request.get_host()
        subdomain = url.split('.')[0]

        if subdomain in ['pl', 'de', 'en']:
            request.session['translator_language'] = subdomain.upper()

    @staticmethod
    def Set_Currency(request):

        geo = GeoIP()
        client_ip = request.META.get('REMOTE_ADDR', None)
        country = geo.country_code(client_ip)

        if country == 'PL':
            request.session['translator_currency'] = 'PLN'

        if country == 'DE':
            request.session['translator_currency'] = 'EUR'

        if country == 'GB': # united kingdom
            request.session['translator_currency'] = 'GBP'

    @staticmethod
    def Get_Language_Redirect(request):

        url = request.get_host()
        subdomain = url.split('.')[0]

        if subdomain not in ['pl', 'de', 'en']:
            client_ip = request.META.get('REMOTE_ADDR', None)

            geo = GeoIP()
            country = geo.country_code(client_ip)
            dynamic_base = Dynamic_Base(request)

            if country == 'PL':
                return redirect(dynamic_base.Get_Urls(language='PL'))

            if country == 'DE':
                return redirect(dynamic_base.Get_Urls(language='DE'))

        return None


def Text(request, pk, language=None):

    if not language:
        language = request.session['translator_language']

    return Translator.Translate(language, pk)