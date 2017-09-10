from server.manage.switch.website.content.errors_handler import *
from server.ground.catalog.views import *
from server.ground.link.views import *


class Catalog_Switch(Website_Manager):

    def Manage_Content(self):
        return Errors_Handler.Code_404(self.request, '__ground__')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'copy':
            element_type = self.request.session['catalog_copy_type']

            if element_type == 'product':
                return Copy_Product(self.request, only_root=True).HTML

            if element_type == 'catalog':
                return Copy_Catalog(self.request, only_root=True).HTML

            if element_type == 'link':
                return Copy_Link(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'move':
            element_type = self.request.session['catalog_move_type']

            if element_type == 'product':
                return Move_Product(self.request, only_root=True).HTML

            if element_type == 'catalog':
                return Move_Catalog(self.request, only_root=True).HTML

            if element_type == 'link':
                return Move_Link(self.request, only_root=True).HTML

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

        try:

            # change catalog and show content
            Catalog_Changer(request, catalog_path)
            return Catalog_Manager(request).HTML

        # catalog not found
        except: return Catalog_Switch(request).HTML
