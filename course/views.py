from django.shortcuts import render, redirect
from .forms import CourseRegistrationForm
from .models import Course

def register_course(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list') 
        
    else:
        form = CourseRegistrationForm()

    return render(request, "course/register_course.html", {"form":form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})    
