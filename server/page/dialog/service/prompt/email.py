from server.page.dialog.service.base import *


class Service_Email(Base_Service):

    def Manage(self):

        self.content['title'] = Text(self.request, 86)
        self.content['form'] = self.Prepare_Form(Form_User_Details)

        self.content['form'].Set_Hidden('new_username')
        self.content['form'].Set_Hidden('new_password')

        return self.dialog.Render_Dialog(
            'dialog/prompt.html', 'email', authorization=True)

