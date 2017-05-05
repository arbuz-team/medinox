from statement.views import *
from catalog.forms import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('catalog/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



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
    def Change(request, cat_1=None, cat_2=None, cat_3=None):
        return Change_Catalog(request, other_value=[cat_1, cat_2, cat_3]).HTML

    @staticmethod
    def Launch(request):
        pass



class New_Catalog(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Catalog(self.request)
        return self.Render_HTML('catalog/new.html', 'new_catalog')

    def Manage_Form_New_Catalog(self):

        self.content['form'] = Form_Catalog(
            self.request, self.request.POST)

        if self.content['form'].is_valid():

                catalog = Catalog()
                catalog.name = self.content['form'].cleaned_data['name']
                catalog.url_name = self.content['form'].cleaned_data['name']
                catalog.parent = self.request.session['catalog_parent']
                catalog.save()

                catalog.Save_Image(self.content['form'].cleaned_data['image'])

                self.content['form'] = None
                return self.Render_HTML('catalog/new.html')

        return self.Render_HTML('catalog/new.html', 'new_catalog')

    def Manage_Form(self):

        if 'new_catalog' in self.request.POST['__form__']:
            return self.Manage_Form_New_Catalog()

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return New_Catalog(request, other_value=other_value,
                           length_navigation=2, only_root=True).HTML

    @staticmethod
    def Launch(request):
        return New_Catalog(request, only_root=True).HTML



class Edit_Catalog(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):

        catalog = Catalog.objects.get(pk=self.other_value['pk'])
        self.content['form'] = Form_Catalog(self.request,
            initial={'name': catalog.name})

        self.content['image'] = catalog.image
        return self.Render_HTML('catalog/edit.html', 'edit_catalog')

    def Manage_Form_Edit_Catalog(self):

        self.content['form'] = Form_Catalog(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            catalog = Catalog.objects.get(pk=self.other_value['pk'])
            catalog.name = self.content['form'].cleaned_data['name']
            catalog.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            catalog.parent = self.request.session['catalog_parent']
            catalog.save()

            catalog.Save_Image(self.content['form'].cleaned_data['image'])

            self.content['form'] = None
            return self.Render_HTML('catalog/new.html')

        return self.Render_HTML('catalog/new.html', 'new_catalog')

    def Manage_Form(self):

        if 'edit_catalog' in self.request.POST['__form__']:
            return self.Manage_Form_Edit_Catalog()

    @staticmethod
    def Redirect(request, pk, url):
        other_value = {'redirect': url, 'pk': pk}
        return Edit_Catalog(request, other_value=other_value,
                            length_navigation=3, only_root=True).HTML

    @staticmethod
    def Edit(request, pk):
        return Edit_Catalog(request, other_value={'pk': pk},
                            only_root=True).HTML

    @staticmethod
    def Launch(request):
        pass