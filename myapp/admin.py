from django.contrib import admin
from .models import User, UserDetails, FoodInfo

# Register your models here.
admin.site.register(User)
admin.site.register(UserDetails)
admin.site.register(FoodInfo)
