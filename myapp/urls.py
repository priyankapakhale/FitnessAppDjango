from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include, re_path



urlpatterns = [
    #re_path(r’^[0-9]+)$’, views.detail, name=’detail’)
    #path('add_user/',views.add_user),
    path('get_user/',views.get_user),
    url(r'^add_user/',views.add_user),


]
