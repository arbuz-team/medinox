from django.conf.urls import url
from server.content.catalog import views

urlpatterns = [

    url(r'^$', views.Panel_App.Launch, name='catalog.start'),
    url(r'^manage/$', views.Catalog_Manager.Launch, name='catalog.manager'),

    # change catalog
    url(r'^:/$', views.Catalog_Switcher.Launch, name='catalog.switcher.empty'),
    url(r'^:/(?P<catalog_path>.+)$', views.Catalog_Switcher.Launch, name='catalog.switcher'),

]
