from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teacher', views.TeacherViewSet)



urlpatterns = [
    path("", views.endpoints),
    path('', include(router.urls))
    # path("teacher-list/", views.teacher_list)
    # path("teacher/", views.TeacherViewSet.as_view())
    
]
