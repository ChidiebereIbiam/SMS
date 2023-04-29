from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'results', views.ResultViewSet)

urlpatterns = [
    path("", views.endpoints),
    path("", include(router.urls)),
    path("student-result/<int:student_num>", views.student_result)
]