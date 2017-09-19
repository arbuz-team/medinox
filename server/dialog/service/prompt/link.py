from server.dialog.service.tree import *
from server.ground.link.models import *


class Service_Link(Catalog_Tree):

    def New(self):

        type = self.dialog.Get_Post_Other('type')
        pk = self.request.POST['value']
        obiekt = None

        if type == 'catalog':
            obiekt = SQL.Get(Model_Catalog, pk=pk)
            self.request.session['link_editing'] = \
                Model_Catalog_Link(catalog=obiekt)

        if type == 'product':
            obiekt = SQL.Get(Model_Product, pk=pk)
            self.request.session['link_editing'] = \
                Model_Product_Link(product=obiekt)

        return obiekt

    def Not_Valid(self):
        self.Create_Catalog_Tree()
        return self.Render_Dialog(
            'link.html', 'link', only_root=True)

    def Manage(self):

        self.Create_Catalog_Tree()
        self.context['obiekt'] = self.New()

        return self.Render_Dialog(
            'link.html', 'link', only_root=True)
