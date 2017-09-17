from django.conf.urls import url
from server.service.pdf import views

urlpatterns = [
    url(r'^$', views.Generator_PDF.Launch, name='pdf.start'),
    url(r'^faktura/(?P<pk>\d+)/$', views.Generator_PDF.Launch, name='pdf.invoice'),
]

