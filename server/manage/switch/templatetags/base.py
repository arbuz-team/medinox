from server.manage.switch.website.base import *
from inspect import getmembers, ismethod
from django import template
register = template.Library()

class Base_Tag_Manager(Base_Website):

    def __init__(self, task, values, request=None):
        self.request = request

        Base_Website.__init__(self, self)
        self.values = values

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if task in method:
                self.OUT = getattr(self.__class__, method)(self)
