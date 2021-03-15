from django.shortcuts import render
from .models import CourseModel, CourseListModel

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