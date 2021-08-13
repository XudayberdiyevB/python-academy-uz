from django.contrib import admin
from .models import (CourseModel, CourseListModel,
                     CourseVideoModel,
                     CommentCourse,ReplyCommentCourse)

class CommentInline(admin.TabularInline):
    model=CommentCourse
    extra = 0

class ReplyInline(admin.TabularInline):
    model=ReplyCommentCourse
    extra = 0

class CommentCourseAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

class ReplyCourseAdmin(admin.ModelAdmin):
    inlines=[ReplyInline]

class ReplyCommentCourseAdmin(admin.ModelAdmin):
    list_display = ['reply_comment', 'created_date']

# Register your models here.
admin.site.register(CourseModel)
admin.site.register(CourseListModel, CommentCourseAdmin)
admin.site.register(CourseVideoModel)
admin.site.register(ReplyCommentCourse, ReplyCommentCourseAdmin)
admin.site.register(CommentCourse, ReplyCourseAdmin)