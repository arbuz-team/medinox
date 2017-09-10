from server.service.sender.views import *
from server.manage.user.forms import *
import os


class Forgot_Password(Website_Manager):

    def Manage_Content(self):
        self.context['form'] = Form_Forgot_Password(self)
        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form_Forgot_Password(self):
        self.context['form'] = Form_Forgot_Password(self, post=True)

        if self.context['form'].is_valid():
            self.context['email'] = self.context['form'].cleaned_data['email']

            if SQL.Filter(Model_User, email=self.context['email']):
                self.Create_Forgot_Password_User()
                self.Send_Secure_Link()

            self.context['form'] = None  # message of correct

            return self.Render_HTML('user/forgot.html')

        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'forgot_password':
            return self.Manage_Form_Forgot_Password()

        return Website_Manager.Manage_Form(self)

    def Create_Forgot_Password_User(self):
        self.context['key'] = self.Generate_Random_Chars(
            20, punctuation=False, uppercase=False)

        if not SQL.Filter(Model_Forgot_Password_User, approved_key=self.context['key']):
            SQL.Save(Model_Forgot_Password_User,
                user=SQL.Get(Model_User, email=self.context['email']),
                approved_key=self.context['key']
            )

        else: self.Create_Forgot_Password_User()

    def Send_Secure_Link(self):

        path_manager = Path_Manager(self)
        activate_key = self.context['key']
        activate_url = path_manager.Get_Urls('user.change_password',
             kwargs={'key': activate_key}, current_language=True)

        email = self.context['email']

        content = {
            'activate_url': activate_url,
            'user':         SQL.Get(Model_User, email=email)
        }

        Sender(self).Send_Forgot_Password_Link(content, email)

    def Manage_Exist(self):

        if self.request.POST['_name_'] == 'email':
            if SQL.Filter(Model_User, email=self.request.POST['value']):
                return HttpResponse('true')

        return HttpResponse('false')

    @staticmethod
    def Launch(request):
        return Forgot_Password(request).HTML
