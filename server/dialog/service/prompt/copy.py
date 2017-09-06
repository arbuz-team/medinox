from server.dialog.service.base import *
from server.ground.catalog.forms.operation import *


class Service_Copy(Base_Service):

    def Get_Element(self):

        if 'value' in self.request.POST:
            element_type = self.dialog.Get_Post_Other('type')
            element_pk = self.request.POST['value']

            # get element
            if element_type == 'product':
                return SQL.Get(Model_Product, pk=element_pk)

            if element_type == 'catalog':
                return SQL.Get(Model_Catalog, pk=element_pk)

        return self.request.session['catalog_copy_element']

    def New(self):

        # get post data
        element_type = self.dialog.Get_Post_Other('type')
        element = self.Get_Element()

        # initial data
        self.request.session['catalog_copy_element'] = element
        self.request.session['catalog_copy_type'] = element_type
        language = self.request.session['translator_language']

        self.initial = {
            'language': language,
            'name': element.name + Text(self, 178)
        }

    def Manage(self):

        self.New()

        # code for each widget
        self.context['title'] = Text(self, 177)
        self.context['form'] = self.Prepare_Form(
            Form_Copy, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'copy', only_root=True)
