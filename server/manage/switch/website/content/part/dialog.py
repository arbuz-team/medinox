from server.manage.switch.website.endpoints import *


class Dialog_Part(Endpoints):

    def Manage_Content(self):

        if self.request.POST['dialog_type'] == 'alert':
            return Dialog_Alert(self).HTML

        if self.request.POST['dialog_type'] == 'confirm':
            return Dialog_Confirm(self).HTML

        if self.request.POST['dialog_type'] == 'prompt':
            return Dialog_Prompt(self).HTML
