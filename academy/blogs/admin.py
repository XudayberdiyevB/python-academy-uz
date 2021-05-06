from django.contrib import admin
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel,CategoryBlog

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(CategoryBlog)
admin.site.register(CommentBlogModel)
admin.site.register(ReplyCommentBlogModel)
