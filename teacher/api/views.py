from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import TeacherSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Teacher API"""
    data = ['teacher/', 'teacher/:id']
    return Response(data)

# @api_view(['GET', 'POST'])
# def teacher_list(request):
#     """Handles retrieval of teachers and registration of new teacher"""
#     if request.method == "GET":

#         teacher = User.objects.all()
#         serializer = TeacherSerializer(teacher, many=True)
#         return Response(serializer.data)
    
#     if request.method == "POST":
#         teacher = User.objects.create(
#             username = request.data['username'],
#             bio = request.data['bio']
#         )
#         serializer = AdvocateSerializer(advocate, many = False)

#         return Response(serializer.data)

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = TeacherSerializer(teacher)

        return super().retrieve(request)
