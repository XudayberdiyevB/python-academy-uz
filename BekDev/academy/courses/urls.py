from django.urls import path, include
from .views import courses, course_list

urlpatterns = [
    path('', courses, name="course"),
    path('course-list/<int:pk>/', course_list, name="course_list")
]