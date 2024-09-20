from django.shortcuts import render, redirect
from.forms import StudentRegistrationForm
from .models import Student
# Create your views here.

def register_student(request):
    if request.method =='POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentRegistrationForm()
    
    return render(request, "student/register_student.html", {"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})