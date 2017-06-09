from django.conf.urls import url
from server.user.account import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='user.account'),
    url(r'^details/$', views.Account_Details.Launch, name='user.account.details'),
    url(r'^addresses/$', views.User_Addresses.Launch, name='user.account.addresses'),
    url(r'^my_shopping/$', views.My_Shopping.Launch, name='user.account.my_shopping'),
    url(r'^favorite/$', views.Favorite.Launch, name='user.account.favorite'),

    url(r'^addresses/redirect/(?P<url>.+)/$',
        views.User_Addresses.Redirect, name='user.account.addresses.redirect'),
]
