from server.dialog.service.tree import *
from server.service.payment.forms import *
from server.ground.catalog.forms import *


class Service_Move(Catalog_Tree):

    def Get_Element(self):

        if 'value' in self.request.POST:
            element_type = self.dialog.Get_Post_Other('type')
            element_pk = self.request.POST['value']

            # get element
            if element_type == 'product':
                return SQL.Get(Model_Product, pk=element_pk)

            if element_type == 'catalog':
                return SQL.Get(Model_Catalog, pk=element_pk)

        return self.request.session['catalog_move_element']

    def New(self):

        # get post data
        element_type = self.dialog.Get_Post_Other('type')
        element = self.Get_Element()

        # initial data
        self.request.session['catalog_move_element'] = element
        self.request.session['catalog_move_type'] = element_type
        language = self.request.session['translator_language']

        self.initial = {
            'language': language,
            'name': element.name
        }

    def Manage(self):

        self.Create_Catalog_Tree()
        self.New()

        # code for each widget
        self.context['title'] = Text(self, 179)
        self.context['form'] = self.Prepare_Form(
            Form_Move, initial=self.initial)

        return self.Render_Dialog(
            'move.html', 'move', only_root=True)
