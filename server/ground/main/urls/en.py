from django.conf.urls import url
from server.ground.main.views import *


urlpatterns = [
    url(r'^$', Home.Launch, name='main.start'),
    url(r'^about/$', About.Launch, name='main.about'),
    url(r'^contact/$', Contact.Launch, name='main.contact'),

    url(r'^about/manage/$', About.Launch, name='main.about.manage'),
    url(r'^contact/manage/$', Contact.Launch, name='main.contact.manage'),
]
