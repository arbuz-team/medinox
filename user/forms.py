from arbuz.forms import *
from user.models import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


class Form_Login(Abstract_Form):

    def clean_email(self):
        email = self.data['email']

        if not User.objects.filter(email=email):
            raise forms.ValidationError(Text(self.request, 41))

        if not User.objects.get(email=email).approved:
            raise forms.ValidationError(Text(self.request, 42))

        return email

    def clean_password(self):
        email = self.data['email']
        password = self.data['password']

        if not User.objects.filter(email=email):
            return ''

        user = User.objects.get(email=email)
        if user.password != Dynamic_Base.Encrypt(password):
            raise forms.ValidationError(Text(self.request, 43))

        return Dynamic_Base.Encrypt(password)

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50)
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):

        email_attrs = {
            'placeholder': Text(self.request, 39),
            'class': 'test',
            'autofocus': 'true',
        }

        password_attrs = {
            'placeholder': Text(self.request, 40),
            'class': 'test',
        }

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
        return Dynamic_Base.Encrypt(password)

    def Create_Fields(self):
        self.fields['captcha'] = NoReCaptchaField()

    def Set_Widgets(self):

        username_attr = {
            'placeholder': Text(self.request, 44),
            'class': 'test',
        }

        password_attr = {
            'placeholder': Text(self.request, 45),
            'class': 'test',
        }

        email_attr = {
            'placeholder': Text(self.request, 46),
            'class': 'test',
            'autofocus': 'true',
        }

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

        if not User.objects.filter(email=email):
            raise forms.ValidationError(Text(self.request, 54))

        if not User.objects.get(email=email).approved:
            raise forms.ValidationError(Text(self.request, 55))

        return email

    def Create_Fields(self):
        self.fields['email'] = forms.CharField(max_length=50)

    def Set_Widgets(self):

        widget_attr = {
            'placeholder': Text(self.request, 56),
            'class': 'test',
            'autofocus': 'true',
        }

        self.fields['email'].widget = forms.TextInput(attrs=widget_attr)



class Form_Change_Password(Abstract_Form):

    def clean_password(self):
        return Dynamic_Base.Encrypt(self.data['password'])

    def Create_Fields(self):
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):

        password_attr = {
            'placeholder': Text(self.request, 57),
            'class': 'test',
            'autofocus': 'true',
        }

        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)
