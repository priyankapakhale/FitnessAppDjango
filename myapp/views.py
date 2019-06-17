from django.shortcuts import render
from django.models import User

# Create your views here.
def add_user(request, email):
    user = User(first_name = first_name,last_name = last_name, email = email)
    user.save()

def get_user(request, email):
    user = User.objects.get(email = email)
    return user
