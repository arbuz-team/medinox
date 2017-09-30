from server.manage.switch.website import *
from server.ground.link.forms import *


class Move_Link(Website_Manager):

    def Manage_Form(self):

        self.context['form'] = Form_Link(self, post=True)
        if self.context['form'].is_valid():

            # get data
            language = self.request.session['translator_language']
            link = self.request.session['catalog_move_element']
            target = self.request.POST['target_en']\
                if language == 'EN' else self.request.POST['target_pl']

            # change data and move catalog
            link.parent = SQL.Get(Model_Catalog, pk=target)
            SQL.Save(data=link)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Move_Link(request, only_root=True).HTML
