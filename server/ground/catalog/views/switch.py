from server.manage.switch.website.content.errors_handler import *
from server.ground.catalog.views import *
from server.ground.link.views import *


class Catalog_Switch(Website_Manager):

    def Manage_Content(self):
        return Errors_Handler.Code_404(
            self.request, '__ground__')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'copy_product':
            return Copy_Product(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'copy_catalog':
            return Copy_Catalog(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'copy_link':
            return Copy_Link(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'move_product':
            return Move_Product(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'move_catalog':
            return Move_Catalog(self.request, only_root=True).HTML

        if self.request.POST['_name_'] == 'move_link':
            return Move_Link(self.request, only_root=True).HTML

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'change':
            return Catalog_Manager(self.request).HTML

    @staticmethod
    def Launch(request, catalog_path=''):

        if '__ground__' not in request.POST.keys() and \
           '__dialog__' not in request.POST.keys():
            return Catalog_Switch(request).HTML

        # service of forms
        if '_name_' in request.POST:

            if request.POST['_name_'] == 'catalog':
                return Catalog_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'product':
                return Product_Manager(request, only_root=True).HTML

            if request.POST['_name_'] == 'link':
                return Link_Manager(request, only_root=True).HTML

        if 'form' in request.POST.values():
            return Catalog_Switch(request, autostart=False)\
                .Manage_Form()

        if 'button' in request.POST.values():
            return Catalog_Switch(request, autostart=False)\
                .Manage_Button()

        try:

            # change catalog and show content
            Catalog_Changer(request, catalog_path)
            return Catalog_Manager(request).HTML

        # catalog not found
        except Catalog_Not_Found:
            return Catalog_Switch(request).HTML
