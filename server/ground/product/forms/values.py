from server.manage.switch.forms.media import *
from server.ground.product.models import *


class Form_Values(Abstract_Model_Form):

    def clean_super_price(self):

        try: return int(float(self.data['super_price']) * 100)
        except ValueError:
            return 0

    def Create_Fields(self):
        self.fields['super_price'] = forms.FloatField(required=False)
        Abstract_Model_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 175), field=Field.INPUT)
        super_price_attr = self.Attr(Text(self, 174), field=Field.NUMBER)

        self.fields['name'].widget.attrs = name_attr
        self.fields['super_price'].widget.attrs = super_price_attr
        Abstract_Model_Form.Set_Widgets(self)

    class Meta:

        model = Model_Values
        fields = (
            'name',
            'super_price',
        )
