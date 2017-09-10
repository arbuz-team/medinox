from server.ground.product.views.copy import *


class Move_Catalog(Website_Manager):

    def Manage_Form(self):

        self.context['form'] = Form_Move(self, post=True)
        if self.context['form'].is_valid():

            # get data
            catalog = self.request.session['catalog_move_element']
            language = self.request.POST['language']
            target = self.request.POST['target']
            name = self.request.POST['name']

            # change data and move catalog
            catalog.name = name
            catalog.language = language
            catalog.parent = SQL.Get(Model_Catalog, pk=target)
            SQL.Save(data=catalog)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Catalog(request, only_root=True).HTML
