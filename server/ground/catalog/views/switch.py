from server.ground.catalog.views.copy import Copy_Catalog
from server.ground.catalog.views.manager import *
from server.ground.catalog.views.changer import *
from server.ground.product.views import *


class Switch(Website_Manager):

    @staticmethod
    def Launch(request, catalog_path=''):

        # service of forms
        if '__form__' in request.POST:

            if request.POST['__form__'] == 'catalog':
                return Catalog_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'product':
                return Product_Manager(request, only_root=True).HTML

            if request.POST['__form__'] == 'copy':
                element_type = request.session['catalog_copy_type']

                if element_type == 'product':
                    return Copy_Product(request, only_root=True).HTML

                if element_type == 'catalog':
                    return Copy_Catalog(request, only_root=True).HTML

        # change catalog and show content
        Catalog_Changer(request, catalog_path)
        return Catalog_Manager(request).HTML
