from server.manage.switch.forms.address import *
from server.manage.switch.website import *


class Form_Login(Abstract_Form):

    def clean_email(self):
        email = self.data['email']

        if not SQL.Filter(User, email=email):
            raise forms.ValidationError(Text(self, 41))

        if not SQL.Get(User, email=email).approved:
            raise forms.ValidationError(Text(self, 42))

        return email

    def clean_password(self):
        email = self.data['email']
        password = self.data['password']

        if not SQL.Filter(User, email=email):
            return ''

        user = SQL.Get(User, email=email)
        if user.password != Base_Website.Encrypt(password):
            raise forms.ValidationError(Text(self, 43))

        return Base_Website.Encrypt(password)

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50)
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):

        email_attrs = self.Attr(Text(self, 39), classes='test', autofocus=True)
        password_attrs = self.Attr(Text(self, 40), classes='test')

        self.fields['email'].widget = forms.TextInput(attrs=email_attrs)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attrs)
