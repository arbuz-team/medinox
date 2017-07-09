from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from server.manage.user.models import *
from server.service.translator.views import *


class Field:

    INPUT = 'input'
    TEXTAREA = 'textarea'
    SELECT = 'select'
    RADIO = 'radio'
    CHECKBOX = 'checkbox'
    NUMBER = 'input'
    EMAIL = 'input'
    URL = 'input'
    PASSWORD = 'input'
    DATE = 'input'



class Base_Form:

    def clean_secure(self):
        password = self.data['secure']

        if self.request.session['user_unique']:
            unique = self.request.session['user_unique']
            user = User.objects.get(unique=unique)

            if Dynamic_Base.Encrypt(password) == user.password:
                return True

        raise forms.ValidationError(Text(self, 85))


    def Create_Fields(self):
        pass

    def Set_Widgets(self):
        pass

    def Exclude_Fields(self):
        pass

    @staticmethod
    def Attr(placeholder='', classes='', autofocus=False,
             hidden=False, other={}, field=Field.INPUT):

        attr = {
            'placeholder':  placeholder,
            'class':        classes,
            'autofocus':    'true' if autofocus else 'false'
        }

        attr['class'] += ' ' + field
        if hidden: attr['hidden'] = 'true'
        if other: attr.update(other)

        return attr


    def Set_Secure_Form(self):

        secure_attrs = self.Attr(Text(self, 84), classes='test')

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

    def Exclude_Fields(self):

        if 'position' in self.fields:
            del self.fields['position']

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

    def clean_image_name(self):
        image_base64 = self.data['image_base64']
        image_name = self.data['image_name']

        if image_base64:
            if not image_name:
                raise forms.ValidationError(Text(self, 166))

        return image_name

    def clean_image_base64(self):
        image_base64 = self.data['image_base64']
        image_name = self.data['image_name']

        if image_base64:

            # save temp image
            manager = File_Manager()
            image_base64 = manager.Save_From_Base64(
                image_base64, image_name, File.IMAGE)

            if not image_base64:
                raise forms.ValidationError(Text(self, 66))

        return image_base64

    def clean_image_url(self):
        image_url = self.data['image_url']

        if image_url:

            # save temp image
            manager = File_Manager()
            image_url = manager.Save_From_URL(
                image_url, File.IMAGE)

            if not image_url:
                raise forms.ValidationError(Text(self, 67))

        return image_url

    def clean_image(self):

        if self.data['image_url']:
            return 'image_url'

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
        self.fields['image_url'] = forms.URLField(required=False)
        self.fields['image_name'] = forms.CharField(required=False)

    def Set_Widgets(self):

        image_attr = self.Attr()
        image_base64_attr = self.Attr(hidden=True)
        image_url_attrs = self.Attr(Text(self, 97))
        name_attrs = self.Attr(hidden=True)

        self.fields['image'].widget = forms.FileInput(attrs=image_attr)
        self.fields['image_base64'].widget = forms.TextInput(attrs=image_base64_attr)
        self.fields['image_url'].widget = forms.TextInput(attrs=image_url_attrs)
        self.fields['image_name'].widget = forms.TextInput(attrs=name_attrs)



class Abstract_File_Form(Abstract_Form):

    def clean_file_name(self):
        file_base64 = self.data['file_base64']
        file_name = self.data['file_name']

        if file_base64:
            if not file_name:
                raise forms.ValidationError(Text(self, 165))

        return file_name

    def clean_file_base64(self):
        file_base64 = self.data['file_base64']
        file_name = self.data['file_name']

        if file_base64:

            # save temp file
            manager = File_Manager()
            file_base64 = manager.Save_From_Base64(
                file_base64, file_name, File.FILE)

            if not file_base64:
                raise forms.ValidationError(Text(self, 163))

        return file_base64

    def clean_file_url(self):
        file_url = self.data['file_url']

        if file_url:

            # save temp file
            manager = File_Manager()
            file_url = manager.Save_From_URL(
                file_url, File.FILE)

            if not file_url:
                raise forms.ValidationError(Text(self, 162))

        return file_url

    def clean_file(self):

        if self.data['file_url']:
            return 'file_url'

        if self.data['file_base64']:
            return 'file_base64'

        return ''

    def clean(self):

        if self.cleaned_data['file']:
            file = self.cleaned_data['file']
            self.cleaned_data['file'] = self.cleaned_data[file]

        return self.cleaned_data

    def Create_Fields(self):
        self.fields['file'] = forms.FileField(required=False)
        self.fields['file_base64'] = forms.CharField(required=False)
        self.fields['file_url'] = forms.URLField(required=False)
        self.fields['file_name'] = forms.CharField(required=False)

    def Set_Widgets(self):

        file_attr = self.Attr()
        file_base64_attr = self.Attr(hidden=True)
        file_url_attrs = self.Attr(Text(self, 97))
        name_attrs = self.Attr(hidden=True)

        self.fields['file'].widget = forms.FileInput(attrs=file_attr)
        self.fields['file_base64'].widget = forms.TextInput(attrs=file_base64_attr)
        self.fields['file_url'].widget = forms.TextInput(attrs=file_url_attrs)
        self.fields['file_name'].widget = forms.TextInput(attrs=name_attrs)



class Abstract_Address_Form(Abstract_Model_Form):

    def Create_Fields(self):
        self.fields['country'] = forms.ChoiceField(choices=countries)

    def Set_Widgets(self):

        full_name_attr = self.Attr(Text(self, 47), classes='test', autofocus=True)
        doctor_number_attr = self.Attr(Text(self, 63), classes='test')
        address_line_attr = self.Attr(Text(self, 48), classes='test')
        city_attr = self.Attr(Text(self, 50), classes='test')
        region_attr = self.Attr(Text(self, 51), classes='test')
        postcode_attr = self.Attr(Text(self, 52), classes='test')
        country_attr = self.Attr(field=Field.SELECT)

        self.fields['full_name'].widget = forms.TextInput(attrs=full_name_attr)
        self.fields['doctor_number'].widget = forms.TextInput(attrs=doctor_number_attr)
        self.fields['address_line'].widget = forms.TextInput(attrs=address_line_attr)
        self.fields['city'].widget = forms.TextInput(attrs=city_attr)
        self.fields['region'].widget = forms.TextInput(attrs=region_attr)
        self.fields['postcode'].widget = forms.TextInput(attrs=postcode_attr)
        self.fields['country'].widget.attrs = country_attr

    def Exclude_Fields(self):

        if self.request.session['translator_language'] != 'PL':
            del self.fields['doctor_number']

        Abstract_Model_Form.Exclude_Fields(self)

    class Meta:
        exclude = '__all__'
        # fields = '__all__'
