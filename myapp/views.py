from django.shortcuts import render
from myapp.models import User
from django.http.response import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
@csrf_exempt
def add_user(request, email):
    user = User(first_name = first_name,last_name = last_name, email = email)
    user.save()
    return JsonResponse({'user creation':'Successful'})

    req = request.POST
    first_name = req['email']
    email = req['first_name']
    last_name = req['last_name']

    ProfileHelper.addUser(first_name,last_name,email)
    return HttpResponse(json.dumps("User added"), content_type='application/json')

@never_cache
@csrf_exempt
def get_user(request):
    req = request.POST
    email_id = req['email']

    query_set = User.objects.filter(email = email)

    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    l = list()
    mydata = dict()
    user = dict()

    id = data[0]['pk']
    print(id)
    for d in data:
        x = d['fields']
        l.append(x)
    temp = dict()

    mydata['User'] = l[0]
    mydata['id'] = id
    print(mydata)

    return HttpResponse(json.dumps(mydata), content_type='application/json')
