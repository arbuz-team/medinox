from server.service.translator.views import *
import importlib


class Dialog(Dynamic_Base):

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

    def Render_Dialog(self, file_name, form_name='', additional_form_name='',
                      authorization=False, only_root=False):

        if not authorization and not only_root:
            return self.Render_HTML(file_name, form_name,
                                    additional_form_name)

        if authorization:
            if self.request.session['user_login']:
                return self.Render_HTML(file_name, form_name,
                                        additional_form_name)

        if only_root:
            if self.request.session['root_login']:
                return self.Render_HTML(file_name, form_name,
                                        additional_form_name)

        return self.Unauthorized_Access()

    @staticmethod
    def Apply_Message():
        return JsonResponse({'__form__': 'true'})

    def Unauthorized_Access(self):
        self.content['title'] = Text(self.request, 69)
        self.content['text'] = Text(self.request, 70)
        return self.Render_HTML('dialog/alert.html')

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
        class_path = 'server.page.dialog.service.' + class_module

        # get module and class
        module = importlib.import_module(class_path)
        return getattr(module, class_name)(self).HTML

    def __init__(self, request, app_name, apply=False):
        Dynamic_Base.__init__(self, request)
        self.parent_app_name= app_name
        self.apply = apply

