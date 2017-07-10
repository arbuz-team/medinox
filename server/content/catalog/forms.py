from server.manage.switch.forms.media import *
from server.content.catalog.models import *


class Form_Catalog(Abstract_Image_Form):

    def clean(self):

        name = self.data['name']
        parent = self.request.session['catalog_parent']
        children = SQL.Filter(Catalog, parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self, 155))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        Abstract_Image_Form.Create_Fields(self)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 164), autofocus=True)
        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        Abstract_Image_Form.Set_Widgets(self)
