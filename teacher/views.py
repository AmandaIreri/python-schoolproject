from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm
from .models import Teacher


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(teacher_list)
        
    else:
        form = TeacherRegistrationForm()

    return render(request, "teacher/register_teacher.html", {"form":form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})