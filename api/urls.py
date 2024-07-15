from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="class_period_list_view")
]