from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


