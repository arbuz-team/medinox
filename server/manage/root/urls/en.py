from django.conf.urls import url
from server.manage.root.views import *

urlpatterns = [
    url(r'^$', Panel_App.Launch, name='root.start'),
    url(r'^sign_in/$', Sign_In.Launch, name='root.sign_in'),
    url(r'^sign_out/$', Sign_Out.Launch, name='root.sign_out'),
    url(r'^company_details/$', Company_Details_Manager.Launch, name='root.company_details'),
    url(r'^users_payments/$', Users_Payments.Launch, name='root.users_payments'),
    url(r'^search_payments/$', Search_Payments.Launch, name='root.search_payments'),
    url(r'^selected_user_payment/(?P<pk>\d+)/$', Selected_User_Payment.Launch, name='root.selected_user_payment'),
    url(r'^social_media/$', Social_Media_Manager.Launch, name='root.social_media'),
    url(r'^delivery_settings/$', Delivery_Settings.Launch, name='root.delivery_settings'),

    url(r'^sign_in/redirect/(?P<url>.+)/$',
        Sign_In.Redirect, name='root.sign_in.redirect'),
]

