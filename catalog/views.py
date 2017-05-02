from arbuz.views import *
from product.models import *


class Change_Catalog(Dynamic_Event_Manager):

    def Get_Last_Catalog(self):

        if not self.other_value[0]:
            return None

        cat_1 = Catalog.objects.get(
            url_name=self.other_value[0],
            parent=None
        )

        if not self.other_value[1]:
            return cat_1

        cat_2 = Catalog.objects.get(
            url_name=self.other_value[1],
            parent=cat_1
        )

        if not self.other_value[2]:
            return cat_2

        cat_3 = Catalog.objects.get(
            url_name=self.other_value[2],
            parent=cat_2
        )

        return cat_3

    def Manage_Content_Ground(self):

        catalog = self.Get_Last_Catalog()
        self.content['catalogs'] = Catalog.objects.filter(parent=catalog)
        self.content['products'] = Product.objects.filter(parent=catalog)

        print(self.content['catalogs'])
        return self.Render_HTML('main/products.html')

    @staticmethod
    def Change(request, cat_1=None, cat_2=None, cat_3=None):
        print(cat_1, cat_2, cat_3)
        return Change_Catalog(request, other_value=[cat_1, cat_2, cat_3]).HTML

    @staticmethod
    def Launch(request):
        pass