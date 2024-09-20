from django.shortcuts import render, redirect
from .forms import ClassPeriodRegistrationForm
from .models import ClassPeriod

def register_classPeriod(request):
    if request.method == 'POST':
        form = ClassPeriodRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_period_list')
    else:
        form = ClassPeriodRegistrationForm()
        
    return render(request, "classPeriod/register_classPeriod.html", {"form":form})

def class_period_list(request):
    class_periods = ClassPeriod.objects.all()
    return render(request, 'class_period/class_period_list.html', {'class_period': class_periods})