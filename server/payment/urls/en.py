from django.conf.urls import url
from server.payment import views


urlpatterns = [
    url(r'^$', views.Payment_Manager.Launch, name='payment'),
    url(r'^apply/$', views.Apply_Payment.Launch, name='payment.apply'),
    url(r'^cancel/$', views.Cancel_Payment.Launch, name='payment.cancel'),
    url(r'^dotpay/$', views.DotPay.Service, name='payment.dotpay'),
    url(r'^paypal/$', views.PayPal.Service, name='payment.paypal'),
    url(r'^buy/(?P<pk>\d+)/$', views.Buy.Buy_Product, name='payment.buy'),
]
