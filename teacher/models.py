from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    staff_id = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"