from django.conf.urls import url
from server.manage.user.account import views

urlpatterns = [
    url(r'^$', views.Panel_App.Launch, name='user.account'),
    url(r'^szczegoly/$', views.Account_Details.Launch, name='user.account.details'),
    url(r'^adresy/$', views.User_Addresses.Launch, name='user.account.addresses'),
    url(r'^moje zakupy/$', views.My_Shopping.Launch, name='user.account.my_shopping'),
    url(r'^ulubione/$', views.Favorite.Launch, name='user.account.favorite'),

    url(r'^adresy/przekierowanie/(?P<url>.+)/$',
        views.User_Addresses.Redirect, name='user.account.addresses.redirect'),
]
