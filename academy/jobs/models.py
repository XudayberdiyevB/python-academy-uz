from django.db import models

# Create your models here.
from django.utils import timezone


class JobsModel(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='logo')
    location = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    dedline = models.DateTimeField()
    salary = models.CharField(max_length=50)
    job_time = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    description = models.TextField()
    experience = models.TextField()
    experience_time = models.CharField(max_length=50)
    benifits = models.TextField()

    def __str__(self):
        return self.title

