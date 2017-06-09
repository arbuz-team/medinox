from django.conf.urls import url, include

urlpatterns = [
    url(r'^uzytkownik/', include('server.user.urls.pl'), name='user'),
    url(r'^administrator/', include('server.root.urls.pl'), name='root'),
    url(r'^komunikat/', include('server.statement.urls.pl'), name='statement'),
    url(r'^produkt/', include('server.product.urls.pl'), name='product'),
    url(r'^ustawienia/', include('server.setting.urls.pl'), name='setting'),
    url(r'^wyszukiwarka/', include('server.searcher.urls.pl'), name='searcher'),
    url(r'^koszyk/', include('server.cart.urls.pl'), name='cart'),
    url(r'^nawigacja/', include('server.navigation.urls.pl'), name='navigation'),
    url(r'^platnosci/', include('server.payment.urls.pl'), name='payment'),
    url(r'^pdf/', include('server.pdf.urls.pl'), name='pdf'),
    url(r'', include('server.main.urls.pl'), name='main'),
]

