from server.statement.views import *
from server.product.views import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('catalog/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Catalog_Service(Dynamic_Event_Manager):

    @staticmethod
    def Service(request, cat_1=None, cat_2=None, cat_3=None):

        if '__form__' in request.POST:

            if request.POST['__form__'] == 'catalog':
                return Catalog_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'product':
                return Product_Manager(request, only_root=True).HTML

        return Change_Catalog(request, other_value=[cat_1, cat_2, cat_3]).HTML

    @staticmethod
    def Launch(request):
        pass



class Change_Catalog(Dynamic_Event_Manager):

    @staticmethod
    def Get_Catalog(url_name, parent):

        if url_name:

            cat = Catalog.objects.filter(
                url_name=url_name, parent=parent)

            if cat: return cat[0]
            else: raise Exception('Catalog not exists')

        return None

    def Get_Last_Catalog(self):

        if not self.other_value[0]:
            return None

        cat_1 = self.Get_Catalog(self.other_value[0], None)
        cat_2 = self.Get_Catalog(self.other_value[1], cat_1)
        cat_3 = self.Get_Catalog(self.other_value[2], cat_2)

        if cat_3:
            return cat_3

        if cat_2:
            return cat_2

        return cat_1

    def Manage_Content_Ground(self):

        try: catalog = self.Get_Last_Catalog()
        except: return Statement_404.Launch(self.request)

        self.request.session['catalog_parent'] = catalog
        self.content['catalogs'] = Catalog.objects.filter(parent=catalog)
        self.content['products'] = Product.objects.filter(parent=catalog)
        return self.Render_HTML('main/products.html')

    @staticmethod
    def Launch(request):
        pass



class Catalog_Manager(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        pass

    def Manage_Form_New_Catalog(self):

        self.content['form'] = Form_Catalog(
            self.request, self.request.POST)

        if self.content['form'].is_valid():

            catalog = Catalog()
            catalog.name = self.content['form'].cleaned_data['name']
            catalog.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            catalog.parent = self.request.session['catalog_parent']
            catalog.save()

            catalog.Save_Image(self.content['form'].cleaned_data['image'])
            self.content['form'] = None

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Catalog(self):

        self.content['form'] = Form_Catalog(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            catalog = self.request.session['catalog_editing']
            catalog.name = self.content['form'].cleaned_data['name']
            catalog.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            catalog.parent = self.request.session['catalog_parent']
            catalog.save()

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
            self.request.session['catalog_editing'].delete()
            self.request.session['catalog_editing'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Catalog_Manager(request, only_root=True).HTML
