from django.shortcuts import render
from myapp.models import User
from django.http.response import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponse
from . import ProfileHelper
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the mediator index.")

@never_cache
@csrf_exempt
def add_user(request):
    print("I am in add request")
    req = request.POST
    first_name = req['first_name']
    last_name = req['last_name']
    email_id = req['email_id']
    #first_name = req.get('first_name')
    #last_name = req.get('last_name')
    #email_id = req.get('email_id')

    ProfileHelper.addUser(first_name,last_name,email_id)
    return HttpResponse(json.dumps("User added"), content_type='application/json')

@never_cache
@csrf_exempt
def add_user_details(request):
    print("In add user details")
    req = request.POST
    email_id = req['email_id']
    age = req['age']
    weight = req['weight']
    height = req['height']
    gender = req['gender']
    goal_weight = 50.0
    bmi = 0.0

    print("fetched gender = ",gender)

    #fetching user from email_id
    query_set = User.objects.filter(email_id = email_id)
    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    print(data)
    data = data[0]
    user = data['fields']
    if gender.lower() == 'female':
        gender = 'F'
    else:
        gender = 'M'

    ProfileHelper.addUser(user, age, gender, weight, height, bmi, goal_weight)
    return HttpResponse(json.dumps("User Details added"), content_type='application/json')


@never_cache
@csrf_exempt
def get_user(request):
    print("I am in get user")
    req = request.POST

    email_id = req['email_id']
    print(email_id)
    query_set = User.objects.filter(email_id = email_id)

    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    print(data)
    data = data[0]
    mydata = dict()

    id = data['pk']
    print(id)

    mydata['user'] = data['fields']
    mydata['id'] = id
    print(mydata)

    return HttpResponse(json.dumps(mydata), content_type='application/json')
