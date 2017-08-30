from django.contrib.gis.geoip import GeoIP
from django.shortcuts import redirect
from server.service.sql.views import *
from server.service.translator.models import *
from server.manage.switch.paths import *


class Translator(Base):

    @staticmethod
    def Translate_EN(pk):
        return SQL.Get(Language_EN, id=pk).value

    @staticmethod
    def Translate_PL(pk):
        return SQL.Get(Language_PL, id=pk).value

    @staticmethod
    def Translate_DE(pk):
        return SQL.Get(Language_DE, id=pk).value

    @staticmethod
    def Translate(language, pk):

        if not SQL.Filter(Language_EN, id=pk):
            raise Exception('This value does not exist. '
                            '<translator.Translator.Translate>')

        method = 'Translate_' + language
        return getattr(Translator, method)(pk)

    def Set_Subdomain_Language(self):

        url = self.request.get_host()
        subdomain = url.split('.', 1)[0]

        if subdomain in ['pl', 'de', 'en']:
            self.request.session['translator_language'] = \
                subdomain.upper()

    def Get_Language_Redirect(self):

        url = self.request.get_host()
        subdomain = url.split('.', 1)[0]

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


def Text(_object=None, pk=0, language=None, request=None):

    if not _object:
        language = request.session['translator_language']

    if not language:
        language = _object.request.session['translator_language']

    return Translator.Translate(language, pk)