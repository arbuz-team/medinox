from server.manage.switch.base import *
from server.content.product.forms import *
from server.content.catalog.forms import *
from server.manage.user.account.forms import *
from server.content.main.forms import *
from server.service.payment.forms import *
from server.content.main.models import *


class Base_Service(metaclass=ABCMeta):

    @abstractmethod
    def Manage(self):
        pass

    def Prepare_Form(self, _class, initial=None, instance=None):

        # form class is only form, not form model
        if 'Model' not in _class.__bases__[0].__name__:

            if self.dialog.not_valid:
                return _class(self.request,
                      initial=self.request.POST)

            return _class(self.request, initial=initial)

        else: # form model

            if self.dialog.not_valid:
                return _class(self.request,
                      initial=self.request.POST,
                      instance=instance)

            return _class(self.request,
                      initial=initial,
                      instance=instance)

    def __init__(self, dialog):

        self.dialog = dialog
        self.request = dialog.request
        self.content = dialog.content
        self.instance = None

        self.HTML = self.Manage()
