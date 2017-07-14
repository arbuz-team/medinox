from server.service.translator.views import *
from base64 import b64encode
from server.manage.switch.templatetags.base import *
from server.service.translator.models import *


class Other_Manager(Base_Tag_Manager):

    def Get_Path_Or_Url(self):

        name = self.values['name']
        full = self.values['full']
        kwargs = self.values['kwargs']
        path_manager = Path_Manager(self)

        if full:
            return path_manager.Get_Urls(
                name, kwargs, current_language=True)

        if not full:
            return path_manager.Get_Path(
                name, kwargs, current_language=True)

    def Create_Redirect_URL(self):

        kwargs = self.values['kwargs']
        url_name = self.values['url_name']
        path_manager = Path_Manager(self)

        url_name = path_manager.Get_Path(
            url_name, kwargs, current_language=True)

        redirect_url = self.values['redirect_url']
        redirect_url = path_manager.Get_Path(
            redirect_url, kwargs, current_language=True)

        redirect_url = b64encode(bytes(redirect_url, 'utf-8'))
        redirect_url = redirect_url.decode('utf-8')
        return '{0}redirect/{1}/'.format(url_name, redirect_url)

    def Get_Text_In_Current_Language(self):
        pk = self.values['pk']
        language = self.values['language']
        return Text(self, pk, language)

    def Get_App_Name(self):
        app_name = self.request.session['arbuz_app'].split('.')[-2]
        print(app_name)
        pk = SQL.Get(Language_EN, value=app_name).pk
        return Text(self, pk).replace('.', ' ').title()



@register.simple_tag(takes_context=True)
def url(context, name=None, full=False, *args, **kwargs):

    task = 'Get_Path_Or_Url'
    request = context['request']
    values = {
        'name': name,
        'full': full,
        'kwargs': kwargs,
    }

    return Other_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def redirect(context, url_name, redirect_url=None, *args, **kwargs):

    task = 'Create_Redirect_URL'
    request = context['request']
    values = {
        'url_name': url_name,
        'redirect_url': redirect_url,
        'kwargs': kwargs,
    }

    return Other_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def text(context, pk, language=None):

    task = 'Get_Text_In_Current_Language'
    request = context['request']
    values = {
        'pk': pk,
        'language': language
    }

    return Other_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def get_app_name(context):

    task = 'Get_App_Name'
    request = context['request']

    return Other_Manager(task, {}, request).OUT

@register.filter
def length(tab):
    return len(tab)

@register.simple_tag(takes_context=True)
def var(context, name, value):
    context[name] = value
    return ''

@register.simple_tag
def random(_len):
    return Base_Website.Generate_Random_Chars(
        _len, punctuation=False)
