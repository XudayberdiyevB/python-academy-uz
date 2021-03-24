from django.shortcuts import render
from .models import Exam, Question, Answer

# Create your views here.

def exam(request):
    exam = Exam.objects.all()
    context = {'tests':exam}
    return render(request, 'tests/tests.html', context)
