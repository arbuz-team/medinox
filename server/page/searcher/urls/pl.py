from django.conf.urls import url
from server.page.searcher import views

urlpatterns = [
    url(r'^$', views.Searcher.Launch, name='searcher.start'),
]
