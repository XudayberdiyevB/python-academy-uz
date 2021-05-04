from django.db import models

# Create your models here.
from django.utils import timezone


class LevelJob(models.Model):
    level=models.CharField(max_length=100)

    def __str__(self):
        return self.level
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
    level=models.ManyToManyField(LevelJob)
    email=models.EmailField(null=True,blank=True)
    phone_number=models.CharField(max_length=100)
    telegram_profile=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.title
