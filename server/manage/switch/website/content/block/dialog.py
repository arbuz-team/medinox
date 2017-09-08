from server.manage.switch.website.endpoints import *


class Dialog_Block(Endpoints):

    def Manage_Content(self):

        if self.request.POST['_type_'] == 'alert':
            return Dialog_Alert(self).HTML

        if self.request.POST['_type_'] == 'confirm':
            return Dialog_Confirm(self).HTML

        if self.request.POST['_type_'] == 'prompt':
            return Dialog_Prompt(self).HTML

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/dialog.html', context=context))

    # methods direct to ground `website`

    def Manage_Form(self):
        return self.website.Manage_Form()

    def Manage_Exist(self):
        return self.website.Manage_Exist()

    def Manage_Get(self):
        return self.website.Manage_Get()

    def Manage_Little_Form(self):
        return self.website.Manage_Little_Form()

    def Manage_Filter(self):
        return self.website.Manage_Filter()

    def Manage_Button(self):
        return self.website.Manage_Button()

    def __init__(self, _object):
        Endpoints.__init__(self, _object)

        try: self.website = _object.website
        except: pass
