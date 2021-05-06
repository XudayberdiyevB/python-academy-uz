from django.shortcuts import render
from .models import JobsModel
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.
def job_homepage(request):
    if request.method=='POST':
        search=request.POST['search_job']
        jobs=JobsModel.objects.filter(experience__icontains=search)
        # paginator = Paginator(job, 1) # Show 25 contacts per page

        # page = request.GET.get('page')
        # try:
        #     jobs = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     jobs = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     jobs = paginator.page(paginator.num_pages)
        context = {'jobs':jobs}
        return render(request, 'jobs/job_list.html', context)

    else:
        job = JobsModel.objects.order_by('-id')
        paginator = Paginator(job, 5) 

        page = request.GET.get('page')
        try:
            jobs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            jobs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            jobs = paginator.page(paginator.num_pages)
        
        context = {'jobs':jobs}
        return render(request, 'jobs/job_list.html', context)

def job_detail(request,pk):
    job = JobsModel.objects.get(id=pk)
    return render(request, 'jobs/job_detail.html', {'job':job})