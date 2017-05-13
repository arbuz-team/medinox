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

        # get product
        self.content['product'] = Product.objects.get(pk=self.other_value)
        widgets = Widget.objects.filter(product=self.content['product'])

        # get descriptions
        self.content['descriptions'] = Description.objects\
            .filter(product=self.content['product'])

        # get widgets
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

        if '__form__' in request.POST:

            if request.POST['__form__'] == 'widget':
                return Widget_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'values':
                return Values_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'description':
                return Description_Manager(request, only_root=True).HTML

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

            return Dialog_Prompt(self.request, self.app_name, other_value=widget).HTML
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

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            self.request.session['product_editing_widget'].delete()
            self.request.session['product_editing_widget'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Widget_Manager(request, only_root=True).HTML



class Values_Manager(Dynamic_Event_Manager):

    def Manage_Form(self):

        self.content['form'] = Form_Values(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            widget = self.request.session['product_editing_widget']

            values = self.content['form'].save(commit=False)
            values.widget = widget
            values.save()

            return Dialog_Prompt(self.request, self.app_name, other_value=widget).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            Values.objects.get(pk=self.request.POST['value']).delete()
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Product_Manager(request, only_root=True).HTML



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



class Description_Manager(Dynamic_Event_Manager):

    def Manage_Form_Description(self):

        description = Form_Description(
            self.request, self.request.POST)

        if description.is_valid():

            if self.request.session['product_description']:
                product_desc = self.request.session['product_description']

            else: product_desc = Description()

            product_desc.header = description.cleaned_data['header']
            product_desc.paragraph = description.cleaned_data['paragraph']
            product_desc.save()

            product_desc.Save_Image(description.cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'description':
            return self.Manage_Form_Description()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Button(self):

        if self.request.POST['__button__'] == 'delete':
            Description.objects.get(pk=self.request.POST['value']).delete()

        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Launch(request):
        return Description_Manager(request, only_root=True).HTML

