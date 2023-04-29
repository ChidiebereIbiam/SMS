from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Result

class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


