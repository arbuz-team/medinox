from arbuz.forms import *
from catalog.models import *


class Form_Catalog(Abstract_Image_Form):

    def Create_Fields(self):
        self.fields['name'] = forms.CharField(max_length=100)
        Abstract_Image_Form.Create_Fields(self)
