from server.manage.switch.forms.address import *
from server.manage.user.models import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


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



class Form_User_Address(Abstract_Address_Form):

    class Meta(Abstract_Address_Form.Meta):
        model = User_Address
        exclude = ('user', )



class Form_Forgot_Password(Abstract_Form):

    def clean_email(self):
        email = self.data['email']

        if not SQL.Filter(User, email=email):
            raise forms.ValidationError(Text(self, 54))

        if not SQL.Get(User, email=email).approved:
            raise forms.ValidationError(Text(self, 55))

        return email

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50)

    def Set_Widgets(self):
        widget_attr = self.Attr(Text(self, 56), classes='test', autofocus=True)
        self.fields['email'].widget = forms.TextInput(attrs=widget_attr)



class Form_Change_Password(Abstract_Form):

    def clean_password(self):
        return Base_Website.Encrypt(self.data['password'])

    def Create_Fields(self):
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):
        password_attr = self.Attr(Text(self, 57), classes='test', autofocus=True)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
