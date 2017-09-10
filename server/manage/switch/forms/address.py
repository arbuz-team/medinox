from server.manage.switch.forms.standard import *


class Abstract_Address_Form(Abstract_Model_Form):

    def Create_Fields(self):
        self.fields['country'] = forms.ChoiceField(choices=countries)

    def Set_Widgets(self):

        full_name_attr = self.Attr(Text(self, 47), classes='test', autocomplite='', autofocus=True)
        doctor_number_attr = self.Attr(Text(self, 63), classes='test', autocomplite='')
        address_line_attr = self.Attr(Text(self, 48), classes='test', autocomplite='')
        city_attr = self.Attr(Text(self, 50), classes='test', autocomplite='')
        region_attr = self.Attr(Text(self, 51), classes='test', autocomplite='')
        postcode_attr = self.Attr(Text(self, 52), classes='test', autocomplite='')
        country_attr = self.Attr(field=Field.SELECT, autocomplite='')

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
