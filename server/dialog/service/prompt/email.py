from server.dialog.service.base import *


class Service_Email(Base_Service):

    def Manage(self):

        self.context['title'] = Text(self, 86)
        self.context['form'] = self.Prepare_Form(Form_User_Details)

        self.context['form'].Set_Hidden('new_username')
        self.context['form'].Set_Hidden('new_password')

        return self.Render_Dialog(
            'prompt.html', 'email', authorization=True)

