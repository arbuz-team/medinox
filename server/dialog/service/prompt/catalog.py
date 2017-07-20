from server.dialog.service.base import *


class Service_Catalog(Base_Service):

    def New(self):
        self.request.session['catalog_editing'] = Model_Catalog()

    def Edit(self):

        catalog = SQL.Get(Model_Catalog,
            pk=self.request.POST['value'])

        self.request.session['catalog_editing'] = catalog
        self.context['edit'] = {'url': '/catalog/manage/'}
        self.context['image'] = catalog.image
        self.initial = {'name': catalog.name}

    def Manage(self):

        if 'value' in self.request.POST:
            self.Edit()

        else: self.New()

        self.context['title'] = Text(self, 157)
        self.context['form'] = self.Prepare_Form(
            Form_Catalog, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'catalog', only_root=True)
