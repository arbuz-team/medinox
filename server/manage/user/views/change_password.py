from server.manage.user.forms import *


class Change_Password(Website_Manager):

    def Manage_Content(self):
        self.context['form'] = Form_Change_Password(self)
        return self.Render_HTML('user/change_password.html', 'change_password')

    def Manage_Form_Change_Password(self):
        self.context['form'] = Form_Change_Password(self, post=True)

        if self.context['form'].is_valid():

            key = self.other_value['key']
            record = SQL.Get(Forgot_Password_User, approved_key=key)
            record.user.password = self.context['form'].cleaned_data['password']
            SQL.Save(data=record.user)

            SQL.Delete(data=record, force=True)
            self.context['form'] = None  # message of correct

            return self.Render_HTML('user/change_password.html')

        return self.Render_HTML('user/change_password.html', 'change_password')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'change_password':
            return self.Manage_Form_Change_Password()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Secure(request, key):
        all_keys = Forgot_Password_User.objects.values('approved_key')

        if {'approved_key': key} in all_keys:
            value = {'key': key}
            return Change_Password(request, other_value=value).HTML

        return Change_Password(request, error_method='Error_Authorization').HTML

    @staticmethod
    def Launch(request):
        return Change_Password(request).HTML
