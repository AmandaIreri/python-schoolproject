from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from class_period.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from .serializers import StudentSerilaizer
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