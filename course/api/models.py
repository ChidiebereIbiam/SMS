from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.


def create_slug(title):
    slug = slugify(title)
    qs = Course.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug, qs.first().id)
    return slug

class Instructor(models.Model):
    profile_photo = models.ImageField(upload_to='instructor_profile/', null=True, blank=True)
    name = models.CharField(max_length=150)
    headline = models.CharField(max_length=150)
    about = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.headline}"


class Course_Module(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    file = models.FileField(upload_to='course_content/')

    def __str__(self):
        return f"{self.name} | {self.course}"



class Course(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    langauge = models.CharField(max_length=255)
    course_highlight = models.TextField()
    modules = models.ManyToManyField(Course_Module, related_name="sections")
    instructor = models.ManyToManyField(Instructor, related_name="instructors")
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        return super().save(*args, **kwargs)
