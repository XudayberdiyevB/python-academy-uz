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
    create_date = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.title

class AdmingaXabar(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    send_date=models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-id']

    def __str__(self):
        return str(self.user)+ '-' +self.text

class UsergaJavob(models.Model):
    send_to=models.ForeignKey(User,on_delete=models.CASCADE)
    savol=models.ForeignKey(AdmingaXabar,on_delete=models.CASCADE, related_name='adminga')
    javob=models.TextField()
    send_date=models.DateTimeField(auto_now_add=True)
    is_answer=models.BooleanField(default=True)

    # class Meta:
    #     ordering = ['-id']

    def __str__(self):
        return str(self.send_to)+ '-' + self.javob + '-' +str(self.is_answer)

class FAQModel(models.Model):
    question = models.TextField(verbose_name='Savol')
    answer = models.TextField(verbose_name='Javob')

    def __str__(self):
        return self.question[:50]