from server.ground.product.views import *
from server.ground.catalog.forms import *


class Catalog_Manager(Website_Manager):

    def Manage_Content_Ground(self):

        # session data
        parent = self.request.session['catalog_parent']
        language = self.request.session['translator_language']

        # database data
        catalogs = SQL.Filter(Model_Catalog, parent=parent, language=language)
        products = SQL.Filter(Product, parent=parent, language=language)

        # pages manager
        elements = list(catalogs) + list(products)
        number_element_on_page = self.request.session['catalog_number_on_page']
        selected_page = self.request.session['catalog_selected_page']

        pages_manager = Pages_Manager(elements,
              number_element_on_page, selected_page)

        self.content.update(pages_manager.Create_Pages())
        return self.Render_HTML('catalog/catalogs.html')

    def Manage_Form_New_Catalog(self):
        self.content['form'] = Form_Catalog(self, post=True)

        if self.content['form'].is_valid():
            name = self.content['form'].cleaned_data['name']

            catalog = Model_Catalog()
            catalog.name = name
            catalog.url_name = Path_Manager.To_URL(name)
            catalog.parent = self.request.session['catalog_parent']
            catalog.language = self.request.session['translator_language']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.content['form'].cleaned_data['image'])
            self.content['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Catalog(self):
        self.content['form'] = Form_Catalog(self, post=True)

        if self.content['form'].is_valid():
            name = self.content['form'].cleaned_data['name']

            catalog = self.request.session['catalog_editing']
            catalog.name = name
            catalog.url_name = Path_Manager.To_URL(name)
            catalog.parent = self.request.session['catalog_parent']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.content['form'].cleaned_data['image'])
            self.content['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['catalog_editing']:
            return self.Manage_Form_Edit_Catalog()

        return self.Manage_Form_New_Catalog()

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            SQL.Delete(data=self.request.session['catalog_editing'])

            self.request.session['catalog_editing'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Catalog_Manager(request, only_root=True).HTML
