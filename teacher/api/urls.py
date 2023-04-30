from django.urls import path
from . import views


urlpatterns = [
    path("", views.endpoints),
    # path("teacher-list/", views.teacher_list)
    # path("teacher/", views.TeacherViewSet.as_view())
    
]
