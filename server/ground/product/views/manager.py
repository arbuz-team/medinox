from server.manage.switch.website.manager import *
from server.ground.product.forms import *
from server.manage.switch.position import *


class Product_Manager(Website_Manager):

    def Manage_Form_Product(self):
        self.context['form'] = Form_Product(self, post=True)

        if self.context['form'].is_valid():
            cleaned_data = self.context['form'].cleaned_data

            product = self.request.session['product_product']
            product.name = cleaned_data['name']
            product.url_name = Path_Manager.To_URL(cleaned_data['name'])
            product.price = cleaned_data['price']
            product.parent = self.request.session['catalog_parent']
            product.language = self.request.session['translator_language']
            SQL.Save(data=product)

            product.Save_Image(cleaned_data['image'])

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'product':
            return self.Manage_Form_Product()

        return Website_Manager.Manage_Form(self)

    def Manage_Button_Delete(self):
        self.request.session['product_product'].delete()
        self.request.session['product_product'] = None
        self.Clear_Session('searcher_result')
        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Recommended(self):
        action = self.Get_Post_Other('action')
        pk = self.request.POST['value']
        product = SQL.Get(Product, pk=pk)

        if action == 'delete':
            SQL.Get(Recommended_Product,
                product=product).delete()

        if action == 'append':
            SQL.Save(Recommended_Product, product=product)

        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Favorite(self):
        action = self.Get_Post_Other('action')
        pk = self.request.POST['value']
        product = SQL.Get(Product, pk=pk)
        user = self.request.session['user_user']

        if action == 'delete':
            SQL.Get(Favorite_Product,
                product=product, user=user).delete()

        if action == 'append':
            SQL.Save(Favorite_Product, product=product, user=user)

        return JsonResponse({'__button__': 'true'})

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            return self.Manage_Button_Delete()

        if 'recommended' in self.request.POST['__button__']:
            return self.Manage_Button_Recommended()

        if 'favorite' in self.request.POST['__button__']:
            return self.Manage_Button_Favorite()

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Product_Manager(request, only_root=True).HTML
