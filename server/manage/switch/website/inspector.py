from server.manage.session.views import *
from server.service.payment.base import *
from server.page.dialog.views import *


class Inspector(Base_Website):

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
        Base_Website.__init__(self, request)

        self.ERROR_HTML = None
        self.authorization = False
        self.only_root = False
        self.payment_models_manager = None
