from django.conf.urls import url
from server.manage.setting import views

urlpatterns = [
    url(r'^$', views.Control_Panel.Launch, name='setting.start'),
]
