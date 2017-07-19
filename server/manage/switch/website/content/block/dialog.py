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