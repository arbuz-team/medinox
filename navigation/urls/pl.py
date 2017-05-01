from django.conf.urls import url
from navigation import views

urlpatterns = [
    url(r'^$', views.Navigation.Launch, name='navigation.start'),
]
