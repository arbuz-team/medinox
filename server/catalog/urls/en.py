from django.conf.urls import url
from server.catalog import views

urlpatterns = [

    url(r'^$', views.Start_App.Launch, name='catalog.start'),
    url(r'^manage/$', views.Catalog_Manager.Launch, name='catalog.manager'),

    # change catalog
    url(r'^:/$', views.Catalog_Service.Service, name='catalog.service'),
    url(r'^:/(?P<cat_1>\w+)/$', views.Catalog_Service.Service, name='catalog.service.1'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/$', views.Catalog_Service.Service, name='catalog.service.2'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/(?P<cat_3>\w+)/$', views.Catalog_Service.Service, name='catalog.service.3'),

]
