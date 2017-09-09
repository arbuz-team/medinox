from .sort_accuracy import *

from django.db.models import Q
from functools import reduce
import operator


class Search_Engine(Base):

    def __Select_Payment(self):

        self.payments = SQL.Filter(Model_Payment, None,
            reduce(operator.or_, (Q(user__email__icontains=s)                           for s in self.words)) |
            reduce(operator.or_, (Q(user__username__icontains=s)                        for s in self.words)) |
            reduce(operator.or_, (Q(model_delivery_address__full_name__icontains=s)     for s in self.words)) |
            reduce(operator.or_, (Q(model_delivery_address__address_line__icontains=s)  for s in self.words)) |
            reduce(operator.or_, (Q(model_delivery_address__city__icontains=s)          for s in self.words)) |
            reduce(operator.or_, (Q(model_delivery_address__region__icontains=s)        for s in self.words)) |
            reduce(operator.or_, (Q(model_delivery_address__postcode__icontains=s)      for s in self.words)) |
            reduce(operator.or_, (Q(model_invoice_address__full_name__icontains=s)      for s in self.words)) |
            reduce(operator.or_, (Q(model_invoice_address__address_line__icontains=s)   for s in self.words)) |
            reduce(operator.or_, (Q(model_invoice_address__city__icontains=s)           for s in self.words)) |
            reduce(operator.or_, (Q(model_invoice_address__region__icontains=s)         for s in self.words)) |
            reduce(operator.or_, (Q(model_invoice_address__postcode__icontains=s)       for s in self.words)) |
            reduce(operator.or_, (Q(model_deadline__name__icontains=s)                  for s in self.words)) |
            reduce(operator.or_, (Q(model_note__note__icontains=s)                      for s in self.words)) |
            reduce(operator.or_, (Q(model_note__model_note_file__name__icontains=s)     for s in self.words))
        )



    def __Sort_Result(self):
        self.payments = Sort_By_Accuracy(self).Sort()

    @staticmethod
    def Get_Words(phrase):
        phrase = phrase.split(' ')
        return [word for word in phrase if word]

    def Search_Payments(self):

        # get products from database
        if self.words: self.__Select_Payment()
        else: self.payments = SQL.All(Model_Payment)

        # sorting selected products
        self.__Sort_Result()
        return self.payments

    def __init__(self, _object, phrase):
        Base.__init__(self, _object)
        self.payments = None
        self.words = []

        if phrase: self.words = \
            self.Get_Words(phrase)
