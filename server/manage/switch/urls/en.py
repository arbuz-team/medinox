from django.conf.urls import url, include
from server.manage.switch.website.content.errors_handler import *

urlpatterns = [
    url(r'^user/', include('server.manage.user.urls.en'), name='user'),
    url(r'^root/', include('server.manage.root.urls.en'), name='root'),
    url(r'^product/', include('server.ground.product.urls.en'), name='product'),
    url(r'^catalog/', include('server.ground.catalog.urls.en'), name='catalog'),
    url(r'^setting/', include('server.manage.setting.urls.en'), name='setting'),
    url(r'^payment/', include('server.service.payment.urls.en'), name='payment'),
    url(r'^pdf/', include('server.service.pdf.urls.en'), name='pdf'),
    url(r'', include('server.ground.main.urls.en'), name='main'),
]

handler403 = Errors_Handler.Code_403
handler404 = Errors_Handler.Code_404
handler500 = Errors_Handler.Code_500