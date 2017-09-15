from server.manage.switch.website.manager import *
from server.ground.product.forms import *
from server.ground.main.models import *
from server.manage.switch.position import *


class Home(Website_Manager):

    def Manage_Content(self):
        language = self.request.session['translator_language']
        path_manager = Path_Manager(self)

        self.context['paragraph_name'] = 'home'
        self.context['paragraph_url'] = path_manager.Get_Path(
            'main.home.manage', current_language=True)

        self.context['content'] = SQL.Filter(Model_Home_Content,
            language=language).order_by('position')

        return self.Render_HTML('main/start.html')

    def Manage_Form(self):
        form_home = Form_Description(self, post=True)

        if form_home.is_valid():

            home = self.request.session['main_home']
            position_manager = Position_Manager(self)
            position_manager.Insert_Element(Model_Home_Content, home)

            home.header = form_home.cleaned_data['header']
            home.paragraph = form_home.cleaned_data['paragraph']
            home.language = self.request.session['translator_language']
            SQL.Save(data=home)

            home.Save_Image(form_home.cleaned_data['image'])

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete_image':
            home = self.request.session['main_home']
            home.image = None
            SQL.Save(data=home)
            return HttpResponse()

        else:

            position_manager = Position_Manager(self)
            position_manager.Button_Service(Model_Home_Content)
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Home(request).HTML
