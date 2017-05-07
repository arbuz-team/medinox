from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='product.start'),
    url(r'^(?P<pk>\d+)/.+/$', views.Details.Details, name='product.details'),
    url(r'^manage/$', views.Product_Manager.Launch, name='product.manage'),
    url(r'^widget/manage/$', views.Widget_Manager.Launch, name='product.widget.manage'),
]
