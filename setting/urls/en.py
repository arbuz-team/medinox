from django.conf.urls import url
from setting import views

urlpatterns = [
    url(r'^$', views.Control_Panel.Launch, name='setting.start'),
]
