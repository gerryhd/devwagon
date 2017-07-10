from django.conf.urls import url

from devwagon.apps.qforum import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
]
