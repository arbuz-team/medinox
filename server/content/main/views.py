# -*- coding: utf-8 -*-
from server.service.sender.views import *
from server.page.searcher.views import *
from server.content.main.forms import *
from server.manage.switch.position import *


class Start(Website_Manager):

    def Manage_Content_Ground(self):
        self.Get_Post_Value('')
        self.content['recommended'] = SQL.Filter(Product,
            pk__in=SQL.All(Recommended_Product).values('product__pk'))

        return self.Render_HTML('main/start.html')

    @staticmethod
    def Launch(request):
        return Start(request).HTML



class About(Website_Manager):

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        path_manager = Path_Manager(self)

        self.content['paragraph_name'] = 'about'
        self.content['paragraph_url'] = path_manager.Get_Path(
            'main.about.manage', current_language=True)

        self.content['content'] = SQL.Filter(About_Content,
            language=language).order_by('position')

        return self.Render_HTML('main/about.html')

    def Manage_Form(self):
        form_about = Form_About_Content(self, post=True)

        if form_about.is_valid():

            about = self.request.session['main_about']
            position_manager = Position_Manager(self)
            position_manager.Insert_Element(About_Content, about)

            about.header = form_about.cleaned_data['header']
            about.paragraph = form_about.cleaned_data['paragraph']
            about.language = self.request.session['translator_language']
            SQL.Save(data=about)

            about.Save_Image(form_about.cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Button(self):
        position_manager = Position_Manager(self)
        position_manager.Button_Service(About_Content)
        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Launch(request):
        return About(request).HTML



class Contact(Website_Manager):

    def Create_Titles(self):

        self.content['form_detail'] = [
            {
                'title':    Text(self, 81),
                'hidden':   'url',
            },
            {
                'title':    Text(self, 82),
                'hidden':   'product',
            },
            {
                'title':    Text(self, 83),
                'hidden':   'url product',
            },
        ]

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        self.content['form'] = Form_Email_Contact(self)
        self.content['content'] = SQL.Filter(Contact_Content,
            language=language).order_by('position')

        self.Create_Titles()
        return self.Render_HTML('main/contact.html', 'email_contact')

    def Manage_Form(self):

        self.Create_Titles()
        self.content['form'] = Form_Email_Contact(self, post=True)

        if self.content['form'].is_valid():

            title = self.content['form'].cleaned_data['title']
            email = self.content['form'].cleaned_data['email']

            content = {
                'client':   self.content['form'].cleaned_data['client'],
                'question': self.content['form'].cleaned_data['message'],
                'product':  self.content['form'].cleaned_data['product'],
                'url':      self.content['form'].cleaned_data['url'],
            }

            Sender(self.request).Send_Contact_Question(title, content, email)

            return self.Render_HTML('main/contact.html', 'email_contact')
        return self.Render_HTML('main/contact.html', 'email_contact')

    @staticmethod
    def Launch(request):
        return Contact(request).HTML



from server.page.cart.views import *
from server.page.navigation.views import *
from server.page.searcher.views import *
from django.views.decorators.csrf import csrf_exempt

class Json_Example:

    @staticmethod
    @csrf_exempt
    def Launch(request):
        Check_Session(request)

        if '__content__' in request.POST:

            contents = request.POST['__content__'].split(' ')
            data = lambda x: {'status': x.status_code, 'html': x.content.decode('utf-8')}

            content = {
                'cart':         {'status': 200, 'html': 'Tu powinien być koszyk'},
                'navigation':   data(Navigation(request).Manage_Content_Navigation()),
                'header':       data(Navigation(request).Manage_Content_Header()),
                'searcher':     data(Searcher(request).Manage_Content_Searcher()),
                'ground':       data(Start(request).Manage_Content_Ground()),
            }

            json = {
                '__content__': {a: content[a] for a in contents}
            }

            return JsonResponse(json)

        return HttpResponse('Hue hue hue')
