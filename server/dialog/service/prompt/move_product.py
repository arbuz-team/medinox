from server.service.payment.forms import *
from server.ground.catalog.forms import *
from server.dialog.service.tree import *


class Service_Move_Product(Catalog_Tree):

    def Get_Element(self, model):

        if 'value' in self.request.POST:
            element_pk = self.request.POST['value']

            # get element
            return SQL.Get(model, pk=element_pk)
        return self.request.session['catalog_move_element']

    def Move_Product(self):

        # get post data
        element = self.Get_Element(Model_Product)

        # initial data
        self.request.session['catalog_move_element'] = element
        language = self.request.session['translator_language']

        self.initial = {
            'language': language,
            'name': element.name
        }

        self.context['form'] = self.Prepare_Form(
            Form_Move, initial=self.initial)

    def Not_Valid(self):
        self.context['title'] = Text(self, 179)
        self.Create_Catalog_Tree()
        return self.Render_Dialog(
            'move.html', 'move_product', only_root=True)

    def Manage(self):

        self.Move_Product()

        # code for each widget
        self.context['title'] = Text(self, 179)
        self.Create_Catalog_Tree()

        return self.Render_Dialog(
            'move.html', 'move_product', only_root=True)
