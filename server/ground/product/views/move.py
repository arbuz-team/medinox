from server.ground.product.views.copy import *


class Move_Product(Website_Manager):

    # Backend: test it
    def Manage_Form(self):

        self.context['form'] = Form_Copy(self, post=True)
        if self.context['form'].is_valid():

            # get data
            product = self.request.session['catalog_move_element']
            language = self.request.POST['language']
            target = self.request.POST['target']
            name = self.request.POST['name']

            # change data and move catalog
            product.name = name
            product.language = language
            product.parent = target
            SQL.Save(data=product)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Product(request, only_root=True).HTML
