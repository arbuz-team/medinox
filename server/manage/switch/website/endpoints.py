from server.manage.session.views import *
from server.dialog.views import *


class Endpoints(Base_Website):

    def Manage_Content(self):
        pass

    def Manage_Form(self):
        pass

    def Manage_Valid(self):
        pass

    def Manage_Get(self):
        pass

    def Manage_Little_Form(self):
        pass

    def Manage_Filter(self):
        pass

    def Manage_Button(self):
        pass

    def Error(self, *args, **kwargs):
        pass

    def Index(self):

        self.Index_Clear_Session()

        # change website to other language
        translator = Translator(self)
        lang_redirect = translator.Get_Language_Redirect()
        if lang_redirect:
            return lang_redirect

        return render(self.request, 'index.html', {})

    def Clear_Session(self, key_contain=''):
        Base_Website.Clear_Session(self, key_contain)
        Check_Session(self.request)

    def Index_Clear_Session(self):
        Base_Website.Clear_Session(self, 'searcher')
        Base_Website.Clear_Session(self, 'root_social_media')
        Base_Website.Clear_Session(self, 'root_address')
        Check_Session(self.request)

    def __init__(self, _object):
        Base_Website.__init__(self, _object)
        self.clear_session = False
