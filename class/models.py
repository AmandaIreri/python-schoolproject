from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_code = models.CharField(max_length=10)
    max_students = models.PositiveIntegerField()
    current_students = models.PositiveBigIntegerField()
    no_of_tables = models.PositiveIntegerField()
    no_of_groups = models.PositiveIntegerField()
    room_number = models.CharField(max_length=10)
    class_rep = models.CharField(max_length=20)
    assistant_trainer_incharge = models.CharField(max_length=20)
    no_of_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.class_name}{self.class_code}"

