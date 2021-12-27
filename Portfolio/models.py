from django.db import models
from django.db.models.base import Model

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.user_name}"
    
    


class Profile(models.Model):
    name = models.CharField(max_length=500, null= True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    plan = models.CharField(max_length=500, null=True, blank=True)
    story = models.CharField(max_length=500, null= True, blank=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user_name} {self.name}"
    