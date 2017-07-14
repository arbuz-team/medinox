from server.manage.switch.forms.media import *
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

        name_attr = self.Attr(Text(self, 173), field=Field.INPUT)
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
