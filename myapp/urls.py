from django.urls import path
from . import views

urlspatterns = [
    path('add_user/',views.add_user, name='add_user'),
    path('get_user/',views.get_user, name='get_user'),

]
