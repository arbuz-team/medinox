from server.manage.switch.website.base import *
from server.manage.switch.forms.standard import *


class Form_User_Details(Abstract_Form):

    def clean_password(self):
        password = self.data['password']
        return Base_Website.Encrypt(password)

    def clean(self):
        email = self.data['email']
        username = self.data['username']
        password = self.data['password']

        if not (email or username or password):
            raise forms.ValidationError(Text(self, 92))

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50, required=False)
        self.fields['username'] = forms.CharField(max_length=20, required=False)
        self.fields['password'] = forms.CharField(max_length=100, required=False)
        self.Set_Secure_Form()

    def Set_Widgets(self):

        username_attr = self.Attr(Text(self, 90), classes='test')
        password_attr = self.Attr(Text(self, 91), classes='test')
        email_attr = self.Attr(Text(self, 89), classes='test')

        self.fields['username'].widget = forms.TextInput(attrs=username_attr)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)

    def Set_Hidden(self, field):
        self.fields[field].widget.attrs = {'hidden': 'true'}
