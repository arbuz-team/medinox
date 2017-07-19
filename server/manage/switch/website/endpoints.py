from server.manage.session.views import *
from server.service.payment.base import *
from server.dialog.views import *


class Endpoints(Base_Website):

    def Manage_Content(self):
        self.content['error'] = 'no_exist'
        return self.Render_HTML('arbuz/error.html')

    def Manage_Form(self):
        self.content['error'] = 'form'
        return self.Render_HTML('arbuz/error.html')

    def Manage_Exist(self):
        return HttpResponse('')

    def Manage_Get(self):
        return HttpResponse('')

    def Manage_Little_Form(self):
        return HttpResponse('')

    def Manage_Filter(self):
        return HttpResponse('')

    def Manage_Button(self):
        return HttpResponse('')

    def Clear_Session(self, key_contain=''):
        Base_Website.Clear_Session(self, key_contain)
        Check_Session(self.request)

    def Index_Clear_Session(self):
        Base_Website.Clear_Session(self, 'searcher')
        Base_Website.Clear_Session(self, 'root_social_media')
        Base_Website.Clear_Session(self, 'root_address')
        Check_Session(self.request)

    def Manage_Index(self):

        self.Index_Clear_Session()

        # change website to other language
        translator = Translator(self)
        lang_redirect = translator.Get_Language_Redirect()
        if lang_redirect:
            return lang_redirect

        return render(self.request, 'index.html', {})

    def __init__(self, _object):
        Base_Website.__init__(self, _object)
        self.clear_session = False
