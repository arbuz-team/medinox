from django.conf.urls import url, include
from server.manage.user import views

urlpatterns = [
    url(r'^$', views.Panel_App.Launch, name='user.start'),
    url(r'^zaloguj/$', views.Sign_In.Launch, name='user.sign_in'),
    url(r'^zarejestruj/$', views.Sign_Up.Launch, name='user.sign_up'),
    url(r'^wyloguj/$', views.Sign_Out.Launch, name='user.sign_out'),
    url(r'^konto/', include('user.account.urls.en'), name='user.account'),
    url(r'^potwierdzenie/(?P<key>[a-z0-9]{40})/$',
        views.Approved_Register.Update_User_Status, name='user.approved'),

    url(r'^zapomnialem/$', views.Forgot_Password.Launch, name='user.forgot'),
    url(r'^zmien_haslo/(?P<key>[a-z0-9]{40})/$',
        views.Change_Password.Secure, name='user.change_password'),

    url(r'^zaloguj/przekierowanie/(?P<url>.+)/$',
        views.Sign_In.Redirect, name='user.sign_in.redirect'),

    url(r'^regulamin/$', views.User_Agreement.Launch, name='user.agreement'),
]
