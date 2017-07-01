from django.conf.urls import url
from qforum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
