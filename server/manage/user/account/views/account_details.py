from server.manage.switch.website.manager import *
from server.manage.user.account.forms import *


class Account_Details(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['user'] = self.request.session['user_user']
        return self.Render_HTML('user/account/details.html')

    def Manage_Form_Edit_Email(self):
        details = Form_User_Details(self, post=True)

        if details.is_valid():
            user = self.request.session['user_user']
            user.email = details.cleaned_data['new_email']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Username(self):
        details = Form_User_Details(self, post=True)

        if details.is_valid():
            user = self.request.session['user_user']
            user.username = details.cleaned_data['new_username']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Password(self):
        details = Form_User_Details(self, post=True)

        if details.is_valid():
            user = self.request.session['user_user']
            user.password = details.cleaned_data['new_password']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'email':
            return self.Manage_Form_Edit_Email()

        if self.request.POST['__form__'] == 'username':
            return self.Manage_Form_Edit_Username()

        if self.request.POST['__form__'] == 'password':
            return self.Manage_Form_Edit_Password()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Account_Details(request, authorization=True).HTML
