from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('add_user/',views.add_user, name='add_user'),
    #path('get_user/',views.get_user, name='get_user'),

    url('add_user/',views.add_user),
    url('get_user/',views.get_user),

]
