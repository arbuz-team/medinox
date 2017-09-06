from server.manage.switch.forms.address import *
from server.manage.switch.website import *


class Form_Forgot_Password(Abstract_Form):

    def clean_email(self):
        email = self.data['email']

        if not SQL.Filter(Model_User, email=email):
            raise forms.ValidationError(Text(self, 54))

        if not SQL.Get(Model_User, email=email).approved:
            raise forms.ValidationError(Text(self, 55))

        return email

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50)

    def Set_Widgets(self):
        widget_attr = self.Attr(Text(self, 56), classes='test', autofocus=True)
        self.fields['email'].widget = forms.TextInput(attrs=widget_attr)
