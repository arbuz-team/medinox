from django.conf.urls import url, include
from server.service.notification.views import *

urlpatterns = [
    url(r'^$', Notification_Manager.Launch, name='notification'),
]
