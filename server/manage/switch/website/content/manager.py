from .block import *


class Direct_Block_Manager(Base):

    def Manage(self, name):
        block = self.blocks[name]

        # parts of pages
        if self.request.POST[name] == 'content':
            return block.Manage_Content()

        # manage forms
        if self.request.POST[name] == 'form':
            return block.Manage_Form()

        # checkers
        if self.request.POST[name] == 'valid':
            return block.Manage_Valid()

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
            'html': response.content.decode('utf-8'), # Backend: change name `html` to `content`
            'code': response.status_code
        }

        # if response url exists
        try: data['url'] = response.url
        except: pass
        return data

    def Create_Block(self, variable):

        # error block for ground
        if variable == '__ground__':
            if self.ground_content:
                return self.Packing(self.ground_content)

        response = self.Manage(variable)
        return self.Packing(response)

    def Direct(self, ground_content=None):

        # variable
        self.request.session['arbuz_response'] = {}
        self.ground_content = ground_content

        variables = self.request.POST.keys()
        exception = None
        response = {}

        # manage only block variables
        for var in variables:
            if var.startswith('__') and var.endswith('__'):

                try:

                    response[var] = self.Create_Block(var)
                    self.request.session['arbuz_response'] = response

                except Exception as e:
                    exception = e

        # error in some blocks
        if exception:
            raise exception

        # response
        self.request.session['arbuz_response'] = {}
        return response

    def __init__(self, website):
        Base.__init__(self, website)

        self.ground_content = None
        self.website = website
        self.blocks = {
            '__ground__': self.website,
            '__cart__': Cart_Block(self),
            '__menu__': Menu_Block(self),
            '__menu_mobile__': Menu_Mobile_Block(self),
            '__searcher__': Searcher_Block(self),
            '__dialog__': Dialog_Block(self)
        }
