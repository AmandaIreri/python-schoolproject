from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=10)
    description = models.TextField()
    department = models.CharField(max_length=20)
    max_capacity = models.PositiveIntegerField()
    pass_grade = models.CharField(max_length=10)
    trainer = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, related_name='course')
    requirement = models.TextField()
    language = models.TextField()
    schedule = models.DateTimeField()


    def __str__(self):
        return f"{self.course_name}{self.course_code}"

