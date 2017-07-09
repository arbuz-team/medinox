from server.manage.switch.forms import *
from server.manage.root.models import *


class Form_Root_Login(Abstract_Form):

    def clean_password(self):
        password = self.data['password']

        if not Root.objects.all():
            raise forms.ValidationError(Text(self, 28))

        if not Root.objects.filter(password=Dynamic_Base.Encrypt(password)):
            raise forms.ValidationError(Text(self, 29))

        root = Root.objects.get(password=Dynamic_Base.Encrypt(password))
        if root.password != Dynamic_Base.Encrypt(password):
            raise forms.ValidationError(Text(self, 30))

        return Dynamic_Base.Encrypt(password)

    def Create_Fields(self):
        self.fields['password'] = forms.CharField(max_length=100)

    def Set_Widgets(self):

        password_attr = self.Attr(Text(self, 31), classes='test', autofocus=True, field=Field.PASSWORD)
        self.fields['password'].widget = forms.PasswordInput(attrs=password_attr)



class Form_Root_Address(Abstract_Address_Form):

    def Set_Widgets(self):

        phone_attr = self.Attr(Text(self, 139))
        email_attr = self.Attr(Text(self, 140), classes='test')

        self.fields['phone'].widget = forms.TextInput(attrs=phone_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)

        Abstract_Address_Form.Set_Widgets(self)

    class Meta(Abstract_Address_Form.Meta):
        model = Root_Address