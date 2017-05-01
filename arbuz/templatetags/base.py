from inspect import getmembers, ismethod
from product.base import *
from django import template
register = template.Library()

class Base_Tag_Manager(Dynamic_Base):

    def __init__(self, task, values, request=None):
        Dynamic_Base.__init__(self, request)
        self.values = values

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if task in method:
                self.OUT = getattr(self.__class__, method)(self)
