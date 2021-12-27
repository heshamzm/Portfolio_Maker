from django.urls import path
from . import views

urlpatterns  = [
    path("", views.home.as_view(), name='home'),
    path("name", views.name.as_view(), name= "name")
]
