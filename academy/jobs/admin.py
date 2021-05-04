from django.contrib import admin

# Register your models here.
from jobs.models import JobsModel,LevelJob

admin.site.register(JobsModel)
admin.site.register(LevelJob)