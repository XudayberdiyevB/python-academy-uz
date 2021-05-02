from django.shortcuts import render
from .models import ProblemModel

def problems(request):
    exercises = ProblemModel.objects.all().order_by('-created_at')
    context = {
        'exercises':exercises
    }
    return render(request, 'problems/problems.html', context)

def problem_detail(request, slug):
    problem = ProblemModel.objects.get(slug=slug)
    context = {
        'problem':problem
    }
    return render(request, 'problems/problem_detail.html', context)