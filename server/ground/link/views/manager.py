from server.manage.switch.website import *
from server.ground.link.forms import *


class Link_Manager(Website_Manager):

    def Manage_Form_New_Link(self):
        form = Form_Link(self, post=True)

        if form.is_valid():

            # get data
            link = self.request.session['link_editing']
            target = self.request.POST['target']
            link.parent = SQL.Get(Model_Catalog, pk=target)
            link.language = self.request.session['translator_language']
            SQL.Save(data=link)

            self.context['form'] = None

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'link':
            return self.Manage_Form_New_Link()

    def Manage_Button_Delete(self):

        link = self.request.session['link_editing']
        self.request.session['link_editing'] = None

        SQL.Delete(data=link, force=True)
        self.Clear_Session('searcher_result')
        return HttpResponse()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete':
            self.Manage_Button_Delete()

    @staticmethod
    def Launch(request):
        return Link_Manager(request, only_root=True).HTML
