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
def course_list(request,pk):
    course=CourseModel.objects.get(id=pk)
    course_list = CourseListModel.objects.filter(course=course)
    context = {'course_list':course_list}
    return render(request, 'courses/course_list.html', context)

def course_detail_view(request,pk):
    course_list = get_object_or_404(CourseListModel, id=pk)
    comments = CommentCourse.objects.filter(course=course_list)
    first_video=course_list.course_video.all()[0]

    return render(request,'courses/course_detail.html',{'course_list':course_list,'comments':comments,'first_video':first_video})

def lesson_detail(request, pn):
    lesson_videos = get_object_or_404(CourseVideoModel, id=pn)
    course_list = get_object_or_404(CourseListModel, id=lesson_videos.name.id)
    return render(request, 'courses/lesson_detail.html', {'lesson':lesson_videos, 'course_list':course_list})

