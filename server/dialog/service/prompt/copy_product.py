from server.dialog.service.tree import *
from server.ground.catalog.forms import *
from server.ground.link.forms import *


class Service_Copy_Product(Catalog_Tree):

    def Get_Element(self, model):

        if 'value' in self.request.POST:
            element_pk = self.request.POST['value']

            # get element
            return SQL.Get(model, pk=element_pk)
        return self.request.session['catalog_copy_element']

    def Copy_Product(self):

        # get post data
        element = self.Get_Element(Model_Product)

        # initial data
        self.request.session['catalog_copy_element'] = element
        language = self.request.session['translator_language']

        self.initial = {
            'language': language,
            'name': element.name + Text(self, 178)
        }

        self.context['form'] = self.Prepare_Form(
            Form_Copy, initial=self.initial)

    def Not_Valid(self):
        pass

    def Manage(self):

        self.Copy_Product()

        # code for each widget
        self.context['title'] = Text(self, 177)
        self.Create_Catalog_Tree()

        return self.Render_Dialog(
            'copy.html', 'copy_product', only_root=True)
