from .part import *


class Direct_Part_Manager(Base):

    def Manage(self, _object):

        # parts of pages
        if '__content__' in self.request.POST:
            return _object.Manage_Content()

        # manage forms
        if '__form__' in self.request.POST:
            return _object.Manage_Form()

        # checkers
        if '__exist__' in self.request.POST:
            return _object.Manage_Exist()

        # getters
        if '__get__' in self.request.POST:
            return _object.Manage_Get()

        # auto/mini form
        if '__little__' in self.request.POST:
            return _object.Manage_Little_Form()

        # filters
        if '__filter__' in self.request.POST:
            return _object.Manage_Filter()

        # options
        if '__button__' in self.request.POST:
            return _object.Manage_Button()

        return self.website.Error_No_Event()

    @staticmethod
    def Get_Content_Data(response):

        data = {
            'status': response.status_code,
            'html': response.content.decode('utf-8')
        }

        return data

    @staticmethod
    def Get_Contents_List(contents):

        contents = contents.split(' ')
        content_list = []

        for part in contents:
            if part: content_list.append(part)

        return content_list

    def Generate_Content(self):

        contents = self.request.POST['__content__']
        contents = self.Get_Contents_List(contents)
        response = {'__content__': {}}

        for content in contents:
            part = self.parts[content]
            html = self.Manage(part)

            response['__content__'][content] = \
                self.Get_Content_Data(html)

        return JsonResponse(response)

    def Direct(self):

        if '__content__' in self.request.POST:
            return self.Generate_Content()

        direct =  self.request.POST['_direct_']
        return self.Manage(self.parts[direct])

    def __init__(self, website):
        Base.__init__(self, website)

        self.website = website
        self.parts = {
            'ground': self.website,
            'cart': Cart_Manager(self),
            'header': Header(self),
            'navigation': Navigation(self),
            'searcher': Searcher(self)
        }
