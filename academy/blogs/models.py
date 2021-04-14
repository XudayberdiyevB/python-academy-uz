from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from home.models import TagModel

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    #text = RichTextField(blank=True, null=True)
    text = RichTextUploadingField(blank=True, null=True)
    create_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(TagModel, verbose_name='list_tag')

    def __str__(self):
        return self.title

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
