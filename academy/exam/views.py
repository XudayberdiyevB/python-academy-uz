from django.shortcuts import render
from .models import Exam, Question, Answer

# Create your views here.

def exam(request):
    exam = Exam.objects.all()
    context = {'exam':exam}
    return render(request, 'exam/exam.html', context)

def exam_detail(request, pk):
    qs = Exam.objects.get(id=pk)
    return render(request, 'exam/test_detail.html', {'test':qs})

def test_results(request, pk):
    qs = Exam.objects.get(id=pk)
    if request.method == 'POST':
        l =  request.POST.getlist('savolid')
        d = {}
        ans_count = 0
        for i in l:
            d[int(i)] = request.POST.get(i)
            q = Question.objects.get(id=int(i))
            for j in q.answers.all():
                if request.POST.get(i)[0] == j.text and j.is_valid:
                    ans_count += 1
                    print('ok')
        print(ans_count)
    print(d)
    context = {
        'test':qs,
        'check': d
    }
    return render(request, 'exam/test_results.html', context)