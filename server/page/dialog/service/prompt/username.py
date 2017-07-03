from server.page.dialog.service.base import *


class Service_Username(Base_Service):

    def Manage(self):

        self.content['title'] = Text(self.request, 87)
        self.content['form'] = self.Prepare_Form(Form_User_Details)

        self.content['form'].Set_Hidden('new_email')
        self.content['form'].Set_Hidden('new_password')

        return self.Render_Dialog(
            'prompt.html', 'username', authorization=True)

