from django.urls import path
from . import views 

urlpatterns = [
    path("register/", views.register_classPeriod, name = "register_classPeriod"),
    path('', views.class_period_list, name="class_period_list")
]