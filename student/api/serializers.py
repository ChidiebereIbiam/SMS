from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import StudentUser

class StudentUserSerializer(ModelSerializer):
    class Meta:
        model = StudentUser
        fields = [
            "registration_number",
            "surname",
            "firstname",
            "othername",
            "email",
            "current_status",
            "gender",
            "date_of_birth",
            "current_class",
            "date_of_admission",
            "parent_mobile_number",
            "address",
            "others",
            "passport",
        ]


