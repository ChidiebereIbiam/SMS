from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns All the Endpoints for the Student API"""
    data = ['results/',]
    return Response(data)

