from server.service.sender.views import *
from server.manage.user.forms import *
import os, binascii


class Forgot_Password(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Forgot_Password(self)
        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form_Forgot_Password(self):
        self.content['form'] = Form_Forgot_Password(self, post=True)

        if self.content['form'].is_valid():
            self.content['email'] = self.content['form'].cleaned_data['email']

            if SQL.Filter(User, email=self.content['email']):
                self.Create_Forgot_Password_User()
                self.Send_Secure_Link()

            self.content['form'] = None  # message of correct

            return self.Render_HTML('user/forgot.html')

        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'forgot_password':
            return self.Manage_Form_Forgot_Password()

        return Website_Manager.Manage_Form(self)

    def Create_Forgot_Password_User(self):
        self.content['key'] = binascii.hexlify(os.urandom(20))

        if not SQL.Filter(Forgot_Password_User, approved_key=self.content['key']):
            SQL.Save(Forgot_Password_User,
                user=SQL.Get(User, email=self.content['email']),
                approved_key=self.content['key']
            )

        else: self.Create_Forgot_Password_User()

    def Send_Secure_Link(self):

        path_manager = Path_Manager(self)
        activate_key = self.content['key'].decode("utf-8")
        activate_url = path_manager.Get_Urls('user.change_password',
             kwargs={'key': activate_key}, current_language=True)

        email = self.content['email']

        content = {
            'activate_url': activate_url,
            'user':         SQL.Get(User, email=email)
        }

        Sender(self).Send_Forgot_Password_Link(content, email)

    def Manage_Exist(self):

        if self.request.POST['__exist__'] == 'email':
            if SQL.Filter(User, email=self.request.POST['value']):
                return JsonResponse({'__exist__': 'true'})

        return JsonResponse({'__exist__': 'false'})

    @staticmethod
    def Launch(request):
        return Forgot_Password(request).HTML
