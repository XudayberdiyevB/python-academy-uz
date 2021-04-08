from django.shortcuts import render
from .models import JobsModel

# Create your views here.
def job_homepage(request):
    jobs = JobsModel.objects.order_by('-id')
    context = {'jobs':jobs}
    return render(request, 'jobs/job_list.html', context)

def job_detail(request,pk):
    job = JobsModel.objects.get(id=pk)
    return render(request, 'jobs/job_detail.html', {'job':job})