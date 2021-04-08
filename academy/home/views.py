from django.shortcuts import render
from home.models import CardModel,TagModel
from blogs.models import BlogModel
from courses.models import CourseListModel

# Create your views here.

def homepage(request):
    card = CardModel.objects.order_by("-id")[0]
    blogs = BlogModel.objects.filter(id__in=[1,2,3])
    courses = CourseListModel.objects.filter(id__in=[1,2,3])

    context = {'card':card,'blogs':blogs, 'courses':courses}

    return render(request, 'home/index.html',context)

def team(requst):
    return render(requst, 'team.html')