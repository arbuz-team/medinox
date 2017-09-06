from .widget import *
from .values import *
from .description import *


class Details(Website_Manager):

    def Status_Buttons(self):

        user = self.request.session['user_user']
        product = self.context['product']

        if SQL.Filter(Model_Favorite_Product, product=product, user=user):
            self.context['is_favorite'] = True

        if SQL.Filter(Model_Recommended_Product, product=product):
            self.context['is_recommended'] = True

    def Descriptions(self):

        # get descriptions
        self.context['descriptions'] = SQL.Filter(Model_Description,
              product=self.context['product']).order_by('position')

        # variable for list of description
        # the same as edit in HTML
        path_manager = Path_Manager(self)
        self.context['paragraph_name'] = 'description'
        self.context['paragraph_url'] = path_manager.Get_Path(
            'product.description.manage', current_language=True)

    def Widgets(self):

        # get widgets
        widgets = SQL.Filter(Model_Widget,
            product=self.context['product'])

        self.context['widgets'] = [
            {
                'widget': widget,
                'values': SQL.Filter(Model_Values, widget=widget)
            }
            for widget in widgets
        ]

    def Manage_Content(self):

        # get product and save to session
        self.context['product'] = SQL.Get(Model_Product, pk=self.other_value)
        self.request.session['product_product'] = self.context['product']
        self.request.session['product_last_selected'] = \
            self.context['product']

        self.Widgets()
        self.Descriptions()
        self.Status_Buttons()
        return self.Render_HTML('product/details.html')

    @staticmethod
    def Launch(request, pk, name):

        if '_name_' in request.POST:

            if request.POST['_name_'] == 'widget':
                return Widget_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'values':
                return Values_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'description':
                return Description_Manager(request, only_root=True).HTML

        return Details(request, other_value=pk).HTML
