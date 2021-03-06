from server.manage.switch.forms.media import *
from server.ground.product.models import *


class Form_Element_Operation(Abstract_Form):

    choices = (
        ('EN', 'English'),
        ('PL', 'Polski'),
    )

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(required=True)
        self.fields['language'] = forms.ChoiceField(
            self.choices, widget=forms.RadioSelect())

        Abstract_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 176), field=Field.INPUT)
        type_attr = self.Attr(field=Field.RADIO)

        self.fields['name'].widget.attrs = name_attr
        self.fields['language'].widget.attrs = type_attr
        Abstract_Form.Set_Widgets(self)



class Form_Copy(Form_Element_Operation):
    pass

class Form_Move(Form_Element_Operation):
    pass



class Form_Restore(Abstract_Form):

    def clean_restore_name(self):

        name = self.data['restore_name']
        model = self.request.session['catalog_restore_type']
        pk = self.request.session['catalog_restore_pk']

        parent = SQL.Get(model, deleted=True, pk=pk).parent
        if SQL.Filter(model, name=name, parent=parent):
            raise forms.ValidationError(Text(self, 277))

        return name

    def Create_Fields(self):
        self.fields['restore_name'] = forms.CharField(required=True)
        Abstract_Form.Create_Fields(self)
