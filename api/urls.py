from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views import TeacherListView


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="class_period_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
]