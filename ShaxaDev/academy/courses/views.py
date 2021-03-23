from datetime import datetime
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UploadFileForm
from .models import CourseModel, CourseListModel, CourseVideoModel, CourseDetailModel, CommentCourse


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

#
# def video_save_form(request):
#     lis=CourseListModel.objects.all()
#     if request.method=='POST':
#         print(request.FILES['myfile'])
#
#         for i in request.FILES['myfile']:
#             print(i)
#             list_name=CourseListModel.objects.get(kurs_name=request.POST['select'])
#             v=CourseVideoModel(name=list_name,file=i,video_name=f"{request.FILES['myfile']}",video_time=datetime.now())
#             v.save()
#             print('yuklandi')
#     return render(request,'courses/video_control.html',{'all':lis})


def course_detail_view(request,pk):
    course_list=CourseListModel.objects.get(id=pk)
    course_det=CourseDetailModel.objects.get(course_detail_name=course_list)
    comments=CommentCourse.objects.filter(course=course_det)
    return render(request,'courses/course_detail.html',{'course':course_det,'course_list':course_list,'comments':comments})



