from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('user.urls.en'), name='user'),
    url(r'^root/', include('root.urls.en'), name='root'),
    url(r'^statement/', include('statement.urls.en'), name='statement'),
    url(r'^product/', include('product.urls.en'), name='product'),
    url(r'^setting/', include('setting.urls.en'), name='setting'),
    url(r'^searcher/', include('searcher.urls.en'), name='searcher'),
    url(r'^cart/', include('cart.urls.en'), name='cart'),
    url(r'^navigation/', include('navigation.urls.en'), name='navigation'),
    url(r'^payment/', include('payment.urls.en'), name='payment'),
    url(r'^pdf/', include('pdf.urls.en'), name='pdf'),
    url(r'', include('main.urls.en'), name='main'),
]

