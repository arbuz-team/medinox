from server.manage.switch.website.manager import *
from server.manage.user.account.forms import *


class Account_Details(Website_Manager):

    def Manage_Content(self):
        self.context['user'] = self.request.session['user_user']
        return self.Render_HTML('user/account/details.html')

    def Manage_Form_Edit_Email(self):
        self.context['form'] = Form_User_Details(self, post=True)

        if self.context['form'].is_valid():
            data = self.context['form'].cleaned_data

            user = self.request.session['user_user']
            user.email = data['email']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Username(self):
        self.context['form'] = Form_User_Details(self, post=True)

        if self.context['form'].is_valid():
            data = self.context['form'].cleaned_data

            user = self.request.session['user_user']
            user.username = data['username']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Password(self):
        self.context['form'] = Form_User_Details(self, post=True)

        if self.context['form'].is_valid():
            data = self.context['form'].cleaned_data

            user = self.request.session['user_user']
            user.password = data['password']
            SQL.Save(data=user)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'email':
            return self.Manage_Form_Edit_Email()

        if self.request.POST['_name_'] == 'username':
            return self.Manage_Form_Edit_Username()

        if self.request.POST['_name_'] == 'password':
            return self.Manage_Form_Edit_Password()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Account_Details(request, authorization=True).HTML
