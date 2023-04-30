from django.shortcuts import render
from . models import Notice
from .serializers import NoticeSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.

@api_view(['GET','POST'])
def notice(request):
    """Handles Fetching and Creating of Notice"""

    if request.method == "GET":
        notice = Notice.objects.all()
        serializer = NoticeSerializer(notice, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        notice = Notice.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            isPublic = request.data['isPublic'],
            isStudent = request.data['isStudent'], 
            isTeacher = request.data['isTeacher'],
        )
        serializer = NoticeSerializer(notice, many = False)
        return Response(serializer.data)
    

class NoticeDetailAPI(APIView):
    """Handles Notice Details API"""

    def get_object(self, id):
        try:
            return Notice.objects.get(id=id)
        except Notice.DoesNotExist:
            raise JsonResponse("Notice doesn't exist")
        
    def get(self, request, id):
        notice = self.get_object(id)
        serializer = NoticeSerializer(notice, many=False)
        return Response (serializer.data)
    
    def put(self, request, id):
        notice = self.get_object(id)
        notice.title = request.data['title']
        notice.content = request.data['content'] 
        notice.isPublic = request.data['isPublic']
        notice.isStudent = request.data['isStudent'] 
        notice.isTeacher = request.data['isTeacher']
        notice.save()
        serializer = NoticeSerializer(notice, many=False)
        return Response(serializer.data)


    def delete(self, request, id):
        notice = self.get_object(id)
        notice.delete()
        return Response("Notice was deleted")



@api_view(['GET'])
def student_notice(request):
    """Returns Notice for Students only"""

    if request.method == "GET":
        notice = Notice.objects.filter(Q(isPublic=True) | Q(isStudent=True))
        serializer = NoticeSerializer (notice, many = True)
        return Response(serializer.data)




