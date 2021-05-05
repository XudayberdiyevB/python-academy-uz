from django.contrib import admin
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel,BlogUserModel

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(CommentBlogModel)
admin.site.register(ReplyCommentBlogModel)
admin.site.register(BlogUserModel)