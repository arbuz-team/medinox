from django.conf.urls import url
from server.service.payment.views import *


urlpatterns = [
    url(r'^$', Payment_Manager.Launch, name='payment'),
    url(r'^potwierdzenie/$', Apply_Payment.Launch, name='payment.apply'),
    url(r'^anulowanie/$', Cancel_Payment.Launch, name='payment.cancel'),
    url(r'^dotpay/$', DotPay.Service, name='payment.dotpay'),
    url(r'^paypal/$', PayPal.Service, name='payment.paypal'),
    url(r'^płatność_przy_odbiorze/$', Cash_On_Delivery.Service, name='payment.cash_on_delivery'),
    url(r'^opóżniona_płatność/$', Delayed_Transfer.Service, name='payment.delayed_transfer'),
    url(r'^kup_teraz/(?P<pk>\d+)/$', Buy.Launch, name='payment.buy'),
    url(r'^koszyk/(?P<pk>\d+)/$', Cart_Manager.Launch, name='payment.cart_manager'),
]
