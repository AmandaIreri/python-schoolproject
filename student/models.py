from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_code = models.CharField(max_length=10, unique=True)
    teacher_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    schedule = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.PositiveIntegerField()
    current_students = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    is_elective = models.BooleanField(default=False)
    prerequisites = models.TextField()
    max_capacity = models.PositiveIntegerField()
    duration_weeks = models.PositiveIntegerField()

    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    hire_date = models.DateField()
    is_fulltime = models.BooleanField(default=True)
    office_number = models.CharField(max_length=10)
    subjects_taught = models.TextField()