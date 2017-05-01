from django.conf.urls import url, include

urlpatterns = [
    url(r'^uzytkownik/', include('user.urls.pl'), name='user'),
    url(r'^administrator/', include('root.urls.pl'), name='root'),
    url(r'^komunikat/', include('statement.urls.pl'), name='statement'),
    url(r'^produkt/', include('product.urls.pl'), name='product'),
    url(r'^ustawienia/', include('setting.urls.pl'), name='setting'),
    url(r'^wyszukiwarka/', include('searcher.urls.pl'), name='searcher'),
    url(r'^koszyk/', include('cart.urls.pl'), name='cart'),
    url(r'^nawigacja/', include('navigation.urls.pl'), name='navigation'),
    url(r'^platnosci/', include('payment.urls.pl'), name='payment'),
    url(r'^pdf/', include('pdf.urls.pl'), name='pdf'),
    url(r'', include('main.urls.pl'), name='main'),
]

