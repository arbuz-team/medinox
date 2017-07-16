from server.dialog.service.base import *


class Service_Password(Base_Service):

    def Manage(self):

        self.content['title'] = Text(self, 88)
        self.content['form'] = self.Prepare_Form(Form_User_Details)

        self.content['form'].Set_Hidden('new_username')
        self.content['form'].Set_Hidden('new_email')

        return self.Render_Dialog(
            'prompt.html', 'password', authorization=True)

