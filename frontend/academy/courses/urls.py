from django.urls import path
from .views import (courses,
                    course_list,
                    course_detail_view,
                    lesson_detail)

app_name = 'courses'
urlpatterns = [
    path('', courses, name="course"),
    path('course-list/<int:pk>/', course_list, name="course_list"),
    path('course-detail/<int:pk>/',course_detail_view,name='course_detail'),
    path('lesson/<int:pn>/', lesson_detail, name="lesson"),

]