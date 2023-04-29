from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentUserSerializer
from .models import StudentUser
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Student API"""
    data = ['/register', '/login', '/student',"student/:registration_number"]
    return Response(data)

@api_view(['POST'])
def register(request):
    """Handles the registration of new student, requires registration number, surname, firstname
        othername and password
    """
    if request.method == "POST":
        student = StudentUser.objects.create(
            registration_number = request.data['registration_number'],
            surname = request.data['surname'],
            firstname=request.data['firstname'],
            othername=request.data['othername']

        )
        serializer = StudentUserSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def student_list(request):
    """Returns all the students in the System"""
    students = StudentUser.objects.all()
    serializer = StudentUserSerializer(students, many=True)
    return Response(serializer.data)


class StudentDetail(APIView):
    """Returns student details, updating and deleting of student details"""
    
    def get_object(self, registration_number):
        try:
            return StudentUser.objects.get(registration_number=registration_number)
        except StudentUser.DoesNotExist:
            raise JsonResponse("Student does not exist")

    def get(self, request, registration_number):
        student = self.get_object(registration_number)
        serializer = StudentUserSerializer(student, many=False)
        return Response(serializer.data)
    
    def put (self, request, registration_number):
        student= self.get_object(registration_number)
        student.surname = request.data['surname']
        student.firstname = request.data['firstname']
        student.othername = request.data['othername']
        student.email = request.data['email']
        student.current_status = request.data['current_status']
        student.gender = request.data['gender']
        student.date_of_birth = request.data['date_of_birth']
        student.current_class = request.data['current_class']
        student.date_of_admission = request.data['date_of_admission']
        student.parent_mobile_number = request.data['parent_mobile_number']
        student.address = request.data['address']
        student.others = request.data['others']
        student.save()
        serializer = StudentUserSerializer(student, many=False)
        return Response(serializer.data)
    
    def delete(self, request, registration_number):
        student = self.get_object(registration_number)
        student.delete()
        return Response('Student was deleted') 


    