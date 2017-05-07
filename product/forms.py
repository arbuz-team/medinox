from arbuz.forms import *
from product.models import *


class Form_Widget(Abstract_Model_Form):

    choices = (
        (0, 'Select'),
        (1, 'Checkbox'),
        (2, 'Radio'),
    )

    def clean_type(self):
        number = int(self.data['type'])
        return self.choices[number][1]

    def Create_Fields(self):
        self.fields['type'] = forms.ChoiceField(self.choices)

    class Meta:

        model = Widget
        fields = (
            'name',
            'type',
        )



class Form_Values(Abstract_Model_Form):

    def clean_super_price(self):

        price = float(self.data['super_price'])
        if price:
            return int(price * 100)

        return 0

    def Create_Fields(self):
        self.fields['super_price'] = forms.FloatField(required=False)

    class Meta:

        model = Values
        fields = (
            'name',
            'super_price',
        )



class Form_Product(Abstract_Image_Form):

    def clean_price(self):

        price = float(self.data['price'])
        if price:
            return int(price * 100)

        return 0

    def clean(self):

        name = self.data['name']
        parent = self.request.session['catalog_parent']
        children = Product.objects.filter(parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self.request, 159))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        self.fields['price'] = forms.FloatField(required=False)
        Abstract_Image_Form.Create_Fields(self)
