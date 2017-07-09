from django.contrib.gis.geoip import GeoIP
from django.shortcuts import redirect
from server.manage.switch.base import *
from server.service.translator.models import *


class Translator(Base):

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

    def Set_Subdomain_Language(self):

        url = self.request.get_host()
        subdomain = url.split('.')[0]

        if subdomain in ['pl', 'de', 'en']:
            self.request.session['translator_language'] = \
                subdomain.upper()

    def Set_Currency(self):

        geo = GeoIP()
        client_ip = self.request.META.get('REMOTE_ADDR', None)
        country = geo.country_code(client_ip)

        if country == 'PL':
            self.request.session['translator_currency'] = 'PLN'

        if country == 'DE':
            self.request.session['translator_currency'] = 'EUR'

        if country == 'GB': # united kingdom
            self.request.session['translator_currency'] = 'GBP'

    def Get_Language_Redirect(self):

        url = self.request.get_host()
        subdomain = url.split('.')[0]

        if subdomain not in ['pl', 'de', 'en']:
            client_ip = self.request.META.get('REMOTE_ADDR', None)

            geo = GeoIP()
            country = geo.country_code(client_ip)
            path_manager = Path_Manager(self)

            if country == 'PL':
                return redirect(path_manager.Get_Urls(language='PL'))

            if country == 'DE':
                return redirect(path_manager.Get_Urls(language='DE'))

        return None


def Text(_object, pk, language=None):

    if not language:
        language = _object.request.session['translator_language']

    return Translator.Translate(language, pk)