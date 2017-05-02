from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='product.start'),
    url(r'^(?P<pk>\.+)/$', views.Details.Launch, name='product.details'),
]
