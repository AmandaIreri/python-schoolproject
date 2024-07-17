from django.urls import path
from .views import StudentListView, ClassPeriodListView, CourseListView, TeacherListView, ClassroomListViews


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="class_period_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "student_class_list_view"),

]