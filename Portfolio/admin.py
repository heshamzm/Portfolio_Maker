from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Profile
# Register your models here.

class UserReview(admin.ModelAdmin):
    list_display = ("user_name", "first_name", "last_name", "email")

class ProfileReview(admin.ModelAdmin):
    list_display = ("user_name", "name")

admin.site.register(User,UserReview)
admin.site.register(Profile,ProfileReview)