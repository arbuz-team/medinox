from server.manage.switch.forms import *
from server.content.product.models import *


class Form_Widget(Abstract_Model_Form):

    choices = (
        ('Select', 'Select'),
        ('Checkbox', 'Checkbox'),
        ('Radio', 'Radio'),
    )

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(required=True)
        self.fields['type'] = forms.ChoiceField(self.choices)
        Abstract_Model_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self.request, 173), field=Field.INPUT)
        type_attr = self.Attr(field=Field.SELECT)

        self.fields['name'].widget.attrs = name_attr
        self.fields['type'].widget.attrs = type_attr
        Abstract_Model_Form.Set_Widgets(self)

    class Meta:

        model = Widget
        fields = (
            'name',
            'type',
        )



class Form_Values(Abstract_Model_Form):

    def clean_super_price(self):

        try: return int(float(self.data['super_price']) * 100)
        except ValueError:
            return 0

    def Create_Fields(self):
        self.fields['super_price'] = forms.FloatField(required=False)
        Abstract_Model_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self.request, 175), field=Field.INPUT)
        super_price_attr = self.Attr(Text(self.request, 174), field=Field.NUMBER)

        self.fields['name'].widget.attrs = name_attr
        self.fields['super_price'].widget.attrs = super_price_attr
        Abstract_Model_Form.Set_Widgets(self)

    class Meta:

        model = Values
        fields = (
            'name',
            'super_price',
        )



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
        children = Product.objects.filter(parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self.request, 159))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        self.fields['price'] = forms.FloatField(required=False)
        self.fields['brand'] = forms.ModelChoiceField(queryset=Brand.objects.all())
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self.request, 167))
        price_attr = self.Attr(Text(self.request, 168), field=Field.NUMBER)
        brand_attr = self.Attr(field=Field.SELECT)

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['price'].widget = forms.TextInput(attrs=price_attr)
        self.fields['brand'].widget = forms.Select(attrs=brand_attr)

        Abstract_Image_Form.Set_Widgets(self)



class Form_Description(Abstract_Image_Form):

    def Create_Fields(self):
        self.fields['header'] = forms.CharField(required=False)
        self.fields['paragraph'] = forms.CharField(required=False)
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        header_attr = self.Attr(Text(self.request, 95), classes='test')
        paragraph_attr = self.Attr(Text(self.request, 96), classes='test', field=Field.TEXTAREA)

        self.fields['header'].widget = forms.TextInput(attrs=header_attr)
        self.fields['paragraph'].widget = forms.Textarea(attrs=paragraph_attr)
        Abstract_Image_Form.Set_Widgets(self)
