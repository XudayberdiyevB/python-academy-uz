from django.shortcuts import render,redirect
from .models import ProblemModel,ProblemAnswerModelUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

def problems(request):
    
    if request.method=='POST':
        s=request.POST['search']
        exercises=ProblemModel.objects.filter(content__icontains=s)
        context = {
            'exercises':exercises
        }
        messages.success(request,'Marxamat qidiruv natijalari')
        return render(request, 'problems/problems.html', context)
    
    exercises = ProblemModel.objects.all().order_by('created_at')

    paginator = Paginator(exercises, 10) 

    page = request.GET.get('page')
    try:
        exercises = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exercises = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exercises = paginator.page(paginator.num_pages)
    context = {
        'exercises':exercises
    }
    return render(request, 'problems/problems.html', context)

def problem_detail(request,pk):
    problem = ProblemModel.objects.get(id=pk)
    all_result=ProblemAnswerModelUser.objects.filter(user=request.user,problem=problem)
    paginator = Paginator(all_result, 10) 

    page = request.GET.get('page')
    try:
        all_result = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_result = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_result = paginator.page(paginator.num_pages)
    all_prob=ProblemModel.objects.all().count()
    filter_prob=ProblemAnswerModelUser.objects.filter(user=request.user,is_correct=True).count()
    context = {
        'problem':problem,
        'all_result':all_result
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
            messages.success(request,'Ajoyib masala yechimingiz adminga yuborildi')
        return redirect('problems:detail',pk=problem_.id)

    return render(request, 'problems/problem_detail.html', context)

@login_required
def my_result_problem(request):
    all_result=ProblemAnswerModelUser.objects.filter(user=request.user,is_waiting=False)
    paginator = Paginator(all_result, 10)
    page = request.GET.get('page')
    try:
        all_result = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_result = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_result = paginator.page(paginator.num_pages)
    all_prob=ProblemModel.objects.all().count()
    filter_prob=ProblemAnswerModelUser.objects.filter(user=request.user,is_correct=True).values('problem').distinct().count()
    urinish=ProblemAnswerModelUser.objects.filter(user=request.user).count()
    return render(request,'problems/my_problem_result.html',{'all_result':all_result,'all':all_prob,'filter':filter_prob,'urinish':urinish})

@login_required
def detail_answer_user(request,pk):
    res=ProblemAnswerModelUser.objects.get(id=pk)
    return render(request,'problems/detail_answer_user.html',{'res':res})

def rating_user(request):
    all_prob=ProblemModel.objects.all().count()
    filter_prob=ProblemAnswerModelUser.objects.filter(user=request.user,is_correct=True)
    
    return render(request,'problems/res.html',{'all':all_prob,'filter':filter_prob})
