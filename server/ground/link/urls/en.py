from django.conf.urls import url
from server.ground.link.views import *

urlpatterns = [
    url(r'^$', Link_Manager.Launch, name='link.start'),
]
