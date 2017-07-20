from server.manage.switch.website.endpoints import *


class Dialog_Block(Endpoints):

    def Manage_Content(self):

        if self.request.POST['dialog_type'] == 'alert':
            return Dialog_Alert(self).HTML

        if self.request.POST['dialog_type'] == 'confirm':
            return Dialog_Confirm(self).HTML

        if self.request.POST['dialog_type'] == 'prompt':
            return Dialog_Prompt(self).HTML

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/dialog.html', context=context))

    # methods direct to ground `website`

    def Manage_Form(self):
        self.website.Manage_Form()

    def Manage_Exist(self):
        self.website.Manage_Exist()

    def Manage_Get(self):
        self.website.Manage_Get()

    def Manage_Little_Form(self):
        self.website.Manage_Little_Form()

    def Manage_Filter(self):
        self.website.Manage_Filter()

    def Manage_Button(self):
        self.website.Manage_Button()

    def __init__(self, _object):
        Endpoints.__init__(self, _object)
        self.website = _object.website
