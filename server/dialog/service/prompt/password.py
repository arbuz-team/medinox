from server.dialog.service.base import *
from server.manage.user.account.forms import *


class Service_Password(Base_Service):

    def Not_Valid(self):

        self.context['title'] = Text(self, 88)
        self.context['form'].Set_Hidden('username')
        self.context['form'].Set_Hidden('email')

        return self.Render_Dialog(
            'prompt.html', 'password', authorization=True)

    def Manage(self):

        self.context['title'] = Text(self, 88)
        self.context['form'] = self.Prepare_Form(Form_User_Details)

        self.context['form'].Set_Hidden('username')
        self.context['form'].Set_Hidden('email')

        return self.Render_Dialog(
            'prompt.html', 'password', authorization=True)

