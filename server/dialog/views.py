from server.dialog.base import *


class Dialog_Alert(Dialog):

    def __init__(self, _object):
        Dialog.__init__(self, _object)
        self.HTML = self.Manage()



class Dialog_Confirm(Dialog):

    def __init__(self, _object):
        Dialog.__init__(self, _object)
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

    def Get_Dialog_Name(self):

        # when not valid or get dialog after send form
        if '_name_' in self.request.POST:
            dialog_name = self.request.POST['_name_']

            if self.Get_Alias(dialog_name):
                return self.Get_Alias(dialog_name)

            return dialog_name

        # when standard ask about dialog
        dialog_name = self.request.POST['_name_']
        if self.Get_Alias(dialog_name):
            return self.Get_Alias(dialog_name)

        return dialog_name

    def __init__(self, _object, apply=False,
                 not_valid=False, other_value=None):

        Dialog.__init__(self, _object, apply, not_valid)
        self.other_value = other_value

        self.HTML = self.Manage()
