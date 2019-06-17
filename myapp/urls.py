from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include, re_path



urlpatterns = [
    path('add_user/<slug:first_name,slug:last_name,slug:email>',views.add_user),
    path('get_user/<slug:email>',views.get_user),

    #url(r^'add_user/',views.add_user),
    #url(r^'get_user/',views.get_user),

]
