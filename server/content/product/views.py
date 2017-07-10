from server.manage.switch.views import *
from server.page.searcher.views import Search_Engine
from server.content.product.forms import *
from server.manage.switch.module.position import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('product/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Details(Dynamic_Event_Manager):

    def Status_Buttons(self):

        user = self.request.session['user_user']
        product = self.content['product']

        if Favorite_Product.objects.filter(product=product, user=user):
            self.content['is_favorite'] = True

        if Recommended_Product.objects.filter(product=product):
            self.content['is_recommended'] = True

    def Descriptions(self):

        # get descriptions
        self.content['descriptions'] = Description.objects \
            .filter(product=self.content['product']).order_by('position')

        # variable for list of description
        # the same as edit in HTML
        path_manager = Path_Manager(self)
        self.content['paragraph_name'] = 'description'
        self.content['paragraph_url'] = path_manager.Get_Path(
            'product.description.manage', current_language=True)

    def Widgets(self):

        # get widgets
        widgets = Widget.objects.filter(
            product=self.content['product'])

        self.content['widgets'] = [
            {
                'widget': widget,
                'values': Values.objects.filter(widget=widget)
            }
            for widget in widgets
        ]

    def Manage_Content_Ground(self):

        # get product and save to session
        self.content['product'] = Product.objects.get(pk=self.other_value)
        self.request.session['product_product'] = self.content['product']
        self.request.session['product_last_selected'] = \
            self.content['product']

        self.Widgets()
        self.Descriptions()
        self.Status_Buttons()
        return self.Render_HTML('product/details.html')

    @staticmethod
    def Details(request, pk, name):

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
        self.content['form'] = Form_Widget(self, post=True)

        if self.content['form'].is_valid():
            widget = Widget(product=self.request.session['product_last_selected'])
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            widget.save()

            # other value get widget to edit
            return Dialog_Prompt(self.request, self.app_name, other_value=widget).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Widget(self):
        self.content['form'] = Form_Widget(self, post=True)

        if self.content['form'].is_valid():
            widget = self.request.session['product_widget']
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            widget.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['product_widget']:
            return self.Manage_Form_Edit_Widget()

        return self.Manage_Form_New_Widget()

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            self.request.session['product_widget'].delete()
            self.request.session['product_widget'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Widget_Manager(request, only_root=True).HTML



class Values_Manager(Dynamic_Event_Manager):

    def Manage_Form(self):
        self.content['form'] = Form_Values(self, post=True)

        if self.content['form'].is_valid():
            widget = self.request.session['product_widget']

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

    def Manage_Form_Product(self):
        self.content['form'] = Form_Product(self, post=True)

        if self.content['form'].is_valid():

            product = self.request.session['product_product']
            product.name = self.content['form'].cleaned_data['name']
            product.url_name = self.To_URL(self.content['form'].cleaned_data['name'])
            product.price = self.content['form'].cleaned_data['price']
            product.parent = self.request.session['catalog_parent']
            product.save()

            product.Save_Image(self.content['form'].cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'product':
            return self.Manage_Form_Product()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Button_Delete(self):
        self.request.session['product_product'].delete()
        self.request.session['product_product'] = None
        self.Clear_Session('searcher_result')
        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Recommended(self):
        action = self.Get_Post_Value('action')
        pk = self.request.POST['value']
        product = Product.objects.get(pk=pk)

        if action == 'delete':
            Recommended_Product.objects.get(
                product=product).delete()

        if action == 'append':
            Recommended_Product(product=product).save()

        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Favorite(self):
        action = self.Get_Post_Value('action')
        pk = self.request.POST['value']
        product = Product.objects.get(pk=pk)
        user = self.request.session['user_user']

        if action == 'delete':
            Favorite_Product.objects.get(
                product=product, user=user).delete()

        if action == 'append':
            Favorite_Product(product=product, user=user).save()

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



class Description_Manager(Dynamic_Event_Manager):

    def Manage_Form_Description(self):
        description = Form_Description(self, post=True)

        if description.is_valid():

            product_desc = self.request.session['product_description']
            position_manager = Position_Manager(self)
            position_manager.Insert_Element(Description, product_desc)

            product_desc.header = description.cleaned_data['header']
            product_desc.paragraph = description.cleaned_data['paragraph']
            product_desc.product = self.request.session['product_last_selected']
            product_desc.save()

            product_desc.Save_Image(description.cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'description':
            return self.Manage_Form_Description()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Button(self):
        position_manager = Position_Manager(self)
        position_manager.Button_Service(Description)
        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Launch(request):
        return Description_Manager(request, only_root=True).HTML

