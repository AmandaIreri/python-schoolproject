from django.shortcuts import render, redirect
from .forms import ClassroomRegistrationForm
from .models import Classroom

def register_classroom(request):
    if request.method == 'POST':
        form = ClassroomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
        
    else:
        form = ClassroomRegistrationForm

    return render(request, "classroom/register_classroom.html", {"form":form})

def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/classroom_list.html', {'classrooms': classrooms})