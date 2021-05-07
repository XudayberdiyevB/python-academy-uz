from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from home.models import TagModel

# Create your models here.

class CategoryBlog(models.Model):
    category_name=models.CharField(max_length=100)
    category_info=models.CharField(max_length=200)
    image=models.ImageField(upload_to='category_photo',null=True,blank=True)


    def __str__(self):
        return self.category_name


class BlogModel(models.Model):
    category_blog=models.ForeignKey(CategoryBlog, on_delete=models.CASCADE,related_name='category_blog')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    text = RichTextUploadingField(blank=True, null=True,config_name='default')
    create_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    count_of_view=models.IntegerField(default=0)
    count_of_comment=models.IntegerField(default=0)
    tag = models.ManyToManyField(TagModel, verbose_name='list_tag')
    is_publish=models.BooleanField(default=True)

    def blog_count(self):
        return BlogModel.objects.filter(is_publish=True).count()

    def __str__(self):
        return str(self.category_blog)+' - '+self.title




class CommentBlogModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comment_blog')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return str(self.author) + ':' + self.text

class ReplyCommentBlogModel(models.Model):
    reply_comment = models.ForeignKey(CommentBlogModel, on_delete=models.CASCADE, related_name='reply_comment_blog')
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ':' + self.text
