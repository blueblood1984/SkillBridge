from django.db import models
from django.urls import reverse

from courses.models import Course

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    file = models.FileField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "lecture"

    def get_absolute_url(self):
        return reverse('courses:list')
