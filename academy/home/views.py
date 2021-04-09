import random

from django.shortcuts import render
from home.models import CardModel,TagModel
from blogs.models import BlogModel
from courses.models import CourseListModel

# Create your views here.

def homepage(request):
    card = CardModel.objects.order_by("-id")[0]

    courses = list(CourseListModel.objects.all())
    if len(courses) == 1:
        courses = random.sample(courses, 1)
    elif len(courses) == 2:
        courses = random.sample(courses, 2)
    else:
        courses = random.sample(courses, 3)

    blogs = list(BlogModel.objects.all())
    if len(blogs) == 1:
        blogs = random.sample(blogs, 1)
    elif len(blogs) == 2:
        blogs = random.sample(blogs, 2)
    else:
        blogs = random.sample(blogs, 3)

    context = {'card':card,'blogs':blogs, 'courses':courses}

    return render(request, 'home/index.html',context)

def team(requst):
    return render(requst, 'team.html')