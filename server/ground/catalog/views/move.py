from server.ground.product.views.copy import *


class Move_Catalog(Website_Manager):

    def Manage_Form(self):

        self.content['form'] = Form_Copy(self, post=True)
        if self.content['form'].is_valid():

            # get data
            catalog = self.request.session['catalog_move_element']
            language = self.request.POST['language']
            target = self.request.POST['target']
            name = self.request.POST['name']

            # change data and move catalog
            catalog.name = name
            catalog.language = language
            catalog.parent = target
            SQL.Save(data=catalog)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Catalog(request, only_root=True).HTML
