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


class OperatorgaXabar(models.Model):
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    send_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)+ '-' +self.text

class UsergaJavob(models.Model):
    send_to=models.ForeignKey(User,on_delete=models.CASCADE)
    savol=models.ForeignKey(OperatorgaXabar,on_delete=models.CASCADE)
    javob=models.TextField()
    send_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.send_to)+ '-' +self.javob

