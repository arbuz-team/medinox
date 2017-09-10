from django.conf.urls import url, include
from server.manage.user.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='user.start'),
    url(r'^sign_in/$', Sign_In.Launch, name='user.sign_in'),
    url(r'^sign_up/$', Sign_Up.Launch, name='user.sign_up'),
    url(r'^sign_out/$', Sign_Out.Launch, name='user.sign_out'),
    url(r'^account/', include('server.manage.user.account.urls.en'), name='user.account'),
    url(r'^approved/(?P<key>[a-z0-9]{40})/$',
        Approved_Register.Update_User_Status, name='user.approved'),

    url(r'^forgot/$', Forgot_Password.Launch, name='user.forgot'),
    url(r'^change_password/(?P<key>[a-z0-9]{40})/$',
        Change_Password.Secure, name='user.change_password'),

    url(r'^sign_in/cart/$', Sign_In_Cart.Launch, name='user.sign_in_cart'),
    url(r'^sign_in/redirect/(?P<url>.+)/$',
        Sign_In.Redirect, name='user.sign_in.redirect'),

    url(r'^agreement/$', User_Agreement.Launch, name='user.agreement'),
]
