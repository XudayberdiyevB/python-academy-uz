import random

from django.shortcuts import render, get_object_or_404
from home.models import CardModel,TagModel
from blogs.models import BlogModel
from courses.models import CourseListModel

# Create your views here.

def card_detail(request, pk):
    card = get_object_or_404(CardModel, id=pk)
    return render(request, 'home/card_detail.html', {'card':card})

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

    tags=TagModel.objects.all()
    context = {'card':card,'blogs':blogs, 'courses':courses,'tags':tags}

    return render(request, 'home/index.html',context)

def team(requst):
    return render(requst, 'team.html')


def tag_filter(request,name):
    tag=get_object_or_404(TagModel,name=name)
    filters_result_course=CourseListModel.objects.filter(tag=tag)
    filters_result_blog=BlogModel.objects.filter(tag=tag)
    filter_result_card=CardModel.objects.filter(tag=tag)
    context={'results_course': filters_result_course, 'results_blog':filters_result_blog,'result_home':filter_result_card}
    return render(request,'home/all_filter.html',context)
