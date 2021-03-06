from server.ground.product.views.copy import *


class Move_Product(Website_Manager):

    def Manage_Form(self):

        self.context['form'] = Form_Move(self, post=True)
        if self.context['form'].is_valid():

            # get data
            product = self.request.session['catalog_move_element']
            language = self.request.POST['language']
            name = self.request.POST['name']
            target = self.request.POST['target_en']\
                if language == 'EN' else self.request.POST['target_pl']

            # change data and move catalog
            product.name = name
            product.language = language
            product.parent = SQL.Get(Model_Catalog, pk=target)
            SQL.Save(data=product)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Product(request, only_root=True).HTML
