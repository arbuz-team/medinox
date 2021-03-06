from server.manage.switch.website.content.errors_handler import *
from server.ground.catalog.views import *
from server.ground.link.views import *


class Catalog_Switch(Website_Manager):

    def Manage_Content(self):
        return Errors_Handler.Code_404(
            self.request, '__ground__')

    def Manage_Form_Restore(self):

        self.context['form'] = Form_Restore(self, post=True)
        if self.context['form'].is_valid():

            # get data
            name = self.context['form'].cleaned_data['restore_name']
            model = self.request.session['catalog_restore_type']
            pk = self.request.session['catalog_restore_pk']

            _object = SQL.Get(model, deleted=True, pk=pk)
            _object.name = name
            _object.deleted = False
            SQL.Save(data=_object)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

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

        if self.request.POST['_name_'] == 'restore':
            return self.Manage_Form_Restore()

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

        if 'form' in request.POST.values() or \
            'button' in request.POST.values():
            return Catalog_Switch(request).HTML

        try:

            # change catalog and show content
            Catalog_Changer(request, catalog_path)
            return Catalog_Manager(request).HTML

        # catalog not found
        except Catalog_Not_Found:
            return Catalog_Switch(request).HTML
