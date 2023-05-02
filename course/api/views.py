from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InstructorSerializer, Course_ModuleSerializer, CourseSerializer
from .models import Instructor, Course_Module, Course
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
import requests

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Course API"""
    data = ['/instructor', 
            '/instructor:id', 
            '/course_module',
            "course_module/:id",
            "course/",
            "course/id"]
    return Response(data)


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def retrieve(self, request, pk=None):
        queryset = Instructor.objects.all()
        instructor = get_object_or_404(queryset, pk=pk)
        courses = Course.objects.filter(instructor = instructor)
        course_serializer = CourseSerializer(courses, many=True)
        serializer = InstructorSerializer(instructor)
        context = {
            "Instructor Detail": serializer.data,
            "courses": course_serializer.data,
        }
        return Response(context)
    

    
class Course_ModelViewSet(ModelViewSet):
    queryset = Course_Module.objects.all()
    serializer_class = Course_ModuleSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer