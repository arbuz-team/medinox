from .block import *


class Direct_Part_Manager(Base):

    def Manage(self, name):
        block = self.blocks[name]

        # parts of pages
        if self.request.POST[name] == 'content':
            return block.Manage_Content()

        # manage forms
        if self.request.POST[name] == 'form':
            return block.Manage_Form()

        # checkers
        if self.request.POST[name] == 'exist':
            return block.Manage_Exist()

        # getters
        if self.request.POST[name] == 'get':
            return block.Manage_Get()

        # auto/mini form
        if self.request.POST[name] == 'little':
            return block.Manage_Little_Form()

        # filters
        if self.request.POST[name] == 'filter':
            return block.Manage_Filter()

        # options
        if self.request.POST[name] == 'button':
            return block.Manage_Button()

        return self.website.Error_No_Event()

    @staticmethod
    def Packing(response):

        data = {
            'code': response.status_code,
            'html': response.content.decode('utf-8')
        }

        return data

    def Direct(self):

        variables = self.request.POST.keys()
        response = {}

        # manage only block variables
        for var in variables:
            if var.startswith('__') and var.endswith('__'):

                html_response = self.Manage(var)
                response[var] = self.Packing(html_response)

        return JsonResponse(response)

    def __init__(self, website):
        Base.__init__(self, website)

        self.website = website
        self.blocks = {
            '__ground__': self.website,
            '__cart__': Cart_Part(self),
            '__header__': Menu_Standard_Part(self),
            '__navigation__': Menu_Mobile_Part(self),
            '__searcher__': Searcher_Part(self),
            '__dialog__': Dialog_Part(self)
        }
