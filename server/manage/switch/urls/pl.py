from django.conf.urls import url, include
from server.manage.switch.website.content.errors_handler import *

urlpatterns = [
    url(r'^markdownx/', include('markdownx.urls'), name='markdownx'),
    url(r'^użytkownik/', include('server.manage.user.urls.pl'), name='user'),
    url(r'^administrator/', include('server.manage.root.urls.pl'), name='root'),
    url(r'^produkt/', include('server.ground.product.urls.pl'), name='product'),
    url(r'^katalog/', include('server.ground.catalog.urls.pl'), name='catalog'),
    url(r'^link/', include('server.ground.link.urls.pl'), name='link'),
    url(r'^ustawienia/', include('server.manage.setting.urls.pl'), name='setting'),
    url(r'^płatności/', include('server.service.payment.urls.pl'), name='payment'),
    url(r'^powiadomienia/', include('server.service.notification.urls.pl'), name='notification'),
    url(r'^waluta/', include('server.service.currency.urls.pl'), name='currency'),
    url(r'^pdf/', include('server.service.pdf.urls.pl'), name='pdf'),
    url(r'', include('server.ground.main.urls.pl'), name='main'),
]

handler403 = Errors_Handler.Code_403
handler404 = Errors_Handler.Code_404
handler500 = Errors_Handler.Code_500