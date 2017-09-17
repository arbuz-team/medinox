from server.manage.switch.forms.address import *
from server.manage.switch.website import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


class Form_Register(Abstract_Model_Form):

    def clean_password(self):
        password = self.data['password']
        return Base_Website.Encrypt(password)

    def Create_Fields(self):
        self.fields['captcha'] = NoReCaptchaField()

    def Set_Widgets(self):

        username_attr = self.Attr(Text(self, 44), classes='test')
        password_attr = self.Attr(Text(self, 45), classes='test', field=Field.PASSWORD)
        email_attr = self.Attr(Text(self, 46), classes='test', autofocus=True)
        phone_attr = self.Attr(Text(self, 197), classes='test')

        self.fields['username'].widget = forms.TextInput(attrs=username_attr)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)
        self.fields['phone'].widget = forms.TextInput(attrs=phone_attr)

    class Meta:

        model = Model_User
        fields = \
        (
            'email',
            'username',
            'phone',
            'password',
        )
