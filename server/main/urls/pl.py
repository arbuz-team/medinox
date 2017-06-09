from django.conf.urls import url
from server.main import views

urlpatterns = [
    url(r'^$', views.Start.Launch, name='main.start'),
    url(r'^o_nas/$', views.About.Launch, name='main.about'),
    url(r'^produkty/$', views.Products.Launch, name='main.products'),
    url(r'^kontakt/$', views.Contact.Launch, name='main.contact'),

    url(r'^o_nas/edytuj/(?P<pk>\d+)/$', views.About.Edit, name='main.edit_about'),
    url(r'^kontakt/edytuj/(?P<pk>\d+)/$', views.Contact.Edit, name='main.edit_contact'),

    url(r'^about/new/$', views.About.New, name='main.new_about'),
    url(r'^about/edit/(?P<pk>\d+)/$', views.About.Edit, name='main.edit_about'),
    url(r'^about/delete/$', views.About.Delete, name='main.delete_about'),

    url(r'^contact/new/$', views.Contact.New, name='main.new_contact'),
    url(r'^contact/edit/(?P<pk>\d+)/$', views.Contact.Edit, name='main.edit_contact'),
    url(r'^contact/delete/$', views.Contact.Delete, name='main.delete_contact'),
]
