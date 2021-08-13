from django.contrib import admin
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel,CategoryBlog

class CommentInline(admin.TabularInline):
    model=CommentBlogModel
    extra = 0

class ReplyInline(admin.TabularInline):
    model=ReplyCommentBlogModel
    extra = 0

class CommentBlogModelAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

class ReplyBlogModelAdmin(admin.ModelAdmin):
    inlines=[ReplyInline]

admin.site.register(BlogModel,CommentBlogModelAdmin)
admin.site.register(CategoryBlog)
admin.site.register(CommentBlogModel,ReplyBlogModelAdmin)
admin.site.register(ReplyCommentBlogModel)
