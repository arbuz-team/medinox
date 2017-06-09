from server.manage.switch.forms import *
from server.content.catalog.models import *


class Form_Catalog(Abstract_Image_Form):

    def clean(self):

        name = self.data['name']
        parent = self.request.session['catalog_parent']
        children = Catalog.objects.filter(parent=parent)

        if children.filter(name=name):
            raise forms.ValidationError(Text(self.request, 155))

        return Abstract_Image_Form.clean(self)

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        Abstract_Image_Form.Create_Fields(self)
