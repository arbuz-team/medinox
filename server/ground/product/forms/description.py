from server.manage.switch.forms.media import *
from server.ground.product.models import *


class Form_Description(Abstract_Image_Form):

    def Create_Fields(self):
        self.fields['header'] = forms.CharField(required=False)
        self.fields['paragraph'] = forms.CharField(required=False)
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        header_attr = self.Attr(Text(self, 95), classes='test')
        paragraph_attr = self.Attr(Text(self, 96), classes='test', field=Field.TEXTAREA)

        self.fields['header'].widget = forms.TextInput(attrs=header_attr)
        self.fields['paragraph'].widget = forms.Textarea(attrs=paragraph_attr)
        Abstract_Image_Form.Set_Widgets(self)
