from server.manage.switch.forms.media import *


class Form_Order_Note(Abstract_File_Form):

    def Create_Fields(self):
        self.fields['note'] = forms.CharField(required=False)
        Abstract_File_Form.Create_Fields(self)

    def Set_Widgets(self):
        note_attr = self.Attr(Text(self, 169), field=Field.TEXTAREA)
        self.fields['note'].widget = forms.Textarea(attrs=note_attr)
        Abstract_File_Form.Set_Widgets(self)
