from server.service.translator.views import *
from server.manage.switch.website.base import *
import importlib


class Dialog(Base_Website):

    def Get_Dialog_Post_Variable(self, name):

        if name in self.request.POST:
            return self.request.POST[name]

        else: return ''

    def Get_Dialog_Type(self):

        # client send type
        if '_type_' in self.request.POST:
            return self.request.POST['_type_']

        # when not valid or next option
        class_name = self.__class__.__name__
        return class_name.split('_', 1)[1].lower()

    def Get_Dialog_Name(self):
        return self.request.POST['_name_']

    def Generate_Content(self):

        self.context['accept'] = {
            'name':     self.Get_Dialog_Post_Variable('accept_name'),
            'action':   self.Get_Dialog_Post_Variable('accept_action'),
            'value':    self.Get_Dialog_Post_Variable('accept_value'),
            'reload':   self.Get_Dialog_Post_Variable('accept_reload'),
            'redirect': self.Get_Dialog_Post_Variable('accept_redirect'),
            'url':      self.Get_Dialog_Post_Variable('accept_url'),
            'event':    self.Get_Dialog_Post_Variable('accept_event'),
            'other_1':  self.Get_Dialog_Post_Variable('accept_other_1'),
            'other_2':  self.Get_Dialog_Post_Variable('accept_other_2'),
            'other_3':  self.Get_Dialog_Post_Variable('accept_other_3'),
        }

    @staticmethod
    def Apply_Message():
        return HttpResponse()

    def Manage(self):

        if self.apply:
            return self.Apply_Message()

        # content for buttons in dialogs
        self.Generate_Content()

        # get POST data
        _type_ = self.Get_Dialog_Type()
        dialog_name = self.Get_Dialog_Name()

        # get class details
        class_module = '{0}.{1}'.format(_type_, dialog_name)
        class_name = 'Service_' + dialog_name.title()
        class_path = 'server.dialog.service.' + class_module

        # get module and class
        module = importlib.import_module(class_path)
        return getattr(module, class_name)(self).HTML

    def __init__(self, _object, apply=False, not_valid=False):
        Base_Website.__init__(self, _object)
        self.parent_app_name= _object.app_name
        self.not_valid = not_valid
        self.apply = apply

