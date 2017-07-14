from server.manage.switch.forms.media import *
from server.content.product.models import *


class Form_Product(Abstract_Image_Form):

    def clean_price(self):

        try: return int(float(self.data['price']) * 100)
        except ValueError:
            return 0

    def clean(self):

        if self.request.session['product_is_editing']:
            return Abstract_Image_Form.clean(self)

        name = self.data['name']
        parent = self.request.session['catalog_parent']
        children = SQL.Filter(Product, parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self, 159))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        self.fields['price'] = forms.FloatField(required=False)
        self.fields['brand'] = forms.ModelChoiceField(queryset=SQL.All(Brand))
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 167))
        price_attr = self.Attr(Text(self, 168), field=Field.NUMBER)
        brand_attr = self.Attr(field=Field.SELECT)

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['price'].widget = forms.TextInput(attrs=price_attr)
        self.fields['brand'].widget.attrs = brand_attr

        Abstract_Image_Form.Set_Widgets(self)
