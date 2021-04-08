from django.urls import path
from .views import job_homepage, job_detail

app_name = "jobs"
urlpatterns = [
    path('', job_homepage, name="jobs"),
    path('<int:pk>', job_detail, name="job_detail"),
]