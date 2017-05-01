from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='product.start'),
    url(r'^(?P<pk>\d+)/$', views.Product_Details.Details, name='product.details'),
    url(r'^(?P<pk>\d+)/.+/$', views.Product_Details.Details, name='product.details_with_name'),
    url(r'^nowy/', views.New_Product.Launch, name='product.new_product'),
    url(r'^edytuj/(?P<pk>\d+)/', views.Edit_Product.Edit, name='product.edit_product'),
    url(r'^usun/', views.Delete.Product, name='product.delete_product'),
    url(r'^polecane/', views.Recommended_Product_Manager.Launch, name='product.recommended'),
    url(r'^ulubione/', views.Favorite_Product_Manager.Launch, name='product.favorite'),
    url(r'^producenta/', views.Delete.Brand, name='product.delete_brand'),
    url(r'^przeznaczenie/', views.Delete.Purpose, name='product.delete_purpose'),
]
