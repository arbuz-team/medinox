from server.dialog.service.tree import *
from server.ground.link.forms import *


class Service_Copy_Link(Catalog_Tree):

    def Get_Element(self, model):

        if 'value' in self.request.POST:
            element_pk = self.request.POST['value']

            # get element
            return SQL.Get(model, pk=element_pk)
        return self.request.session['catalog_copy_element']

    def Copy_Link(self):

        # get post data
        model_type = self.dialog.Get_Post_Other('model')
        element = None

        if model_type == 'product_link':
            element = self.Get_Element(Model_Product_Link)

        if model_type == 'catalog_link':
            element = self.Get_Element(Model_Catalog_Link)

        # initial data
        self.request.session['catalog_copy_element'] = element

    def Not_Valid(self):
        pass

    def Manage(self):

        self.Copy_Link()

        # code for each widget
        self.context['title'] = Text(self, 177)
        self.Create_Catalog_Tree()

        return self.Render_Dialog(
            'copy.html', 'copy_link', only_root=True)
