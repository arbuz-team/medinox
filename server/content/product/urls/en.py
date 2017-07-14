from django.conf.urls import url
from server.content.product.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='product.start'),
    url(r'^:/$', Products.Launch, name='product.products'),
    url(r'^(?P<pk>\d+)/(?P<name>\w+)/$', Details.Details, name='product.details'),
    url(r'^manage/$', Product_Manager.Launch, name='product.manage'),
    url(r'^widget/manage/$', Widget_Manager.Launch, name='product.widget.manage'),
    url(r'^values/manage/$', Values_Manager.Launch, name='product.values.manage'),
    url(r'^description/manage/$', Description_Manager.Launch, name='product.description.manage'),
]
