from django.db import models

# Create your models here.
class ClassPeriod (models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    course = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=20)