from django.shortcuts import render,redirect
from .models import ProblemModel,ProblemAnswerModelUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
def problems(request):
    exercises = ProblemModel.objects.all().order_by('-created_at')
    context = {
        'exercises':exercises
    }
    return render(request, 'problems/problems.html', context)

def problem_detail(request,pk):
    problem = ProblemModel.objects.get(id=pk)
    print(pk)
    context = {
        'problem':problem
    }
    if request.method=='POST':
        code=request.POST['name_code']
        if code=='':
            messages.warning(request,'Xatolik')
        else:
            problem_=ProblemModel.objects.get(id=pk)
            ans=ProblemAnswerModelUser(user=request.user,problem=problem_)
            ans.answer_code_text=code
            ans.save()
            print('ok')
            messages.success(request,'Ajoyib masala yechimingiz adminga yuborildi')
        return redirect('problems:detail',pk=problem_.id)

    return render(request, 'problems/problem_detail.html', context)

@login_required
def my_result_problem(request):
    all_result=ProblemAnswerModelUser.objects.filter(user=request.user)
    return render(request,'problems/my_problem_result.html',{'all_result':all_result})

@login_required
def detail_answer_user(request,pk):
    res=ProblemAnswerModelUser.objects.get(id=pk)
    return render(request,'problems/detail_answer_user.html',{'res':res})