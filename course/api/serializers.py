from rest_framework.serializers import ModelSerializer
from .models import Instructor, Course_Module, Course

class InstructorSerializer(ModelSerializer):
    class Meta:
        model= Instructor
        fields = '__all__'


class Course_ModuleSerializer(ModelSerializer):

    class Meta:
        model = Course_Module
        fields = '__all__'


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'