from server.manage.switch.forms.address import *
from server.manage.switch.website import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


class Form_Register(Abstract_Model_Form):

    def add_prefix(self, field_name):

        mapping = {
            'email':    'new_email',
            'username': 'new_username',
            'password': 'new_password',
        }

        field_name = mapping.get(field_name, field_name)
        return Abstract_Model_Form.add_prefix(self, field_name)

    def clean_password(self):
        password = self.data['new_password']
        return Base_Website.Encrypt(password)

    def Create_Fields(self):
        self.fields['captcha'] = NoReCaptchaField()

    def Set_Widgets(self):

        username_attr = self.Attr(Text(self, 44), classes='test')
        password_attr = self.Attr(Text(self, 45), classes='test', field=Field.PASSWORD)
        email_attr = self.Attr(Text(self, 46), classes='test', autofocus=True)

        self.fields['username'].widget = forms.TextInput(attrs=username_attr)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)

    class Meta:

        model = User
        fields = \
        (
            'email',
            'username',
            'password',
        )