from django.conf.urls import url
from server.service.currency.views.manager import *

urlpatterns = [
    url(r'^$', Currency_Manager.Launch, name='currency.start'),
]

