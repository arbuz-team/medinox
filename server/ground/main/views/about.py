from server.manage.switch.website import *
from server.ground.product.forms import *
from server.ground.main.models import *
from server.manage.switch.position import *


class About(Website_Manager):

    def Manage_Content(self):
        language = self.request.session['translator_language']
        path_manager = Path_Manager(self)

        self.context['paragraph_name'] = 'about'
        self.context['paragraph_url'] = path_manager.Get_Path(
            'main.about.manage', current_language=True)

        self.context['content'] = SQL.Filter(Model_About_Content,
            language=language).order_by('position')

        return self.Render_HTML('main/about.html')

    def Manage_Form(self):
        form_about = Form_Description(self, post=True)

        if form_about.is_valid():

            about = self.request.session['main_about']
            position_manager = Position_Manager(self)
            position_manager.Insert_Element(Model_About_Content, about)

            about.header = form_about.cleaned_data['header']
            about.paragraph = form_about.cleaned_data['paragraph']
            about.language = self.request.session['translator_language']
            SQL.Save(data=about)

            about.Save_Image(form_about.cleaned_data['image'])

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Button(self):
        position_manager = Position_Manager(self)
        position_manager.Button_Service(Model_About_Content)
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return About(request).HTML
