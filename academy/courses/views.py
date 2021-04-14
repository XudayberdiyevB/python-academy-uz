from datetime import datetime
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
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

    for i in course_list:
        duration_of_course = CourseVideoModel.objects.filter(name=i)
        hour = time_count(duration_of_course)[0]
        minut = time_count(duration_of_course)[1]
        #print(type(hour))
        #duration_of_course.hour_of_course = hour
        #duration_of_course.minut_of_course = minut
        #duration_of_course.save()

    context = {'course_list':course_list, 'count_of_video':count_of_video}

    return render(request, 'courses/course_list.html', context)

# ---- number of view ----
#course_object = CourseListModel.objects.all()
#course_object.number_of_view += 1
#course_object.save()

def course_detail_view(request,pk):
    course_list = get_object_or_404(CourseListModel, id=pk)
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

    comments = CommentCourse.objects.order_by('-created_date').filter(course=course_list)
    # ---- send comment ----

    if request.method == 'POST':
        if request.POST.get('comment')=='':
            redirect('courses:course_detail', pk=pk)
        else:
            # print(request.POST)
            # print(request.POST.get('comment_id'))
            if request.POST.get('comment_id') is not None:
                comment=CommentCourse.objects.get(id=request.POST.get('comment_id'))
                reply_com=ReplyCommentCourse(reply_comment=comment,author=request.user,text=request.POST.get('reply_comment'))
                reply_com.save()
            elif request.POST.get('comment') is not None:
                com=CommentCourse(course=course_list)
                com.author=request.user
                com.text=request.POST.get('comment')
                com.save()


        return redirect('courses:course_detail',pk=pk)

    return render(request,'courses/course_detail.html',
                  {'course_list':course_list,'comments':comments,
                   'first_video':first_video, 'count_of_video':count_of_video,
                   'soat':hour, 'minut':minut, 'pkey':pk})

def lesson_detail(request, pn):
    lesson_videos = get_object_or_404(CourseVideoModel, id=pn)
    course_list = get_object_or_404(CourseListModel, id=lesson_videos.name.id)
    return render(request, 'courses/lesson_detail.html', {'lesson':lesson_videos, 'course_list':course_list})

