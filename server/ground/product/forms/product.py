from server.manage.switch.forms.media import *
from server.ground.product.models import *


class Form_Product(Abstract_Image_Form):

    def clean_price_pln(self):
        if 'price_pln' not in self.data: return 0
        if not self.data['price_pln']: return 0
        return self.data['price_pln']

    def clean(self):

        if self.request.session['product_is_editing']:
            return Abstract_Image_Form.clean(self)

        name = self.data['name']
        parent = self.request.session['catalog_parent']
        children = SQL.Filter(Model_Product, parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self, 159))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        self.fields['price_pln'] = forms.FloatField(required=False)
        self.fields['price_eur'] = forms.FloatField(required=False)
        self.fields['price_gbp'] = forms.FloatField(required=False)
        self.fields['brand'] = forms.ModelChoiceField(queryset=SQL.All(Model_Brand),
                                empty_label=Text(self, 275), required=False)

        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 167))
        price_pln_attr = self.Attr(Text(self, 185), field=Field.NUMBER, classes='currency_converter-field')
        price_eur_attr = self.Attr(Text(self, 184), field=Field.NUMBER, classes='currency_converter-field', other={'disabled': 'true'})
        price_gbp_attr = self.Attr(Text(self, 186), field=Field.NUMBER, classes='currency_converter-field', other={'disabled': 'true'})
        brand_attr = self.Attr(field=Field.SELECT)

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['price_pln'].widget = forms.TextInput(attrs=price_pln_attr)
        self.fields['price_eur'].widget = forms.TextInput(attrs=price_eur_attr)
        self.fields['price_gbp'].widget = forms.TextInput(attrs=price_gbp_attr)
        self.fields['brand'].widget.attrs = brand_attr

        Abstract_Image_Form.Set_Widgets(self)
