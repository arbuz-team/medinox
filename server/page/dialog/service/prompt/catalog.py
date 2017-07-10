from server.page.dialog.service.base import *


class Service_Catalog(Base_Service):

    def New(self):
        self.request.session['catalog_editing'] = Catalog()

    def Edit(self):

        catalog = SQL.Get(Catalog,
            pk=self.request.POST['dialog_value'])

        self.request.session['catalog_editing'] = catalog
        self.content['edit'] = {'url': '/catalog/manage/'}
        self.content['image'] = catalog.image
        self.instance = {'name': catalog.name}

    def Manage(self):

        if 'dialog_value' in self.request.POST:
            self.Edit()

        else: self.New()

        self.content['title'] = Text(self, 157)
        self.content['form'] = self.Prepare_Form(
            Form_Catalog, initial=self.instance)

        return self.Render_Dialog(
            'prompt.html', 'catalog', only_root=True)
