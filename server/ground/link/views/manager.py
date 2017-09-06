from server.manage.switch.website import *
from server.ground.link.models import *


class Link_Manager(Website_Manager):

    def Manage_Content(self):
        return HttpResponse()

    def Manage_Button_Delete(self):

        catalog = self.request.session['product_editing']
        catalog.name += ':' + self.Generate_Random_Chars(
            20, punctuation=False)

        SQL.Delete(data=catalog)
        self.request.session['product_editing'] = None
        self.Clear_Session('searcher_result')
        return HttpResponse()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete':
            self.Manage_Button_Delete()

    @staticmethod
    def Launch(request):
        return Link_Manager(request, only_root=True).HTML
