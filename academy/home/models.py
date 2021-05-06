from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class TagModel(models.Model):
    name=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CardModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    text = RichTextUploadingField(blank=True, null=True)
    create_date = models.DateField(default=datetime.now())
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.title


class AdminSendMessage(models.Model):
    text=models.TextField()
    image=models.ImageField(default='message.jpeg',upload_to='message/')
    send_date=models.DateField(default=datetime.now())