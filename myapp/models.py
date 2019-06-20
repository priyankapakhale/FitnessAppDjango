from django.db import models
from django.utils import timezone

# Create your models here.
class FoodInfo(models.Model):
    foodinfo_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=50)

class UserDetails(models.Model):
    userdetails_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField() #weight in kg
    height = models.FloatField() #height in cm
    bmi = models.FloatField()
    goal_weight = models.FloatField() #weight in kg
