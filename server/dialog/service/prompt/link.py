from server.dialog.service.tree import *
from server.ground.link.models import *


class Service_Link(Catalog_Tree):

    def New(self):
        type = self.dialog.Get_Post_Other('type')
        pk = self.request.POST['value']

        if type == 'catalog':
            catalog = SQL.Get(Model_Catalog, pk=pk)
            self.request.session['link_editing'] = \
                Model_Catalog_Link(catalog=catalog)

        if type == 'product':
            product = SQL.Get(Model_Product, pk=pk)
            self.request.session['link_editing'] = \
                Model_Product_Link(catalog=product)

    def Manage(self):

        self.Create_Catalog_Tree()
        self.New()

        self.context['title'] = Text(self, 187)
        return self.Render_Dialog(
            'link.html', only_root=True)
