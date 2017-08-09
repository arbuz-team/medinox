from django.conf.urls import url
from server.ground.catalog.views.switch import *
from server.ground.catalog.views.manager import *
from server.ground.catalog.views.panel_app import *

urlpatterns = [

    url(r'^$', Panel_App.Launch, name='catalog.start'),
    url(r'^manage/$', Catalog_Manager.Launch, name='catalog.manager'),

    # change catalog
    url(r'^:/$', Catalog_Switch.Launch, name='catalog.switcher.empty'),
    url(r'^:/(?P<catalog_path>.+)$', Catalog_Switch.Launch, name='catalog.switcher'),

]
