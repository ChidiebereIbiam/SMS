from django.urls import path
from . import views


urlpatterns = [
    path("notice/", views.notice),
    path("notice/<int:id>", views.NoticeDetailAPI.as_view()),
    
]
