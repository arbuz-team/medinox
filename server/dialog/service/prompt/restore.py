from server.dialog.service.base import *
from server.ground.catalog.forms import *
from server.ground.product.forms import *


class Service_Restore(Base_Service):

    def Not_Valid(self):
        self.context['title'] = Text(self, 276)
        return self.Render_Dialog(
            'prompt.html', 'restore', only_root=True)

    def Manage(self):

        pk = self.request.POST['value']
        model_type = self.dialog.Get_Post_Other('model_type')
        model = None

        if model_type == 'catalog': model = Model_Catalog
        if model_type == 'product': model = Model_Product

        self.request.session['catalog_restore_pk'] = pk
        self.request.session['catalog_restore_type'] = model

        name = SQL.Get(model, deleted=True, pk=pk).name
        name = name.rsplit(':', 1)[0]

        self.context['title'] = Text(self, 276)
        self.context['form'] = self.Prepare_Form(
            Form_Restore, initial={'restore_name': name})

        return self.Render_Dialog(
            'prompt.html', 'restore', only_root=True)
