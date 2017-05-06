from django.conf.urls import url
from catalog import views

urlpatterns = [

    url(r'^$', views.Start_App.Launch, name='catalog.start'),

    # change catalog
    url(r'^:/$', views.Change_Catalog.Change, name='catalog.change'),
    url(r'^:/(?P<cat_1>\w+)/$', views.Change_Catalog.Change, name='catalog.change1'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/$', views.Change_Catalog.Change, name='catalog.change2'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/(?P<cat_3>\w+)/$', views.Change_Catalog.Change, name='catalog.change3'),

]
