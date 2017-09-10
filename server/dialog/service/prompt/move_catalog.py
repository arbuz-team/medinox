from server.dialog.service.tree import *
from server.service.payment.forms import *
from server.ground.catalog.forms import *


class Service_Move_Catalog(Catalog_Tree):

    def Get_Element(self, model):

        if 'value' in self.request.POST:
            element_pk = self.request.POST['value']

            # get element
            return SQL.Get(model, pk=element_pk)
        return self.request.session['catalog_move_element']

    def Move_Catalog(self):

        # get post data
        element = self.Get_Element(Model_Catalog)

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
        pass

    def Manage(self):

        self.Move_Catalog()

        # code for each widget
        self.context['title'] = Text(self, 179)
        self.Create_Catalog_Tree()

        return self.Render_Dialog(
            'move.html', 'move_catalog', only_root=True)
