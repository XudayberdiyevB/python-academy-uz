from django.contrib import admin
from .models import CourseModel, CourseListModel,CourseDetailModel,CourseVideoModel

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(CourseListModel)
admin.site.register(CourseDetailModel)
admin.site.register(CourseVideoModel)