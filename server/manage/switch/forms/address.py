from server.manage.switch.forms.standard import *


class Abstract_Address_Form(Abstract_Model_Form):

    def Create_Fields(self):
        self.fields['country'] = forms.ChoiceField(choices=countries)
        self.fields['nip'] = forms.CharField(max_length=20, required=False)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 200), classes='test', autocomplite='', autofocus=True)
        surname_attr = self.Attr(Text(self, 201), classes='test', autocomplite='')
        company_name_attr = self.Attr(Text(self, 202), classes='test', autocomplite='')
        nip_attr = self.Attr(Text(self, 199), classes='test', autocomplite='')
        address_line_attr = self.Attr(Text(self, 48), classes='test', autocomplite='')
        city_attr = self.Attr(Text(self, 50), classes='test', autocomplite='')
        region_attr = self.Attr(Text(self, 51), classes='test', autocomplite='')
        postcode_attr = self.Attr(Text(self, 52), classes='test', autocomplite='')
        country_attr = self.Attr(field=Field.SELECT, autocomplite='')

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['surname'].widget = forms.TextInput(attrs=surname_attr)
        self.fields['company_name'].widget = forms.TextInput(attrs=company_name_attr)
        self.fields['nip'].widget = forms.TextInput(attrs=nip_attr)
        self.fields['address_line'].widget = forms.TextInput(attrs=address_line_attr)
        self.fields['city'].widget = forms.TextInput(attrs=city_attr)
        self.fields['region'].widget = forms.TextInput(attrs=region_attr)
        self.fields['postcode'].widget = forms.TextInput(attrs=postcode_attr)
        self.fields['country'].widget.attrs = country_attr

    def Exclude_Fields(self):

        # if self.request.session['translator_language'] != 'PL':
        #     del self.fields['doctor_number']

        Abstract_Model_Form.Exclude_Fields(self)

    class Meta:
        exclude = '__all__'
        # fields = '__all__'
