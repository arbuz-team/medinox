from server.ground.product.views import *
from server.ground.link.views import *
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

        products = SQL.Filter(Model_Product,
            deleted=deleted, parent=parent, language=language)

        link_product = SQL.Filter(Model_Product_Link,
            deleted=deleted, parent=parent, language=language)

        link_catalog = SQL.Filter(Model_Catalog_Link,
            deleted=deleted, parent=parent, language=language)

        # pages manager
        elements = list(catalogs) + list(products) + list(link_product) + list(link_catalog)
        number_element_on_page = self.request.session['catalog_number_on_page']
        selected_page = self.request.session['catalog_selected_page']

        pages_manager = Pages_Manager(elements,
              number_element_on_page, selected_page)

        self.context.update(pages_manager.Create_Pages())
        return self.Render_HTML('catalog/catalogs.html')

    @staticmethod
    def Create_URL_For_Catalog(catalog):

        name = Path_Manager.To_URL(catalog.name)
        path = [name]
        parent = catalog.parent

        # find all parents
        while True:

            # root directory
            if parent.name == '/': break

            name = Path_Manager.To_URL(parent.name)
            path.append(name)

            # get next parent if exist
            if not parent.parent: break
            else: parent = parent.parent

        path.reverse()
        return '/'.join(path) + '/'

    def Manage_Form_Catalog(self):
        self.context['form'] = Form_Catalog(self, post=True)

        if self.context['form'].is_valid():

            name = self.context['form'].cleaned_data['name']
            catalog = self.request.session['catalog_editing']

            catalog.name = name
            catalog.parent = self.request.session['catalog_parent']
            catalog.language = self.request.session['translator_language']
            SQL.Save(data=catalog)

            catalog.url_name = self.Create_URL_For_Catalog(catalog)
            catalog.Save_Image(self.context['form'].cleaned_data['image'])
            SQL.Save(data=catalog)

            self.context['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'catalog':
            return self.Manage_Form_Catalog()

    def Manage_Button_Delete(self):

        if 'value' in self.request.POST:
            pk = self.request.POST['value']
            catalog = SQL.Get(Model_Catalog, pk=pk)

        else: catalog = self.request.session['product_editing']
        catalog.name += ':' + self.Generate_Random_Chars(
            20, punctuation=False)

        SQL.Delete(data=catalog, force=False)

        self.request.session['catalog_editing'] = None
        return HttpResponse()

    def Manage_Button_Delete_Image(self):

        pk = self.request.POST['value']
        catalog = SQL.Get(Model_Catalog, pk=pk)
        catalog.image = None
        SQL.Save(data=catalog)
        return HttpResponse()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete':
            return self.Manage_Button_Delete()

        if self.request.POST['_name_'] == 'delete_image':
            return self.Manage_Button_Delete_Image()

        if self.request.POST['_name_'] == 'change':
            self.request.session['catalog_selected_page'] = \
                int(self.request.POST['value'])

            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Catalog_Manager(request, only_root=True).HTML
