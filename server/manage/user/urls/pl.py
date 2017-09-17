from django.conf.urls import url, include
from server.manage.user.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='user.start'),
    url(r'^zaloguj/$', Sign_In.Launch, name='user.sign_in'),
    url(r'^zarejestruj/$', Sign_Up.Launch, name='user.sign_up'),
    url(r'^wyloguj/$', Sign_Out.Launch, name='user.sign_out'),
    url(r'^konto/', include('server.manage.user.account.urls.pl'), name='user.account'),
    url(r'^potwierdzenie/(?P<key>[a-z0-9]{20})/$',
        Approved_Register.Update_User_Status, name='user.approved'),

    url(r'^zapomniałem/$', Forgot_Password.Launch, name='user.forgot'),
    url(r'^zmiana_hasła/(?P<key>[a-z0-9]{20})/$',
        Change_Password.Secure, name='user.change_password'),

    url(r'^zaloguj/koszyk/$', Sign_In_Cart.Launch, name='user.sign_in_cart'),
    url(r'^zaloguj/przekierowanie/(?P<url>.+)/$',
        Sign_In.Redirect, name='user.sign_in.redirect'),

    url(r'^regulamin/$', User_Agreement.Launch, name='user.agreement'),
]
