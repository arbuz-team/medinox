from django.conf.urls import url
from server.manage.root.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='root.start'),
    url(r'^zaloguj/$', Sign_In.Launch, name='root.sign_in'),
    url(r'^wyloguj/$', Sign_Out.Launch, name='root.sign_out'),
    url(r'^szczegóły_firmy/$', Company_Details_Manager.Launch, name='root.company_details'),
    url(r'^płatności_użytkowników/$', Users_Payments.Launch, name='root.users_payments'),
    url(r'^wyszukiwarka_płatności/$', Search_Payments.Launch, name='root.search_payments'),
    url(r'^wybrana_płatność_użytkownika/(?P<pk>\d+)/$', Selected_User_Payment.Launch, name='root.selected_user_payment'),
    url(r'^media_społecznościowe/$', Social_Media_Manager.Launch, name='root.social_media'),
    url(r'^opcje_dostawy/$', Delivery_Settings.Launch, name='root.delivery_settings'),
    url(r'^ustawienia_płatności/$', Payment_Settings.Launch, name='root.payment_settings'),
    url(r'^dane_publiczne/$', Data_For_Public.Launch, name='root.data_for_public'),

    url(r'^zaloguj/przekierowanie/(?P<url>.+)/$',
        Sign_In.Redirect, name='root.sign_in.redirect'),
]

