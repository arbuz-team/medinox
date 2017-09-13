from server.manage.switch.website.endpoints import *
from server.manage.switch.website.base import *
from server.ground.product.models import *


class Searcher_Block(Endpoints):

    def Manage_Content(self):
        self.context['brands'] = SQL.All(Model_Brand)
        return self.Render_HTML('block/searcher.html')

    def Manage_Filter_Phrase(self):
        self.request.session['searcher_phrase'] = \
            self.request.POST['value']

        return HttpResponse()

    def Manage_Filter_Brand(self):
        filters = self.request.session['searcher_filter_brand']

        if self.request.POST['action'] == 'append':
            if self.request.POST['value'] not in filters:
                filters.append(self.request.POST['value'])
                self.request.session['searcher_filter_brand'] = filters

        if self.request.POST['action'] == 'delete':
            if self.request.POST['value'] in filters:
                filters.remove(self.request.POST['value'])
                self.request.session['searcher_filter_brand'] = filters

        return HttpResponse()

    def Manage_Filter_Sort(self):

        if 'category' in self.request.POST['field']:
            self.request.session['searcher_sort_name'] = \
                self.request.POST['value']

        if 'direction' in self.request.POST['field']:
            self.request.session['searcher_sort_direction'] = \
                self.request.POST['value']

        return HttpResponse()

    def Manage_Filter(self):
        self.request.session['searcher_result'] = None

        if self.request.POST['_name_'] == 'phrase':
            return self.Manage_Filter_Phrase()

        if self.request.POST['_name_'] == 'brand':
            return self.Manage_Filter_Brand()

        if self.request.POST['_name_'] == 'sort':
            return self.Manage_Filter_Sort()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'show_deleted':
            value = self.request.session['catalog_deleted_flag']
            self.request.session['catalog_deleted_flag'] = not value
            return HttpResponse()

        if self.request.POST['_name_'] == 'clear_session':
            self.Clear_Session('searcher_')
            return HttpResponse()

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/searcher.html', context=context))
