from server.manage.switch.forms.media import *
from server.service.payment.models import *


class Form_Order_Deadline(Abstract_Model_Form):

    def Create_Fields(self):

        self.fields['name'] = forms.CharField()
        self.fields['deadline'] = forms.DateField(required=False)
        self.fields['reminder'] = forms.DateField(required=False)
        self.fields['send_to_client'] = forms.BooleanField(required=False)
        self.fields['send_to_root'] = forms.BooleanField(required=False)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 170))
        deadline_attr = self.Attr(other={'type': 'date'}, field=Field.DATE)
        reminder_attr = self.Attr(other={'type': 'date'}, field=Field.DATE)
        stb_attr = self.Attr(field=Field.CHECKBOX)
        str_attr = self.Attr(field=Field.CHECKBOX)

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['deadline'].widget = forms.DateInput(attrs=deadline_attr)
        self.fields['reminder'].widget = forms.DateInput(attrs=reminder_attr)
        self.fields['send_to_client'].widget = forms.CheckboxInput(attrs=stb_attr)
        self.fields['send_to_root'].widget = forms.CheckboxInput(attrs=str_attr)

    class Meta:
        model = Model_Deadline
        fields = ('name', 'deadline', 'reminder',
                  'send_to_client', 'send_to_root')
