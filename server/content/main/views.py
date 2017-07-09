# -*- coding: utf-8 -*-
from server.service.sender.views import *
from server.page.searcher.views import *
from server.content.main.forms import *
from server.manage.switch.module.position import *


class Start(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.Get_Post_Value('')
        self.content['recommended'] = Product.objects.filter(
            pk__in=Recommended_Product.objects.all().values('product__pk'))

        return self.Render_HTML('main/start.html')

    @staticmethod
    def Launch(request):
        return Start(request).HTML



class Products(Dynamic_Event_Manager): # TODO(backend): generate pages move to abstract

    def Get_Current_Page(self, number_product_on_page):

        page = self.request.session['main_page']
        start = (page-1) * number_product_on_page
        end = page * number_product_on_page

        products = self.request.session['searcher_result']
        return products[start:end]

    @staticmethod
    def Get_List_Pages(number_of_pages):
        return list(range(1, number_of_pages + 1))

    def Get_Split_Pages(self, number_of_pages):
        page = self.request.session['main_page']

        if number_of_pages < 8:  # 1 2 3 4 5 6 7
            return [list(range(1, number_of_pages + 1))]

        if page < 5:  # 1 2 3 4 5 … 9
            return [list(range(1, 6)), [number_of_pages]]

        if page > number_of_pages - 4:  # 1 … 5 6 7 8 9
            return [[1], list(range(number_of_pages - 4, number_of_pages + 1))]

        # 1 … 3 4 5 6 7 … 9
        return [[1], list(range(page - 2, page + 3)), [number_of_pages]]

    def Manage_Content_Ground(self):

        products = self.request.session['searcher_result']
        number_product_on_page = self.request.session['main_number_product_on_page']
        number_of_pages = int(len(products) / number_product_on_page)
        if len(products) % number_product_on_page:
            number_of_pages += 1

        self.content['products'] = self.Get_Current_Page(number_product_on_page)
        self.content['number_of_pages'] = number_of_pages
        self.content['list_pages'] = self.Get_List_Pages(number_of_pages)
        self.content['split_pages'] = self.Get_Split_Pages(number_of_pages)
        self.content['next_page'] = self.request.session['main_page'] + 1
        self.content['prev_page'] = self.request.session['main_page'] - 1

        return self.Render_HTML('main/products.html')

    def Manage_Button(self):

        self.request.session['main_page'] = \
            int(self.request.POST['value'])

        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Launch(request):
        return Products(request).HTML



class About(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        path_manager = Path_Manager(self)

        self.content['paragraph_name'] = 'about'
        self.content['paragraph_url'] = path_manager.Get_Path(
            'main.about.manage', current_language=True)

        self.content['content'] = About_Content.objects.filter(
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
            about.save()

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



class Contact(Dynamic_Event_Manager):

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
        self.content['content'] = Contact_Content.objects.filter(
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
