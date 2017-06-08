from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='product.start'),
    url(r'^(?P<pk>\d+)/(?P<name>\w+)/$', views.Details.Details, name='product.details'),
    url(r'^manage/$', views.Product_Manager.Launch, name='product.manage'),
    url(r'^widget/manage/$', views.Widget_Manager.Launch, name='product.widget.manage'),
    url(r'^values/manage/$', views.Values_Manager.Launch, name='product.values.manage'),
    url(r'^description/manage/$', views.Description_Manager.Launch, name='product.description.manage'),
]
