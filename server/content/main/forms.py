from server.manage.switch.forms import *
from server.content.main.models import *
from nocaptcha_recaptcha.fields import NoReCaptchaField


class Form_Email_Contact(Abstract_Form):

    def Create_Fields(self):
        self.fields['title'] = forms.CharField(max_length=100, initial=Text(self.request, 83))
        self.fields['client'] = forms.CharField(max_length=50)
        self.fields['email'] = forms.EmailField(max_length=50)
        self.fields['product'] = forms.CharField(max_length=50, required=False)
        self.fields['url'] = forms.URLField(required=False)
        self.fields['message'] = forms.CharField(max_length=2000)
        self.fields['captcha'] = NoReCaptchaField()

    def Set_Widgets(self):

        title_attr = self.Attr(Text(self.request, 71), hidden=True)
        client_attr = self.Attr(Text(self.request, 72), classes='test')
        email_attr = self.Attr(Text(self.request, 73), classes='test', field=Field.EMAIL)
        message_attr = self.Attr(Text(self.request, 74), classes='test', field=Field.TEXTAREA)
        product_attr = self.Attr(Text(self.request, 79), hidden=True)
        url_attr = self.Attr(Text(self.request, 80), hidden=True)

        self.fields['title'].widget = forms.TextInput(attrs=title_attr)
        self.fields['client'].widget = forms.TextInput(attrs=client_attr)
        self.fields['email'].widget = forms.EmailInput(attrs=email_attr)
        self.fields['message'].widget = forms.Textarea(attrs=message_attr)
        self.fields['product'].widget = forms.TextInput(attrs=product_attr)
        self.fields['url'].widget = forms.URLInput(attrs=url_attr)



class Form_About_Content(Abstract_Image_Form):

    def Create_Fields(self):
        self.fields['header'] = forms.CharField(required=False)
        self.fields['paragraph'] = forms.CharField(required=False)
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        header_attr = {
            'placeholder': Text(self.request, 95),
            'class': 'test',
        }

        paragraph_attr = {
            'placeholder': Text(self.request, 96),
            'class': 'test',
        }

        self.fields['header'].widget = forms.TextInput(attrs=header_attr)
        self.fields['paragraph'].widget = forms.Textarea(attrs=paragraph_attr)
        Abstract_Image_Form.Set_Widgets(self)
