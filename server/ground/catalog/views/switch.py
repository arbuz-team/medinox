from server.manage.switch.website.content.errors_handler import *
from server.ground.catalog.views.copy import Copy_Catalog
from server.ground.catalog.views.manager import *
from server.ground.catalog.views.changer import *
from server.ground.product.views import *
from server.ground.link.views import *


class Catalog_Switch(Website_Manager):

    def Manage_Content(self):
        return Errors_Handler.Code_404(self.request, '__ground__')

    @staticmethod
    def Launch(request, catalog_path=''):

        # service of forms
        if '_name_' in request.POST:

            if request.POST['_name_'] == 'catalog':
                return Catalog_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'product':
                return Product_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'link':
                return Link_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'copy':
                element_type = request.session['catalog_copy_type']

                if element_type == 'product':
                    return Copy_Product(request, only_root=True).HTML

                if element_type == 'catalog':
                    return Copy_Catalog(request, only_root=True).HTML

                if element_type == 'link':
                    return Copy_Link(request, only_root=True).HTML

        try:

            # change catalog and show content
            Catalog_Changer(request, catalog_path)
            return Catalog_Manager(request).HTML

        # catalog not found
        except: return Catalog_Switch(request).HTML
