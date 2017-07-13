from django.conf.urls import url
from server.content.main import views


urlpatterns = [
    url(r'^$', views.Start.Launch, name='main.start'),
    url(r'^about/$', views.About.Launch, name='main.about'),
    url(r'^contact/$', views.Contact.Launch, name='main.contact'),

    url(r'^about/manage/$', views.About.Launch, name='main.about.manage'),
    url(r'^contact/manage/$', views.Contact.Launch, name='main.contact.manage'),

    url(r'^example/$', views.Json_Example.Launch, name='main.json_example'),
]
