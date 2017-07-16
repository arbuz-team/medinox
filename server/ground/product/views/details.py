from .widget import *
from .values import *
from .description import *


class Details(Website_Manager):

    def Status_Buttons(self):

        user = self.request.session['user_user']
        product = self.content['product']

        if SQL.Filter(Favorite_Product, product=product, user=user):
            self.content['is_favorite'] = True

        if SQL.Filter(Recommended_Product, product=product):
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
        widgets = SQL.Filter(Widget,
            product=self.content['product'])

        self.content['widgets'] = [
            {
                'widget': widget,
                'values': SQL.Filter(Values, widget=widget)
            }
            for widget in widgets
        ]

    def Manage_Content_Ground(self):

        # get product and save to session
        self.content['product'] = SQL.Get(Product, pk=self.other_value)
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
