from server.manage.switch.forms.address import *
from server.manage.root.models import *


class Form_Root_Login(Abstract_Form):

    def clean_password(self):
        password = self.data['password']

        if not SQL.All(Root):
            raise forms.ValidationError(Text(self, 28))

        if not SQL.Filter(Root, password=Base_Website.Encrypt(password)):
            raise forms.ValidationError(Text(self, 29))

        root = SQL.Get(Root, password=Base_Website.Encrypt(password))
        if root.password != Base_Website.Encrypt(password):
            raise forms.ValidationError(Text(self, 30))

        return Base_Website.Encrypt(password)

    def Create_Fields(self):
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):

        password_attr = self.Attr(Text(self, 31), classes='test', autofocus=True, field=Field.PASSWORD)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
