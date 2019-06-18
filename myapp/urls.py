from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include, re_path



urlpatterns = [
    path('add_user/<str:email>',views.add_user, name="add_user"),
    path('get_user/',views.get_user, name="get_user"),



]
