from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<titulo>\w+)/(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})/artigo\.html$',
        views.viewArtigo, name='artigo'),
]
