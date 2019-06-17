from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include, re_path



urlpatterns = [
    re_path(r'^add_user/',views.add_user, name='add_user'),
    re_path(r'^get_user/',views.get_user, name='get_user'),

    #url(r^'add_user/',views.add_user),
    #url(r^'get_user/',views.get_user),

]
