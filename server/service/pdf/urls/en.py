from django.conf.urls import url
from server.service.pdf import views

urlpatterns = [
    url(r'^$', views.Generator_PDF.Launch, name='pdf.start'),
    url(r'^invoice/(?P<pk>\d+)/$', views.Generator_PDF.Launch, name='pdf.invoice'),
]

