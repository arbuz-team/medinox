from django.conf.urls import url, include

urlpatterns = [
    url(r'^uzytkownik/', include('server.manage.user.urls.pl'), name='user'),
    url(r'^administrator/', include('server.manage.root.urls.pl'), name='root'),
    url(r'^komunikat/', include('server.content.statement.urls.pl'), name='statement'),
    url(r'^produkt/', include('server.content.product.urls.pl'), name='product'),
    url(r'^ustawienia/', include('server.manage.setting.urls.pl'), name='setting'),
    url(r'^wyszukiwarka/', include('server.page.searcher.urls.pl'), name='searcher'),
    url(r'^koszyk/', include('server.page.cart.urls.pl'), name='cart'),
    url(r'^nawigacja/', include('server.page.navigation.urls.pl'), name='navigation'),
    url(r'^platnosci/', include('server.service.payment.urls.pl'), name='payment'),
    url(r'^pdf/', include('server.service.pdf.urls.pl'), name='pdf'),
    url(r'', include('server.content.main.urls.pl'), name='main'),
]

