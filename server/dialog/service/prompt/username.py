from server.dialog.service.base import *


class Service_Username(Base_Service):

    def Manage(self):

        self.context['title'] = Text(self, 87)
        self.context['form'] = self.Prepare_Form(Form_User_Details)

        self.context['form'].Set_Hidden('new_email')
        self.context['form'].Set_Hidden('new_password')

        return self.Render_Dialog(
            'prompt.html', 'username', authorization=True)

