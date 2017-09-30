from server.manage.switch.forms.media import *


class Form_Element_Operation(Abstract_Form):

    choices = (
        ('EN', 'English'),
        ('PL', 'Polski'),
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



class Form_Copy(Form_Element_Operation):
    pass

class Form_Move(Form_Element_Operation):
    pass
