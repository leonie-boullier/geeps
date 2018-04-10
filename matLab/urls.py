from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.formulaire, name='formulaire'),
    url(r'^licence/(?P<pk>[0-9]+)/$', views.licence_detail, name='licence_detail'),
]
