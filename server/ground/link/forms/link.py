from server.manage.switch.forms.media import *
from server.ground.link.models import *


class Form_Link(Abstract_Form):

    def clean(self):

        link = self.request.session['link_editing']

        # get data
        name = str(link)
        parent = SQL.Get(Model_Catalog, pk=self.data['target'])
        children = SQL.Filter(Model_Catalog, parent=parent)

        # check if catalog with the name exists
        if children.filter(name=name):
            raise forms.ValidationError(Text(self, 155))

        return Abstract_Form.clean(self)

