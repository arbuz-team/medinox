from django.core.urlresolvers import reverse, resolve
from server.manage.switch.base import *


class Path_Manager(Base):

    @staticmethod
    def Media_Root(file=''):
        return os.path.join(MEDIA_ROOT, file)

    @staticmethod
    def Static_Root(file=''):
        return os.path.join(STATICFILES_DIRS[0], file)

    @staticmethod
    def Static_URL(file=''):
        return os.path.join(STATIC_URL, file)

    @staticmethod
    def To_URL(text):
        text = text.replace(' ', '_').lower()
        text = text.replace('-', '')
        return Base.Convert_Polish_To_Ascii(text)

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

            'local_en': secure + domain +
                  reverse(name, urlconf='server.manage.switch.urls.en', kwargs=kwargs),

            # 'local_pl': secure + domain +
            #       reverse(name, urlconf='server.manage.switch.urls.pl', kwargs=kwargs),

            # 'local_de': secure + domain +
            #       reverse(name, urlconf='server.manage.switch.urls.de', kwargs=kwargs),
        }

        if current_language:
            language = self.request.session['translator_language']

        if language:

            if '127.0.0.1' in domain:
                return urls['local_' + language.lower()]

            return urls[language.lower()]

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
