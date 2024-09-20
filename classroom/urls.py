from django.urls import path
from . import views 

urlpatterns = [
    path("register/", views.register_classroom, name = "register_classroom"),
    path('', views.classroom_list, name = "classroom_list")
]