from django.conf.urls import url
from catalog import views

urlpatterns = [

    url(r'^$', views.Start_App.Launch, name='catalog.start'),

    url(r'^edit/(?P<pk>.+)/$', views.Edit_Catalog.Edit, name='catalog.edit'),
    url(r'^edit/(?P<pk>.+)/redirect/(?P<url>.+)/$', views.Edit_Catalog.Redirect, name='catalog.edit'),

    url(r'^new/$', views.New_Catalog.Launch, name='catalog.new'),
    url(r'^new/redirect/(?P<url>.+)/$', views.New_Catalog.Redirect, name='catalog.new.redirect'),

    # change catalog
    url(r'^:/$', views.Change_Catalog.Change, name='catalog.change'),
    url(r'^:/(?P<cat_1>\w+)/$', views.Change_Catalog.Change, name='catalog.change1'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/$', views.Change_Catalog.Change, name='catalog.change2'),
    url(r'^:/(?P<cat_1>\w+)/(?P<cat_2>\w+)/(?P<cat_3>\w+)/$', views.Change_Catalog.Change, name='catalog.change3'),

]
