from rest_framework import serializers
from student.models import Student
from class_period.models import ClassPeriod
from teacher.models import Teacher
from course.models import Course
# from class.models import Class

class StudentSerilaizer( serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Class
#         fields = "__all__"