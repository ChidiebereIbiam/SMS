from django.db import models


from .utils import score_grade


# Create your models here.
class Result(models.Model):
    """Database Model for Result"""
    student_num = models.IntegerField()
    session = models.CharField(max_length=100)
    term = models.CharField(max_length=199)
    current_class = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    class Meta:
        ordering = ["subject"]

    def __str__(self):
        return f"{self.student_num} {self.session} {self.term} {self.subject}"

    def total_score(self):
        return self.test_score + self.exam_score

    def grade(self):
        return score_grade(self.total_score())
