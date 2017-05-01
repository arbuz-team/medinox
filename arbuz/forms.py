from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from user.models import *
from translator.views import *


class Base_Form:

    def clean_secure(self):
        password = self.data['secure']

        if self.request.session['user_unique']:
            unique = self.request.session['user_unique']
            user = User.objects.get(unique=unique)

            if Dynamic_Base.Encrypt(password) == user.password:
                return True

        raise forms.ValidationError(Text(self.request, 85))


    def Create_Fields(self):
        pass

    def Set_Widgets(self):
        pass

    def Exclude_Fields(self):
        pass


    def Set_Secure_Form(self):

        secure_attrs = {
            'placeholder': Text(self.request, 84),
            'class': 'test',
        }

        self.fields['secure'] = forms.CharField(max_length=100)
        self.fields['secure'].widget = forms.PasswordInput(attrs=secure_attrs)

    def __init__(self, request):
        self.request = request

        self.Create_Fields()
        self.Set_Widgets()
        self.Exclude_Fields()



class Abstract_Model_Form(Base_Form, forms.ModelForm):

    def Edit_Instance(self):
        pass

    def __init__(self, request, *args, **kwargs):

        if 'instance' in kwargs:
            self.instance = kwargs['instance']
            self.Edit_Instance()

        forms.ModelForm.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, request)



class Abstract_Form(Base_Form, forms.Form):

    def __init__(self, request, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, request)



class Abstract_Image_Form(Abstract_Form):

    def clean_image_base64(self):
        image_base64 = self.data['image_base64']

        if image_base64:
            image_base64 = Dynamic_Base.\
                Save_Image_From_Base64(image_base64)

            if not image_base64:
                raise forms.ValidationError(Text(self.request, 66))

        return image_base64

    def clean_url(self):
        image_url = self.data['url']

        if image_url:
            image_url = Dynamic_Base.\
                Save_Image_From_URL(image_url)

            if not image_url:
                raise forms.ValidationError(Text(self.request, 67))

        return image_url

    def clean_image(self):

        if self.data['url']:
            return 'url'

        if self.data['image_base64']:
            return 'image_base64'

        return ''

    def clean(self):

        if self.cleaned_data['image']:
            image = self.cleaned_data['image']
            self.cleaned_data['image'] = self.cleaned_data[image]

        return self.cleaned_data

    def Create_Fields(self):
        self.fields['image'] = forms.ImageField(required=False)
        self.fields['image_base64'] = forms.CharField(required=False)
        self.fields['url'] = forms.URLField(required=False)

    def Set_Widgets(self):

        image_base64_attr = {
            'hidden': 'true'
        }

        url_attrs = {
            'placeholder': Text(self.request, 97)
        }

        self.fields['image_base64'].widget = forms.TextInput(attrs=image_base64_attr)
        self.fields['url'].widget = forms.TextInput(attrs=url_attrs)



class Abstract_Address_Form(Abstract_Model_Form):

    def Create_Fields(self):
        self.fields['country'] = LazyTypedChoiceField(choices=countries)

    def Set_Widgets(self):

        full_name_attr = {
            'placeholder': Text(self.request, 47),
            'class': 'test',
            'autofocus': 'true',
        }

        doctor_number_attr = {
            'placeholder': Text(self.request, 63),
            'class': 'test',
        }

        address_line_attr = {
            'placeholder': Text(self.request, 48),
            'class': 'test',
        }

        city_attr = {
            'placeholder': Text(self.request, 50),
            'class': 'test',
        }

        region_attr = {
            'placeholder': Text(self.request, 51),
            'class': 'test',
        }

        postcode_attr = {
            'placeholder': Text(self.request, 52),
            'class': 'test',
        }

        self.fields['full_name'].widget = forms.TextInput(attrs=full_name_attr)
        self.fields['doctor_number'].widget = forms.TextInput(attrs=doctor_number_attr)
        self.fields['address_line'].widget = forms.TextInput(attrs=address_line_attr)
        self.fields['city'].widget = forms.TextInput(attrs=city_attr)
        self.fields['region'].widget = forms.TextInput(attrs=region_attr)
        self.fields['postcode'].widget = forms.TextInput(attrs=postcode_attr)

    def Exclude_Fields(self):
        if self.request.session['translator_language'] != 'PL':
            del self.fields['doctor_number']

    class Meta:
        exclude = '__all__'
        # fields = '__all__'
