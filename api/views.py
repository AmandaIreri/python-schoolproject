from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from class_period.models import ClassPeriod
from classroom.models import Classroom
from .serializers import ClassPeriodSerializer, StudentSerilaizer, TeacherSerializer, CourseSerializer, ClassroomSerializer

# Create your views here.
class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerilaizer(students, many=True)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
class ClassroomListViews(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    