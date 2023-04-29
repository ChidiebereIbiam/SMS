from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import StudentUser

class StudentUserSerializer(ModelSerializer):
    class Meta:
        model = StudentUser
        fields = "__all__"


