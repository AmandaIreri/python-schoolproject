from django.db import models
from classroom.models import Classroom
from course.models import Course

# Create your models here.
class ClassPeriod (models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='course_period')
    day_of_the_week = models.CharField(max_length=20)
    classroom = models.ForeignKey(Classroom, on_delete = models.SET_NULL, null = True, related_name ='class_time' )
