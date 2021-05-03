from django.shortcuts import render
from .models import JobsModel

# Create your views here.
def job_homepage(request):
    if request.method=='POST':
        search=request.POST['search_job']
        jobs=JobsModel.objects.filter(experience__icontains=search)
        print(jobs)
        context = {'jobs':jobs}
        return render(request, 'jobs/job_list.html', context)

    else:
        jobs = JobsModel.objects.order_by('-id')
        context = {'jobs':jobs}
        return render(request, 'jobs/job_list.html', context)

def job_detail(request,pk):
    job = JobsModel.objects.get(id=pk)
    return render(request, 'jobs/job_detail.html', {'job':job})