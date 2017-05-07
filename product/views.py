from arbuz.views import *
from searcher.views import Search_Engine
from product.forms import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('product/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Details(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['product'] = Product.objects.get(pk=self.other_value)
        widgets = Widget.objects.filter(product=self.content['product'])
        self.content['widgets'] = [
            {
                'widget': widget,
                'values': Values.objects.filter(widget=widget)
            }
            for widget in widgets
        ]

        self.request.session['product_last_selected'] = self.content['product']
        return self.Render_HTML('product/details.html')

    @staticmethod
    def Details(request, pk):
        return Details(request, other_value=pk).HTML

    @staticmethod
    def Launch(request):
        pass



class Widget_Manager(Dynamic_Event_Manager):

    def Manage_Form_New_Widget(self):

        self.content['form'] = Form_Widget(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            widget = Widget(product=self.request.session['product_last_selected'])
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            widget.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Widget(self):

        self.content['form'] = Form_Widget(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            widget = self.request.session['product_editing_widget']
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            widget.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['product_editing_widget']:
            return self.Manage_Form_Edit_Widget()

        return self.Manage_Form_New_Widget()

    @staticmethod
    def Launch(request):
        return Widget_Manager(request, only_root=True).HTML



class Product_Manager(Dynamic_Event_Manager):

    def Manage_Form_New_Product(self):

        self.content['form'] = Form_Product(
            self.request, self.request.POST)

        if self.content['form'].is_valid():

            product = Product()
            product.name = self.content['form'].cleaned_data['name']
            product.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            product.price = self.content['form'].cleaned_data['price']
            product.parent = self.request.session['catalog_parent']
            product.save()

            product.Save_Image(self.content['form'].cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Product(self):

        self.content['form'] = Form_Product(
            self.request, self.request.POST)

        if self.content['form'].is_valid():

            product = self.request.session['product_editing']
            product.name = self.content['form'].cleaned_data['name']
            product.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            product.price = self.content['form'].cleaned_data['price']
            product.parent = self.request.session['catalog_parent']
            product.save()

            product.Save_Image(self.content['form'].cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['product_editing']:
            return self.Manage_Form_Edit_Product()

        return self.Manage_Form_New_Product()

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            self.request.session['product_editing'].delete()
            self.request.session['product_editing'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Product_Manager(request, only_root=True).HTML
