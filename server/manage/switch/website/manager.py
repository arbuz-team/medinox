from server.manage.switch.website.endpoints import *
from server.manage.switch.website.inspector import *
from server.manage.switch.website.refresh import *


class Website_Manager(Endpoints, Inspector, Refresh, metaclass=ABCMeta):

    def Check(self):

        if self.error_method:
            self.ERROR_HTML = self.Error()
            return False

        methods = getmembers(Inspector(self.request), predicate=ismethod)
        methods = [method[0] for method in methods]

        # call all of methods Check_*
        for method in methods:
            if 'Check_' in method:

                # Check_* returned False
                if not getattr(Website_Manager, method)(self):

                    # render error HTML
                    method = method.replace('Check', 'Error')
                    self.ERROR_HTML = getattr(Website_Manager, method)(self)

                    return False

        return True

    def Update(self):

        methods = getmembers(Refresh(self.request), predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if 'Update_' in method:
                getattr(Website_Manager, method)(self)

    def Error(self):
        return getattr(Website_Manager, self.error_method)(self)

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

        Endpoints.__init__(self, request)
        Inspector.__init__(self, request)
        Refresh.__init__(self, request)

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
    def Launch(request, *args, **kwargs):
        return Website_Manager(request)