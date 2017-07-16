from server.manage.switch.website.manager import *
from server.ground.product.base import *
from server.ground.product.models import *


class Searcher(Website_Manager):

    def Manage_Content_Searcher(self):
        self.content['brands'] = SQL.All(Brand)
        return self.Render_HTML('searcher/searcher.html')

    def Manage_Content(self):

        if self.request.POST['__content__'] == 'searcher':
            return self.Manage_Content_Searcher()

        return Website_Manager.Manage_Content(self)

    def Manage_Filter_Brand(self):
        filters = self.request.session['searcher_filter_brand']

        if self.request.POST['action'] == 'append':#
            if self.request.POST['name'] not in filters:
                filters.append(self.request.POST['name'])
                self.request.session['searcher_filter_brand'] = filters

        if self.request.POST['action'] == 'delete':
            if self.request.POST['name'] in filters:
                filters.remove(self.request.POST['name'])
                self.request.session['searcher_filter_brand'] = filters

        return JsonResponse({'__filter__': 'true'})

    def Manage_Filter_Phrase(self):
        self.request.session['searcher_phrase'] = \
            self.request.POST['value']

        return JsonResponse({'__filter__': 'true'})

    def Manage_Filter_Order(self):

        if 'name' in self.request.POST['__filter__']:
            self.request.session['searcher_order_name'] = \
                self.request.POST['value']

        if 'direction' in self.request.POST['__filter__']:
            self.request.session['searcher_order_direction'] = \
                self.request.POST['value']

        return JsonResponse({'__filter__': 'true'})

    def Manage_Filter(self):

        if self.request.POST['__filter__'] == 'brand':
            return self.Manage_Filter_Brand()

    @staticmethod
    def Launch(request):
        searcher = Searcher(request, clear_session=True)
        # Search_Engine.Filter_Products(request)
        return searcher.HTML
