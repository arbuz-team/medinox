from server.manage.switch.website import *
from server.ground.link.forms import *


class Move_Link(Website_Manager):

    def Manage_Form(self):

        self.context['form'] = Form_Link(self, post=True)
        if self.context['form'].is_valid():

            # get data
            link = self.request.session['catalog_move_element']
            target = self.request.POST['target']

            # change data and move catalog
            link.parent = SQL.Get(Model_Catalog, pk=target)
            SQL.Save(data=link)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Link(request, only_root=True).HTML
