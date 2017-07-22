from server.manage.switch.website.endpoints import *
from server.manage.switch.website.base import *
from server.ground.product.models import *


class Searcher_Block(Endpoints):

    def Manage_Content(self):
        self.context['brands'] = SQL.All(Brand)
        return self.Render_HTML('block/searcher.html')

    def Manage_Filter_Phrase(self):
        self.request.session['searcher_result'] = None
        self.request.session['searcher_phrase'] = \
            self.request.POST['value']

        return HttpResponse()

    def Manage_Filter_Brand(self):
        self.request.session['searcher_result'] = None
        filters = self.request.session['searcher_filter_brand']

        if self.request.POST['action'] == 'append':#
            if self.request.POST['name'] not in filters:
                filters.append(self.request.POST['name'])
                self.request.session['searcher_filter_brand'] = filters

        if self.request.POST['action'] == 'delete':
            if self.request.POST['name'] in filters:
                filters.remove(self.request.POST['name'])
                self.request.session['searcher_filter_brand'] = filters

        return HttpResponse()

    def Manage_Filter_Order(self):

        if 'name' in self.request.POST['_name_']:
            self.request.session['searcher_sort_name'] = \
                self.request.POST['value']

        if 'direction' in self.request.POST['_name_']:
            self.request.session['searcher_sort_direction'] = \
                self.request.POST['value']

        return HttpResponse()

    def Manage_Filter(self):

        if self.request.POST['_name_'] == 'phrase':
            return self.Manage_Filter_Phrase()

        if self.request.POST['_name_'] == 'brand':
            return self.Manage_Filter_Brand()

        if self.request.POST['_name_'] == 'order':
            return self.Manage_Filter_Order()

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/searcher.html', context=context))
