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



class Base_Form(Base):

    def clean_secure(self):
        password = self.data['secure']

        if self.request.session['user_user']:
            user = self.request.session['user_user']

            if Base_Website.Encrypt(password) == user.password:
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

    def __init__(self, _object):
        Base.__init__(self, _object)

        self.Create_Fields()
        self.Set_Widgets()
        self.Exclude_Fields()
