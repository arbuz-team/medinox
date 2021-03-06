from server.manage.switch.forms.media import *
from server.ground.main.models import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


class Form_Email_Contact(Abstract_Form):

    def Create_Fields(self):
        self.fields['title'] = forms.CharField(max_length=100, initial=Text(self, 83))
        self.fields['client'] = forms.CharField(max_length=50)
        self.fields['email'] = forms.EmailField(max_length=50)
        self.fields['product'] = forms.CharField(max_length=50, required=False)
        self.fields['url'] = forms.URLField(required=False)
        self.fields['message'] = forms.CharField(max_length=2000)
        self.fields['captcha'] = NoReCaptchaField()

    def Set_Widgets(self):

        title_attr = self.Attr(Text(self, 71), hidden=True)
        client_attr = self.Attr(Text(self, 72), classes='test')
        email_attr = self.Attr(Text(self, 73), classes='test', field=Field.EMAIL)
        message_attr = self.Attr(Text(self, 74), classes='test', field=Field.TEXTAREA)
        product_attr = self.Attr(Text(self, 79), hidden=True)
        url_attr = self.Attr(Text(self, 80), hidden=True)

        self.fields['title'].widget = forms.TextInput(attrs=title_attr)
        self.fields['client'].widget = forms.TextInput(attrs=client_attr)
        self.fields['email'].widget = forms.EmailInput(attrs=email_attr)
        self.fields['message'].widget = forms.Textarea(attrs=message_attr)
        self.fields['product'].widget = forms.TextInput(attrs=product_attr)
        self.fields['url'].widget = forms.URLInput(attrs=url_attr)
