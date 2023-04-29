from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentUserSerializer
from .models import StudentUser

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Student API"""
    data = ['/register/', '/login/', '/profile/',]
    return Response(data)

@api_view(['POST'])
def register(request):

    if request.method == "POST":
        student = StudentUser.objects.create(
            registration_number = request.data['registration_number'],
            surname = request.data['surname'],
            firstname=request.data['firstname'],
            othername=request.data['othername']

        )
        serializer = StudentUserSerializer(student, many=False)
    return Response(serializer.data)

    