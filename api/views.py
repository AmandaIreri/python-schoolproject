from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from class_period.models import ClassPeriod
from classroom.models import Classroom
from api.serializers import (ClassPeriodSerializer, StudentSerilaizer, TeacherSerializer, CourseSerializer, ClassroomSerializer, MinimalStudentSerializer, MinimalCourseSerializer, MinimalTeacherSerializer, MinimalClassroomSerializer, MinimalClassPeriodSerializer)

# Create your views here.
class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerilaizer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerilaizer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    


class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teachers = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
         
    
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    


class ClassroomListViews(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = MinimalClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = CourseSerializer(classroom)
        return Response(serializer.data)
    
    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED) 
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classroom = Course.objects.get(id=id)
        classroom.delete()
        return Response (status=status.HTTP_202_ACCEPTED)