from django.conf.urls import url
from server.service.payment.views import *


urlpatterns = [
    url(r'^$', Payment_Manager.Launch, name='payment'),
    url(r'^apply/$', Apply_Payment.Launch, name='payment.apply'),
    url(r'^cancel/$', Cancel_Payment.Launch, name='payment.cancel'),
    url(r'^dotpay/$', DotPay.Service, name='payment.dotpay'),
    url(r'^paypal/$', PayPal.Service, name='payment.paypal'),
    url(r'^buy/(?P<pk>\d+)/$', Buy.Launch, name='payment.buy'),
    url(r'^cart/(?P<pk>\d+)/$', Cart_Manager.Launch, name='payment.cart_manager'),
]
