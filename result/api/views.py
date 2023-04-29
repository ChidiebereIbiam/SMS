from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status, permissions, generics
from .serializers import ResultSerializer
from .models import Result

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Student API"""
    data = ['results/','results/:id']
    return Response(data, status=status.HTTP_200_OK)


class ResultViewSet(viewsets.ModelViewSet):
    """Result API Viewset"""
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    # def list(self, request):
    #     result = Result.objects.all()
    #     result_serializers = ResultSerializer(result, many = True)
    #     return Response (result_serializers.data, status=status.HTTP_200_OK)

    # def retrieve(self, request, student_num=None):
    #     result =  get_list_or_404(Result, student_num=student_num)
    #     serializer = ResultSerializer(result)
    #     return Response(serializer.data, status = statis)   


@api_view(['GET'])
def student_result(request, student_num):
    """Returns a result for a particular student"""
    completed_result = []
    result = Result.objects.all().filter(student_num=student_num)
    for s in result:
        completed_result.append ({
            "id": s.id,
            "session": s.session,
            "term":s.term,
            "current_class": s.current_class,
            "subject": s.subject,
            "test_score":s.test_score,
            "exam_score":s.exam_score,
            "total_score":s.total_score(),
            "grade":s.grade()

        })
        
    
    return Response(completed_result, status=status.HTTP_200_OK)



