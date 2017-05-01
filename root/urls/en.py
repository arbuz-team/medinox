from django.conf.urls import url
from root import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='root.start'),
    url(r'^sign_in/$', views.Sign_In.Launch, name='root.sign_in'),
    url(r'^sign_out/$', views.Sign_Out.Launch, name='root.sign_out'),
    url(r'^company_details/$', views.Company_Details_Manager.Launch, name='root.company_details'),
    url(r'^users_payments/$', views.Users_Payments.Launch, name='root.users_payments'),
    url(r'^social_media/$', views.Social_Media_Manager.Launch, name='root.social_media'),
    url(r'^delivery_settings/$', views.Delivery_Settings.Launch, name='root.delivery_settings'),

    url(r'^sign_in/redirect/(?P<url>.+)/$',
        views.Sign_In.Redirect, name='root.sign_in.redirect'),
]

