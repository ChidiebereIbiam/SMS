from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    isPublic = models.BooleanField()
    isStudent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} {self.content}"