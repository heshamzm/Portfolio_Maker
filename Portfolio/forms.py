from django import forms
from django.db.models import fields
from django.forms import models
from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            "user_name" : "User Name",
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "phone_number" : "Phone Number",
            "email" : "Email"
            }
        
        error_messages = {
            "user_name" : {
                "required" : "Your name must not be empty",
                "max_length" : "please enter a shorter name"
            },
            "first_name" : {
                "required" : "Your name must not be empty",
                "max_length" : "please enter a shorter name"
            },
            "last_name" : {
                "required" : "Your name must not be empty",
                "max_length" : "please enter a shorter name"
            },
            "email" : {
                "required" : "Please enter you email ! ",
                "max_length" : "please enter a shorter email !"
            }
            
        }