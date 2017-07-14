from server.content.catalog.views.manager import *
from server.content.catalog.views.changer import *
from server.content.product.views import *


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
