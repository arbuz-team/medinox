from server.manage.session.views import *
from server.service.payment.base import *
from server.page.dialog.views import *


class Endpoints(Base_Website):

    def Manage_Content_Ground(self):
        pass

    def Manage_Content_Dialog(self):

        if self.request.POST['dialog_type'] == 'alert':
            return Dialog_Alert(self.request, self.app_name).HTML

        if self.request.POST['dialog_type'] == 'confirm':
            return Dialog_Confirm(self.request, self.app_name).HTML

        if self.request.POST['dialog_type'] == 'prompt':
            return Dialog_Prompt(self.request, self.app_name).HTML

    def Manage_Content(self):

        if self.request.POST['__content__'] == 'ground':
            return self.Manage_Content_Ground()

        if self.request.POST['__content__'] == 'dialog':
            return self.Manage_Content_Dialog()

        self.content['error'] = 'no_event'
        return self.Render_HTML('arbuz/error.html')

    def Manage_Form(self):
        self.content['error'] = 'form'
        return self.Render_HTML('arbuz/error.html')

    def Manage_Exist(self):
        return JsonResponse({'__exist__': 'false'})

    def Manage_Get(self):
        return JsonResponse({'__get__': 'false'})

    def Manage_Little_Form(self):
        return JsonResponse({'__little__': 'false'})

    def Manage_Filter(self):
        return JsonResponse({'__filter__': 'false'})

    def Manage_Button(self):

        if self.request.POST['__button__'] == 'clear_session':
            if self.clear_session:

                self.Clear_Session(self.app_name)
                Check_Session(self.request)
                return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

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

    def __init__(self, request):
        Base_Website.__init__(self, request)
        self.clear_session = False
