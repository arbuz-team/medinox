from server.service.translator.views import *
from server.manage.switch.website.base import *
import importlib


class Dialog(Base_Website):

    def Get_POST_Variable(self, name):

        if name in self.request.POST:
            return self.request.POST[name]

        else: return ''

    def Get_Dialog_Type(self):

        # client send type
        if 'dialog_type' in self.request.POST:
            return self.request.POST['dialog_type']

        # when not valid or next option
        class_name = self.__class__.__name__
        return class_name.split('_', 1)[1].lower()

    def Get_Dialog_Name(self):
        return self.request.POST['dialog_name']

    def Generate_Content(self):

        self.content['additional'] = {
            'name':     self.Get_POST_Variable('additional_name'),
            'action':   self.Get_POST_Variable('additional_action'),
            'value':    self.Get_POST_Variable('additional_value'),
            'reload':   self.Get_POST_Variable('additional_reload'),
            'redirect': self.Get_POST_Variable('additional_redirect'),
            'url':      self.Get_POST_Variable('additional_url'),
            'event':    self.Get_POST_Variable('additional_event'),
        }

    @staticmethod
    def Apply_Message():
        return JsonResponse({'__form__': 'true'})

    def Manage(self):

        if self.apply:
            return self.Apply_Message()

        # content for buttons in dialogs
        self.Generate_Content()

        # get POST data
        dialog_type = self.Get_Dialog_Type()
        dialog_name = self.Get_Dialog_Name()

        # get class details
        class_module = '{0}.{1}'.format(dialog_type, dialog_name)
        class_name = 'Service_' + dialog_name.title()
        class_path = 'server.dialog.service.' + class_module

        # get module and class
        module = importlib.import_module(class_path)
        return getattr(module, class_name)(self).HTML

    def __init__(self, _object, apply=False):
        Base_Website.__init__(self, _object)
        self.parent_app_name= _object.app_name
        self.apply = apply

