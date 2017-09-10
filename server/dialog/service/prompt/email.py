from server.dialog.service.base import *
from server.manage.user.account.forms import *


class Service_Email(Base_Service):

    def Not_Valid(self):
        pass

    def Manage(self):

        self.context['title'] = Text(self, 86)
        self.context['form'] = self.Prepare_Form(Form_User_Details)

        self.context['form'].Set_Hidden('username')
        self.context['form'].Set_Hidden('password')

        return self.Render_Dialog(
            'prompt.html', 'email', authorization=True)

