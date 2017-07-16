from server.manage.switch.forms.media import *


class Form_Copy(Abstract_Form):

    choices = (
        ('EN', 'English'),
        ('PL', 'Polski'),
        ('DE', 'Deutsch'),
    )

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(required=True)
        self.fields['language'] = forms.ChoiceField(self.choices)
        Abstract_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 176), field=Field.INPUT)
        type_attr = self.Attr(field=Field.SELECT)

        self.fields['name'].widget.attrs = name_attr
        self.fields['language'].widget.attrs = type_attr
        Abstract_Form.Set_Widgets(self)
