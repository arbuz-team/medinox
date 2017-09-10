from server.manage.switch.website.content.errors_handler import *
from server.ground.catalog.views import *
from server.ground.link.views import *


class Catalog_Switch(Website_Manager):

    @staticmethod
    def Catalog_Not_Found(request):
        return Errors_Handler.Code_404(request, '__ground__')

    @staticmethod
    def Switch_Form(request):

        if request.POST['_name_'] == 'copy_product':
            return Copy_Product(request, only_root=True).HTML

        if request.POST['_name_'] == 'copy_catalog':
            return Copy_Catalog(request, only_root=True).HTML

        if request.POST['_name_'] == 'copy_link':
            return Copy_Link(request, only_root=True).HTML

        if request.POST['_name_'] == 'move_product':
            return Move_Product(request, only_root=True).HTML

        if request.POST['_name_'] == 'move_catalog':
            return Move_Catalog(request, only_root=True).HTML

        if request.POST['_name_'] == 'move_link':
            return Move_Link(request, only_root=True).HTML

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

        if 'form' in request.POST.values():
            return Catalog_Switch.Switch_Form(request)

        # try:

        # change catalog and show content
        Catalog_Changer(request, catalog_path)
        return Catalog_Manager(request).HTML

        # catalog not found
        # except: return Catalog_Switch(request).HTML
