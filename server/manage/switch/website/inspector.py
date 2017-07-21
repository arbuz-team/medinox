from server.manage.switch.website.base import *
from server.service.payment.base import *


class Inspector(Base_Website):

    def Error_No_Event(self):
        self.context['error'] = 'no_event'
        return self.Render_HTML('arbuz/error.html')

    def Error_Authorization(self):
        path_manager = Path_Manager(self)
        redirect = None

        if self.only_root:
            redirect = path_manager.Create_Redirect_URL(
                'root.sign_in', None)

        if self.authorization:
            redirect = path_manager.Create_Redirect_URL(
                'user.sign_in', None)

        return HttpResponseRedirect(redirect)

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

    def Check_Payment(self): # Backend: WTF!!
        self.payment_models_manager = \
            Payment_Models_Manager(self)

        return True

    def __init__(self, _object):
        Base_Website.__init__(self, _object)

        self.ERROR_HTML = None
        self.authorization = False
        self.only_root = False
        self.payment_models_manager = None
