from rest_framework import serializers
from student.models import Student
from class_period.models import ClassPeriod

class StudentSerilaizer( serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"