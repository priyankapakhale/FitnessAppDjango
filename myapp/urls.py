from django.urls import path
from . import views

urlspatterns = [
    url(r^'add_user/',views.add_user),
    url(r^'get_user/',views.get_user),

]
