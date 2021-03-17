from django.urls import path, include
from .views import (courses, course_list,
                    video_save_form,course_detail_view)

urlpatterns = [
    path('', courses, name="course"),
    path('/course-list/<int:pk>/', course_list, name="course_list"),
    path('/video_add/',video_save_form,name='video_add'),
    path('/course_detail/<int:pk>/',course_detail_view,name='course_detail')
]