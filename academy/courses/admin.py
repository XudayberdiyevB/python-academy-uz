from django.contrib import admin
from .models import (CourseModel, CourseListModel,
                     CourseVideoModel,
                     CommentCourse,ReplyCommentCourse)

class CommentCourseAdmin(admin.ModelAdmin):
    list_filter = ['course']

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(CourseListModel)
admin.site.register(CourseVideoModel)
admin.site.register(ReplyCommentCourse)
admin.site.register(CommentCourse, CommentCourseAdmin)