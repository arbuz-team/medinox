from django.conf.urls import url
from server.ground.main.views import *


urlpatterns = [
    url(r'^$', Home.Launch, name='main.start'),
    url(r'^o_nas/$', About.Launch, name='main.about'),
    url(r'^kontakt/$', Contact.Launch, name='main.contact'),

    url(r'^start/zarządzaj/$', Home.Launch, name='main.home.manage'),
    url(r'^o_nas/zarządzaj/$', About.Launch, name='main.about.manage'),
    url(r'^kontakt/zarządzaj/$', Contact.Launch, name='main.contact.manage'),
]
