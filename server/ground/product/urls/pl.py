from django.conf.urls import url
from server.ground.product.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='product.start'),
    url(r'^:/$', Products.Launch, name='product.products'),
    url(r'^(?P<pk>\d+)/(?P<product_name>.+)/$', Details.Launch, name='product.details'),
    url(r'^(?P<pk>\d+)/$', Details.Launch2, name='product.details2'),
    url(r'^zarządzaj/$', Product_Manager.Launch, name='product.manage'),
    url(r'^widżet/zarządzaj/$', Widget_Manager.Launch, name='product.widget.manage'),
    url(r'^opcje/zarządzaj/$', Values_Manager.Launch, name='product.values.manage'),
    url(r'^opis/zarządzaj/$', Description_Manager.Launch, name='product.description.manage'),
    url(r'^marka/zarządzaj/$', Brand_Manager.Launch, name='product.brand.manage'),
]
