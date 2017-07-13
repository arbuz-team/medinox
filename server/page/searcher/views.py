from server.manage.switch.website.manager import *
from django.http.response import HttpResponse
from server.content.product.base import *
from server.content.product.models import *
from django.db.models import Q
from functools import reduce
import operator


class Search_Priorities:

    def Get_Priorities(self, word):
        word = word.lower()
        accuracy = 0

        accuracy += self.name.count(word) * 10
        accuracy += self.keywords.count(word) * 5
        accuracy += self.filters.count(word) * 3
        accuracy += self.content.count(word)

        return accuracy

    def __init__(self, name, keywords='',
                 filters='', content=''):

        self.name = name.lower()
        self.keywords = keywords.lower()
        self.filters = filters.lower()
        self.content = content.lower()



class Search_Engine:

    def Search_Products_EN(self):

        self.result = SQL.Filter(Product,
            reduce(operator.or_, (Q(details_en__name__icontains=s)          for s in self.phrase)) |
            reduce(operator.or_, (Q(details_en__description__icontains=s)   for s in self.phrase)) |
            reduce(operator.or_, (Q(keywords__icontains=s)                  for s in self.phrase)) |
            reduce(operator.or_, (Q(brand__name__icontains=s)               for s in self.phrase)) &
                                  Q(where_display__display_en=True)
        )

    def Search_Products_PL(self):

        self.result = SQL.Filter(Product,
            reduce(operator.or_, (Q(details_pl__name__icontains=s)          for s in self.phrase)) |
            reduce(operator.or_, (Q(details_pl__description__icontains=s)   for s in self.phrase)) |
            reduce(operator.or_, (Q(keywords__icontains=s)                  for s in self.phrase)) |
            reduce(operator.or_, (Q(brand__name__icontains=s)               for s in self.phrase)) &
                                  Q(where_display__display_pl=True)
        )

    def Search_Products_DE(self):

        self.result = SQL.Filter(Product,
            reduce(operator.or_, (Q(details_de__name__icontains=s)          for s in self.phrase)) |
            reduce(operator.or_, (Q(details_de__description__icontains=s)   for s in self.phrase)) |
            reduce(operator.or_, (Q(keywords__icontains=s)                  for s in self.phrase)) |
            reduce(operator.or_, (Q(brand__name__icontains=s)               for s in self.phrase)) &
                                  Q(where_display__display_de=True)
        )

    def Search_Products(self):

        if not self.phrase: # phrase is empty
            self.result = SQL.All(Product)

        else:

            if self.request.session['translator_language'] == 'EN':
                self.Search_Products_EN()

            if self.request.session['translator_language'] == 'PL':
                self.Search_Products_PL()

            if self.request.session['translator_language'] == 'DE':
                self.Search_Products_DE()

        self.Sort_Result()
        return self.result

    def Sort_Result_Order_By_Accuracy(self):

        if not self.phrase:
            return

        # convert product to string
        products_as_string = \
        [
            (
                product.pk, # repetitions set range
                Search_Priorities(
                    name=self.product_models_manager.Get_Product_Name(product),
                    content=self.product_models_manager.Get_Product_Description(product),
                    filters=product.brand.name,
                    keywords=product.keywords
                )
            )
            for product in self.result
        ]

        # tuple contains position of products
        positions = []
        for product in products_as_string:

            accuracy = 0
            for word in self.phrase:
                accuracy += product[1].Get_Priorities(word)

            positions.append((accuracy, product[0]))  # (hits, id)

        # sort positions by hits/price/name
        direction = self.request.session['searcher_order_direction']
        if direction == 'descending':
            positions.sort(reverse=True)

        else: positions.sort()

        # select ordered data from database
        sorted_pks = [pos[1] for pos in positions]
        ordering = ''

        for to_pk, from_pk in enumerate(sorted_pks):
            ordering += 'WHEN id={0} THEN {1} '.format(from_pk, to_pk)

        ordering = 'CASE {0} END'.format(ordering)
        self.result = SQL.Filter(Product, pk__in=self.result).extra(
            select={'ordering': ordering}, order_by=['ordering'])

    def Sort_Result_Order_By_Price(self):

        direction = self.request.session['searcher_order_direction']
        order_by = 'price_eur'

        if direction == 'descending':
            order_by = '-' + order_by

        self.result = SQL.Filter(Product,
            pk__in=self.result).order_by(order_by)

    def Sort_Result_Order_By_Name(self):

        direction = self.request.session['searcher_order_direction']
        language = self.request.session['translator_language']
        order_by = 'details_{0}__name'.format(language.lower())

        if direction == 'descending':
            order_by = '-' + order_by

        self.result = SQL.Filter(Product,
            pk__in=self.result).order_by(order_by)

    def Sort_Result_Filters(self):

        brands = self.request.session['searcher_filter_brand']
        if not brands:
            return

        get_brands = lambda pks: pks \
            if pks else Brand.objects.values('pk')

        self.result = SQL.Filter(Product,
            Q(brand__in=get_brands(brands))         &
            Q(pk__in=self.result.values('pk'))
        ).distinct()

    def Sort_Result(self):
        self.Sort_Result_Filters()

        if self.request.session['searcher_order_name'] == 'search_accuracy':
            self.Sort_Result_Order_By_Accuracy()

        if self.request.session['searcher_order_name'] == 'price':
            self.Sort_Result_Order_By_Price()

        if self.request.session['searcher_order_name'] == 'name_of_product':
            self.Sort_Result_Order_By_Name()

    def Remove_Empty_Word(self):
        self.phrase = \
            [word for word in self.phrase if word]

    @staticmethod
    def Get_Polish_Word_Variations(word):

        file = open(BASE_DIR + '/searcher/variations/PL')
        lines = file.read().splitlines()
        file.close()
        for line in lines:
            if word in line:
                return line

    @staticmethod
    def Filter_Products(request):
        request.session['product_page'] = 1
        phrase = request.session['searcher_phrase']
        searcher = Search_Engine(request, phrase)
        request.session['searcher_result'] = \
            searcher.Search_Products()

    def __init__(self, request, phrase):
        self.result = []
        self.request = request
        self.phrase = phrase
        self.product_models_manager = \
            Product_Models_Manager(self.request)

        if self.phrase:
            self.phrase = phrase.split(' ')
            self.Remove_Empty_Word()



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
