from server.manage.switch.website.base import *
from server.ground.product.forms import *
from server.ground.catalog.forms import *
from server.manage.user.account.forms import *
from server.ground.main.forms import *
from server.service.payment.forms import *
from server.ground.main.models import *


class Base_Service(metaclass=ABCMeta):

    @abstractmethod
    def Manage(self):
        pass

    def Unauthorized_Access(self):
        self.content['title'] = Text(self, 69)
        self.content['text'] = Text(self, 70)
        return self.dialog.Render_HTML('dialog/alert/alert.html')

    def Render_Dialog(self, file_name, form_name='', additional_form_name='',
                      authorization=False, only_root=False):

        # example: dialog/prompt/catalog.html
        file_name = 'dialog/{0}/{1}'.format(
            self.dialog.Get_Dialog_Type(), file_name)

        if not authorization and not only_root:
            return self.dialog.Render_HTML(
                file_name, form_name, additional_form_name)

        if authorization:
            if self.request.session['user_login']:
                return self.dialog.Render_HTML(
                    file_name, form_name, additional_form_name)

        if only_root:
            if self.request.session['root_login']:
                return self.dialog.Render_HTML(
                    file_name, form_name, additional_form_name)

        return self.Unauthorized_Access()

    def Prepare_Form(self, _class, initial=None, instance=None):

        # form class is only form, not form model
        if 'Model' not in _class.__bases__[0].__name__:

            if self.dialog.not_valid:
                return _class(self, post=True)

            return _class(self, initial=initial)

        else: # form model

            if self.dialog.not_valid:
                return _class(self, post=True,
                              instance=instance)

            return _class(self, initial=initial,
                          instance=instance)

    def __init__(self, dialog):

        self.dialog = dialog
        self.request = dialog.request
        self.content = dialog.content
        self.instance = None
        self.initial = None

        self.HTML = self.Manage()