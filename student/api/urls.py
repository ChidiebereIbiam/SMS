from django.urls import path
from . import views


urlpatterns = [
    path("", views.endpoints, name="endpoints"),
    path("register/", views.register, name="register"),
    path("student/", views.student_list, name="student-list"),
    path("student/<int:registration_number>/", views.StudentDetail.as_view()),
    
]

