from server.manage.switch.forms.address import *
from server.manage.switch.website import *


class Form_Change_Password(Abstract_Form):

    def clean_password(self):
        return Base_Website.Encrypt(self.data['password'])

    def Create_Fields(self):
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):
        password_attr = self.Attr(Text(self, 57), classes='test', autofocus=True)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
