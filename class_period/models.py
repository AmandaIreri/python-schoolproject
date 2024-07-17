from django.db import models
from classroom.models import Classroom
from course.models import Course

# Create your models here.
class ClassPeriod (models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='course_period')
    course = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=20)
    classroom = models.ForeignKey(Classroom, on_delete = models.SET_NULL, null = True, related_name ='class_time' )
