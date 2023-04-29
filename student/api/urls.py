from django.urls import path
from . import views


urlpatterns = [
    path("", views.endpoints, name="endpoints"),
    path("register/", views.register, name="register")
    
]

