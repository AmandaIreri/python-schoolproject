from django.urls import path
from .views import StudentListView, ClassPeriodListView, CourseListView, TeacherListView, ClassroomListViews, StudentDetailView, ClassPeriodDetailView, CourseDetailView, ClassroomDetailView, TeacherDetailView


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="class_period_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("classroom/",ClassroomListViews.as_view(),name = "class_room_list_view"),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("classperiods/<int:id>/", ClassPeriodDetailView.as_view(), name="class_period_detail_view"),
    path("courses/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path("teachers/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    path("classroom/<int:id>/", ClassroomDetailView.as_view(), name="class_room_detail_view"),

]