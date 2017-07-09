from server.manage.switch.settings import *
from abc import ABCMeta, abstractmethod


class Base:

    def __init__(self, _object):
        self.request = _object.request
