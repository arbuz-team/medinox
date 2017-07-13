from server.content.statement.views import *
from server.content.product.views import *
from server.content.catalog.forms import *


class Panel_App(Website_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('catalog/start.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request).HTML



class Switch(Website_Manager):

    @staticmethod
    def Launch(request, catalog_path=''):

        # service of forms
        if '__form__' in request.POST:

            if request.POST['__form__'] == 'catalog':
                return Catalog_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'product':
                return Product_Manager(request, only_root=True).HTML

        # change catalog and show content
        Catalog_Changer(request, catalog_path)
        return Catalog_Manager(request).HTML



class Catalog_Changer(Website_Manager):

    @staticmethod
    def Get_Catalog(url_name, parent):

        if url_name:

            cat = SQL.Filter(Catalog,
                url_name=url_name, parent=parent)

            if cat: return cat[0]
            else: raise Exception('Catalog not exists')

        return None

    def Get_Selected_Catalog(self):

        catalogs = self.catalog_path.split('/')[:-1]
        parent = None
        selected = None

        if not catalogs:
            return None

        for catalog in catalogs:
            selected = self.Get_Catalog(catalog, parent)
            parent = selected

        return selected

    def Change_Catalog(self):

        try: catalog = self.Get_Selected_Catalog()
        except: return Statement_404.Launch(self.request)

        self.request.session['catalog_parent'] = catalog
        self.request.session['catalog_path'] = self.catalog_path

    def __init__(self, request, catalog_path):
        Website_Manager.__init__(self, request)

        self.catalog_path = catalog_path
        self.Change_Catalog()



class Catalog_Manager(Website_Manager):

    def Manage_Content_Ground(self):
        catalog = self.request.session['catalog_parent']
        self.content['catalogs'] = SQL.Filter(Catalog, parent=catalog)
        self.content['products'] = SQL.Filter(Product, parent=catalog)
        return self.Render_HTML('catalog/catalogs.html')

    def Manage_Form_New_Catalog(self):
        self.content['form'] = Form_Catalog(self, post=True)

        if self.content['form'].is_valid():

            catalog = Catalog()
            catalog.name = self.content['form'].cleaned_data['name']
            catalog.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            catalog.parent = self.request.session['catalog_parent']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.content['form'].cleaned_data['image'])
            self.content['form'] = None

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Catalog(self):
        self.content['form'] = Form_Catalog(self, post=True)

        if self.content['form'].is_valid():
            catalog = self.request.session['catalog_editing']
            catalog.name = self.content['form'].cleaned_data['name']
            catalog.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            catalog.parent = self.request.session['catalog_parent']
            SQL.Save(data=catalog)

            catalog.Save_Image(self.content['form'].cleaned_data['image'])
            self.content['form'] = None

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

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
