from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='product.start'),
    url(r'^(?P<pk>\d+)/$', views.Product_Details.Details, name='product.details'),
    url(r'^(?P<pk>\d+)/.+/$', views.Product_Details.Details, name='product.details_with_name'),
    url(r'^new/', views.New_Product.Launch, name='product.new_product'),
    url(r'^edit/(?P<pk>\d+)/', views.Edit_Product.Edit, name='product.edit_product'),
    url(r'^delete/', views.Delete.Product, name='product.delete_product'),
    url(r'^recommended/', views.Recommended_Product_Manager.Launch, name='product.recommended'),
    url(r'^favorite/', views.Favorite_Product_Manager.Launch, name='product.favorite'),
    url(r'^brand/', views.Delete.Brand, name='product.delete_brand'),
    url(r'^purpose/', views.Delete.Purpose, name='product.delete_purpose'),
]
