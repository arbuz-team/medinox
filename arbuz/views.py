from session.views import *
from payment.base import *
from dialog.views import *

from abc import ABCMeta, abstractmethod


class Manager(Dynamic_Base):

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
        Dynamic_Base.Clear_Session(self, key_contain)
        Check_Session(self.request)

    def Index_Clear_Session(self):
        Dynamic_Base.Clear_Session(self, 'searcher')
        Dynamic_Base.Clear_Session(self, 'root_social_media')
        Dynamic_Base.Clear_Session(self, 'root_address')
        Check_Session(self.request)

    def Manage_Index(self):

        self.Index_Clear_Session()

        # change website to other language
        lang_redirect = Translator.Get_Language_Redirect(self.request)
        if lang_redirect:
            return lang_redirect

        return render(self.request, 'index.html', {})

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
        self.clear_session = False



class Checker(Dynamic_Base):

    def Error_No_Event(self):
        self.content['error'] = 'no_event'
        return self.Render_HTML('arbuz/error.html')

    def Error_Authorization(self):
        self.content['error'] = 'unauthorized'
        return self.Render_HTML('arbuz/error.html')

    def Check_Authorization(self):

        # dialog is checked in dialog abstract class
        if '__content__' in self.request.POST:
            if self.request.POST['__content__'] == 'dialog':
                return True

        if self.authorization:
            if self.request.session['user_login']:
                return True
            return False

        if self.only_root:
            if self.request.session['root_login']:
                return True
            return False

        return True

    def Check_Payment(self):
        self.payment_models_manager = \
            Payment_Models_Manager(self.request)

        return True

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)

        self.ERROR_HTML = None
        self.authorization = False
        self.only_root = False
        self.payment_models_manager = None



class Updater(Dynamic_Base):

    def Update_Navigation(self):

        navigation = []
        url = self.request.get_full_path()
        parts_of_url = url.split('/')[1:-1]
        page = '/'

        for part in parts_of_url:
            page += part + '/'
            navigation.append((part, page))

        if self.length_navigation:
            navigation = navigation[0:self.length_navigation]

        self.request.session['arbuz_navigation'] = navigation

    def Update_Current_Url(self):
        self.request.session['arbuz_url'] = self.Get_Urls()

    def Update_Website_Permissions(self):

        self.request.session['arbuz_permissions'] = ''
        if '__content__' not in self.request.POST:
            return

        if self.request.POST['__content__'] == 'ground':

            if self.only_root:
                self.request.session['arbuz_permissions'] = 'only_root'

            if self.authorization:
                self.request.session['arbuz_permissions'] = 'authorization'

    def Update_Redirect_URL(self):
        self.content['go_back'] = '/'

        if 'redirect' in self.other_value:
            self.content['go_back'] = base64.b64decode(
                bytes(self.other_value['redirect'], 'utf-8'))

    def Update_App_Name(self):
        self.request.session['arbuz_app'] = self.app_name

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
        self.length_navigation = None
        self.only_root = False
        self.authorization = False
        self.other_value = None



class Dynamic_Event_Manager(Manager, Checker, Updater, metaclass=ABCMeta):

    def Check(self):

        if self.error_method:
            self.ERROR_HTML = self.Error()
            return False

        methods = getmembers(Checker(self.request), predicate=ismethod)
        methods = [method[0] for method in methods]

        # call all of methods Check_*
        for method in methods:
            if 'Check_' in method:

                # Check_* returned False
                if not getattr(Dynamic_Event_Manager, method)(self):

                    # render error HTML
                    method = method.replace('Check', 'Error')
                    self.ERROR_HTML = getattr(Dynamic_Event_Manager, method)(self)

                    return False

        return True

    def Update(self):

        methods = getmembers(Updater(self.request), predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if 'Update_' in method:
                getattr(Dynamic_Event_Manager, method)(self)

    def Error(self):
        return getattr(Dynamic_Event_Manager, self.error_method)(self)

    def Manage(self):

        # parts of pages
        if '__content__' in self.request.POST:
            return self.Manage_Content()

        # manage forms
        if '__form__' in self.request.POST:
            return self.Manage_Form()

        # checkers
        if '__exist__' in self.request.POST:
            return self.Manage_Exist()

        # getters
        if '__get__' in self.request.POST:
            return self.Manage_Get()

        # auto/mini form
        if '__little__' in self.request.POST:
            return self.Manage_Little_Form()

        # filters
        if '__filter__' in self.request.POST:
            return self.Manage_Filter()

        # options
        if '__button__' in self.request.POST:
            return self.Manage_Button()

        return self.Error_No_Event()

    def Initialize(self):

        self.Update()

        if self.request.method == 'POST':
            if self.Check():
                return self.Manage()

            return self.ERROR_HTML

        if self.request.method == 'GET':
            return self.Manage_Index()

    def __init__(self, request,
                 autostart=True,
                 authorization=False,
                 error_method=None,
                 other_value={},
                 only_root=False,
                 clear_session=False,
                 length_navigation=None):

        Manager.__init__(self, request)
        Checker.__init__(self, request)
        Updater.__init__(self, request)

        self.authorization = authorization
        self.error_method = error_method
        self.other_value = other_value
        self.only_root = only_root
        self.clear_session = clear_session
        self.length_navigation = length_navigation

        if autostart:

            try:

                self.Timer_Start()
                self.HTML = self.Initialize()
                self.Display_Status()

                if not self.HTML:
                    self.Display_Status(message='NOT HTML')

            except Exception as exception:

                self.Display_Status(message='INTERNAL')
                raise exception

    @staticmethod
    @abstractmethod
    def Launch(request):
        return Dynamic_Event_Manager(request)