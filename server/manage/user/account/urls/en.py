from django.conf.urls import url
from server.manage.user.account.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='user.account'),
    url(r'^details/$', Account_Details.Launch, name='user.account.details'),
    url(r'^addresses/$', User_Addresses.Launch, name='user.account.addresses'),
    url(r'^favorite/$', Favorite.Launch, name='user.account.favorite'),
    url(r'^my_shopping/$', My_Shopping.Launch, name='user.account.my_shopping'),
    url(r'^selected_shopping/(?P<unique>.+)/$', Selected_Shopping.Launch,
        name='user.account.selected_shopping'),

    url(r'^addresses/redirect/(?P<url>.+)/$', User_Addresses.Redirect,
        name='user.account.addresses.redirect'),
]
