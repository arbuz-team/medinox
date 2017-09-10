from server.manage.switch.website.base import *
from server.manage.switch.forms.standard import *


class Form_User_Details(Abstract_Form):

    def clean_new_password(self):
        password = self.data['new_password']
        return Base_Website.Encrypt(password)

    def clean(self):
        new_email = self.data['new_email']
        new_username = self.data['new_username']
        new_password = self.data['new_password']

        if not (new_email or new_username or new_password):
            raise forms.ValidationError(Text(self, 92))

    def Create_Fields(self):
        self.fields['new_email'] = forms.CharField(max_length=50, required=False)
        self.fields['new_username'] = forms.CharField(max_length=20, required=False)
        self.fields['new_password'] = forms.CharField(max_length=100, required=False)
        self.Set_Secure_Form()

    def Set_Widgets(self):

        new_username_attr = self.Attr(Text(self, 90), classes='test')
        new_password_attr = self.Attr(Text(self, 91), classes='test')
        new_email_attr = self.Attr(Text(self, 89), classes='test')

        self.fields['new_username'].widget = forms.TextInput(attrs=new_username_attr)
        self.fields['new_password'].widget = forms.PasswordInput(attrs=new_password_attr)
        self.fields['new_email'].widget = forms.TextInput(attrs=new_email_attr)

    def Set_Hidden(self, field):
        self.fields[field].widget.attrs = {'hidden': 'true'}
