from server.manage.switch.forms.media import *


class Form_About_Content(Abstract_Image_Form):

    def Create_Fields(self):
        self.fields['header'] = forms.CharField(required=False)
        self.fields['paragraph'] = forms.CharField(required=False)
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        header_attr = {
            'placeholder': Text(self, 95),
            'class': 'test',
        }

        paragraph_attr = {
            'placeholder': Text(self, 96),
            'class': 'test',
        }

        self.fields['header'].widget = forms.TextInput(attrs=header_attr)
        self.fields['paragraph'].widget = forms.Textarea(attrs=paragraph_attr)
        Abstract_Image_Form.Set_Widgets(self)
