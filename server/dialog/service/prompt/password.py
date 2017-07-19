from server.dialog.service.base import *


class Service_Password(Base_Service):

    def Manage(self):

        self.context['title'] = Text(self, 88)
        self.context['form'] = self.Prepare_Form(Form_User_Details)

        self.context['form'].Set_Hidden('new_username')
        self.context['form'].Set_Hidden('new_email')

        return self.Render_Dialog(
            'prompt.html', 'password', authorization=True)

