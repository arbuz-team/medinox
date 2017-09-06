from .sort_accuracy import *
from .sort_price import *
from .sort_name import *

from django.db.models import Q
from functools import reduce
import operator


class Search_Engine(Base):

    def __Select_Products(self):

        language = self.request.session['translator_language']
        self.products = SQL.Filter(Product, None,
            reduce(operator.or_, (Q(name__icontains=s)                      for s in self.words)) |
            reduce(operator.or_, (Q(brand__name__icontains=s)               for s in self.words)) |
            reduce(operator.or_, (Q(description__header__icontains=s)       for s in self.words)) |
            reduce(operator.or_, (Q(description__paragraph__icontains=s)    for s in self.words)) |
            reduce(operator.or_, (Q(widget__name__icontains=s)              for s in self.words)) |
            reduce(operator.or_, (Q(widget__values__name__icontains=s)      for s in self.words)) &
                                  Q(language=language)
        )



    def __Sort_Result_Filters(self):

        brands = self.request.session['searcher_filter_brand']
        if not brands:
            return

        get_brands = lambda pks: pks \
            if pks else SQL.All(Brand).values('pk')

        self.products = SQL.Filter(Product, None,
            Q(brand__in=get_brands(brands)) &
            Q(pk__in=self.products.values('pk'))
        ).distinct()

    def __Sort_Result(self):

        sort_name = self.request.session['searcher_sort_name']
        self.__Sort_Result_Filters()

        if sort_name == 'search_accuracy':
            self.products = Sort_By_Accuracy(self).Sort()

        if sort_name == 'price':
            self.products = Sort_By_Price(self).Sort()

        if sort_name == 'name_of_product':
            self.products = Sort_By_Name(self).Sort()

    @staticmethod
    def Get_Words(phrase):
        phrase = phrase.split(' ')
        return [word for word in phrase if word]

    def Search_Products(self):

        # get products from database
        if self.words: self.__Select_Products()
        else: self.products = SQL.All(Product)

        # sorting selected products
        self.__Sort_Result()
        return self.products

    def __init__(self, _object, phrase):
        Base.__init__(self, _object)
        self.products = None
        self.words = []

        if phrase: self.words = \
            self.Get_Words(phrase)
