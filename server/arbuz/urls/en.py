from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('server.user.urls.en'), name='user'),
    url(r'^root/', include('server.root.urls.en'), name='root'),
    url(r'^statement/', include('server.statement.urls.en'), name='statement'),
    url(r'^product/', include('server.product.urls.en'), name='product'),
    url(r'^catalog/', include('server.catalog.urls.en'), name='catalog'),
    url(r'^setting/', include('server.setting.urls.en'), name='setting'),
    url(r'^searcher/', include('server.searcher.urls.en'), name='searcher'),
    url(r'^cart/', include('server.cart.urls.en'), name='cart'),
    url(r'^navigation/', include('server.navigation.urls.en'), name='navigation'),
    url(r'^payment/', include('server.payment.urls.en'), name='payment'),
    url(r'^pdf/', include('server.pdf.urls.en'), name='pdf'),
    url(r'', include('server.main.urls.en'), name='main'),
]

