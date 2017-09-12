from server.manage.switch.forms.standard import *


class Form_Send_Email(Abstract_Form):

    def Create_Fields(self):
        self.fields['title'] = forms.CharField(required=True)
        self.fields['message'] = forms.CharField(required=True)

    def Set_Widgets(self):

        title_attr = self.Attr(Text(self, 190))
        message_attr = self.Attr(Text(self, 191), field=Field.TEXTAREA)

        self.fields['title'].widget = forms.TextInput(attrs=title_attr)
        self.fields['message'].widget = forms.Textarea(attrs=message_attr)

        Abstract_Form.Set_Widgets(self)
