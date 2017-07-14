from django.conf.urls import url
from server.content.catalog.views.switch import *
from server.content.catalog.views.manager import *
from server.content.catalog.views.panel_app import *

urlpatterns = [

    url(r'^$', Panel_App.Launch, name='catalog.start'),
    url(r'^manage/$', Catalog_Manager.Launch, name='catalog.manager'),

    # change catalog
    url(r'^:/$', Switch.Launch, name='catalog.switcher.empty'),
    url(r'^:/(?P<catalog_path>.+)$', Switch.Launch, name='catalog.switcher'),

]
