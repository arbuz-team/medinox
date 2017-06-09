from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('server.manage.user.urls.en'), name='user'),
    url(r'^root/', include('server.manage.root.urls.en'), name='root'),
    url(r'^statement/', include('server.content.statement.urls.en'), name='statement'),
    url(r'^product/', include('server.content.product.urls.en'), name='product'),
    url(r'^catalog/', include('server.content.catalog.urls.en'), name='catalog'),
    url(r'^setting/', include('server.manage.setting.urls.en'), name='setting'),
    url(r'^searcher/', include('server.page.searcher.urls.en'), name='searcher'),
    url(r'^cart/', include('server.page.cart.urls.en'), name='cart'),
    url(r'^navigation/', include('server.page.navigation.urls.en'), name='navigation'),
    url(r'^payment/', include('server.service.payment.urls.en'), name='payment'),
    url(r'^pdf/', include('server.service.pdf.urls.en'), name='pdf'),
    url(r'', include('server.content.main.urls.en'), name='main'),
]

