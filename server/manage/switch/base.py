from server.manage.switch.settings import *

from django.utils.timezone import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from abc import ABCMeta, abstractmethod
import string, time

class Base:

    def __init__(self, _object):
        self.request = _object.request

