from server.manage.switch.forms.media import *
from server.ground.link.models import *


class Form_Link(Abstract_Form):

    def clean(self):

        link = self.request.session['link_editing']
        language = self.request.session['translator_language']
        target_name = 'target_' + language.lower()

        if target_name not in self.data:
            raise forms.ValidationError(Text(self, 189))

        # get data
        name = str(link)
        parent = SQL.Get(Model_Catalog, pk=self.data[target_name])
        children = SQL.Filter(Model_Catalog, parent=parent)

        # check if catalog with the name exists
        if children.filter(name=name):
            raise forms.ValidationError(Text(self, 155))

        return Abstract_Form.clean(self)

