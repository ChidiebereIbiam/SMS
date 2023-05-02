from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'instructor', views.InstructorViewSet)
router.register(r'course_module', views.Course_ModelViewSet)
router.register(r'course', views.CourseViewSet)


urlpatterns = [
    path('', views.endpoints),
    path('', include(router.urls))

]
