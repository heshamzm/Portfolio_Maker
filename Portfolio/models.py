from django.db import models
from django.db.models.base import Model

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=20)


    


class Profile(models.Model):
    name = models.CharField(max_length=500)
    about = models.CharField(max_length=500)
    plan = models.CharField(max_length=500)
    story = models.CharField(max_length=500)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
