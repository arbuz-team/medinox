from django.conf.urls import url
from searcher import views

urlpatterns = [
    url(r'^$', views.Searcher.Launch, name='searcher.start'),
]
