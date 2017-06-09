from django.conf.urls import url
from server.cart import views

urlpatterns = [
    url(r'^$', views.Cart_Manager.Launch, name='cart.start'),
]
