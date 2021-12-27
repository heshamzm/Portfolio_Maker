from django import forms
from django.forms import fields
from .models import User, Profile


class NameForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'user_name']
        exclude = ['about', 'plan', 'story']
        labels = {
            "name" : "Enter a Name to be shown in the portfolio",
            "user_name" : "Enter your user name again"
        }
        error_messages = {
            "name" : {
                "required" : "You must enter a name",
                "max_length" : "please enter a shorter name"
            },
            "User Name" : {
                "required" : "You must enter a name",
                "max_length" : "please enter a shorter name"
            }
        }
        

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