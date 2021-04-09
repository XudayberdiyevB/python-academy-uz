from datetime import datetime
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import CourseModel, CourseListModel, CourseVideoModel, CommentCourse
import pafy

# Create your views here.
# all courses
def courses(request):
    courses = CourseModel.objects.all()
    context = {'courses':courses}
    return render(request, 'courses/courses.html', context)

# course lists
def course_list(request,pk=None):
    course=CourseModel.objects.get(id=pk)
    course_list = CourseListModel.objects.filter(course=course)
    count_of_video = CourseVideoModel.objects.filter(name=course_list[0]).count()
    duration_of_course = CourseVideoModel.objects.filter(name=course_list[0])
    hour, minut = 0, 0
    for video in duration_of_course:
        hour += int((video.video_time).split(':')[0])
        minut += int((video.video_time).split(':')[1])
    if minut >= 60:
        hour += minut // 60
        minut = minut % 60

    # ---- number of view ----
    #course_object = CourseListModel.objects.all()
    course_object = get_object_or_404(CourseListModel, id=pk)

    #course_object.number_of_view += 1
    #course_object.save()
    print(course_object)

    context = {'course_list':course_list, 'count_of_video':count_of_video,
               'soat':hour, 'minut':minut}

    return render(request, 'courses/course_list.html', context)

def course_detail_view(request,pk):
    course_list = get_object_or_404(CourseListModel, id=pk)
    comments = CommentCourse.objects.filter(course=course_list)
    first_video = course_list.course_video.all()[0]
    count_of_video = CourseVideoModel.objects.filter(name=course_list).count()
    duration_of_course = CourseVideoModel.objects.filter(name=course_list)
    hour, minut = 0, 0
    for video in duration_of_course:
        hour += int((video.video_time).split(':')[0])
        minut += int((video.video_time).split(':')[1])
    if minut >= 60:
        hour += minut // 60
        minut = minut % 60

    return render(request,'courses/course_detail.html',
                  {'course_list':course_list,'comments':comments,
                   'first_video':first_video, 'count_of_video':count_of_video,
                   'soat':hour, 'minut':minut})

def lesson_detail(request, pn):
    lesson_videos = get_object_or_404(CourseVideoModel, id=pn)
    course_list = get_object_or_404(CourseListModel, id=lesson_videos.name.id)
    return render(request, 'courses/lesson_detail.html', {'lesson':lesson_videos, 'course_list':course_list})

