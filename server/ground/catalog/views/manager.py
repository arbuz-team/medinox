from server.ground.product.views import *
from server.ground.catalog.forms import *


class Catalog_Manager(Website_Manager):

    def Manage_Content(self):

        # session data
        parent = self.request.session['catalog_parent']
        deleted = self.request.session['catalog_deleted_flag']
        language = self.request.session['translator_language']
        if deleted: deleted = None # show deleted and not deleted elements

        # database data
        catalogs = SQL.Filter(Model_Catalog,
            deleted=deleted, parent=parent, language=language)

        products = SQL.Filter(Product,
            deleted=deleted, parent=parent, language=language)

        # pages manager
        elements = list(catalogs) + list(products)
        number_element_on_page = self.request.session['catalog_number_on_page']
        selected_page = self.request.session['catalog_selected_page']

        pages_manager = Pages_Manager(elements,
              number_element_on_page, selected_page)

        self.context.update(pages_manager.Create_Pages())
        return self.Render_HTML('catalog/catalogs.html')

    def Manage_Form_New_Catalog(self):
        self.context['form'] = Form_Catalog(self, post=True)

        if self.context['form'].is_valid():
            name = self.context['form'].cleaned_data['name']

            catalog = Model_Catalog()
            catalog.name = name
            catalog.url_name = Path_Manager.To_URL(name)
            catalog.parent = self.request.session['catalog_parent']
            catalog.language = self.request.session['translator_language']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.context['form'].cleaned_data['image'])
            self.context['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Catalog(self):
        self.context['form'] = Form_Catalog(self, post=True)

        if self.context['form'].is_valid():
            name = self.context['form'].cleaned_data['name']

            catalog = self.request.session['catalog_editing']
            catalog.name = name
            catalog.url_name = Path_Manager.To_URL(name)
            catalog.parent = self.request.session['catalog_parent']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.context['form'].cleaned_data['image'])
            self.context['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['catalog_editing']:
            return self.Manage_Form_Edit_Catalog()

        return self.Manage_Form_New_Catalog()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete' :
            SQL.Delete(data=self.request.session['catalog_editing'])
            self.request.session['catalog_editing'] = None
            return HttpResponse()

        if self.request.POST['_name_'] == 'show_deleted':
            value = self.request.session['catalog_deleted_flag']
            self.request.session['catalog_deleted_flag'] = not value
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Catalog_Manager(request, only_root=True).HTML
