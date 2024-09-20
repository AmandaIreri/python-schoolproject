from django.urls import path
from . import views 

urlpatterns = [
    path("register/", views.register_course, name="register_course"),
    path('', views.course_list, name="course_list")
]