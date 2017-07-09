from server.manage.switch.settings import *
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    def __init__(self, _object):
        self.request = _object.request
