from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for Student User """
    def create_user(
            self,
            registration_number,
            surname,
            firstname,
            othername,
            password=None,
    ):
        """Create a New Student"""
        if not registration_number:
            raise ValueError("Student must have a registration number")
        user=self.model(
            registration_number = registration_number,
            surname = surname,
            firstname=firstname,
            othername=othername
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

        
class StudentUser(AbstractBaseUser, PermissionsMixin):
    """Database model for Student Users in the system"""
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    registration_number = models.CharField(max_length=244, primary_key=True, editable=False, unique=True,
    )
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    othername = models.CharField(max_length=200, blank=True)

    
    email = models.EmailField(max_length=254, null=True, blank=True)
    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", null=True, blank=True
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", null=True, blank=True)
    date_of_birth = models.DateField( null=True, blank=True)
    current_class =models.CharField(max_length=50, null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!", 
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True, null=True
    )

    address = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/", null=True)
    
    objects = UserManager()

    USERNAME_FIELD = "registration_number"
    REQUIRED_FIELDS = [
        "surname",
        "firstname",
        "othername",
    ]

    def __str__(self):
        return self.email
    

