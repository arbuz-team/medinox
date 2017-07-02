from server.page.dialog.base import *


class Dialog_Alert(Dialog):

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Confirm(Dialog):

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Prompt(Dialog):

    @staticmethod
    def Get_Alias(dialog_name):

        # if dialog name have alias
        # when get the same dialog

        aliases = {
            'values':   'widget',
        }

        if dialog_name in aliases.keys():
            return aliases[dialog_name]

        return None

    def Generate_Content(self):

        self.content['additional'] = {
            'reload': self.request.POST['additional_reload'],
            'redirect': self.request.POST['additional_redirect'],
            'event': self.request.POST['additional_event'],
        }

    def Get_Dialog_Name(self):

        if '__form__' in self.request.POST:
            dialog_name = self.request.POST['__form__']

            if self.Get_Alias(dialog_name):
                return self.Get_Alias(dialog_name)

            return dialog_name

        return self.request.POST['dialog_name']

    def __init__(self, request, app_name, apply=False,
                 not_valid=False, other_value=None):

        Dialog.__init__(self, request, app_name, apply)
        self.not_valid = not_valid
        self.other_value = other_value

        self.HTML = self.Manage()
