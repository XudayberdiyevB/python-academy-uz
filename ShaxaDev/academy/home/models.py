from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TagModel(models.Model):
    name=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CardModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    text = models.TextField()
    create_date = models.DateField(default=datetime.now())
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.title

class HomeMaqolaModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    text = models.TextField()
    create_date = models.DateField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(TagModel, verbose_name='list_tag')
    ribbon=models.CharField(max_length=10)


    def __str__(self):
        return str(self.author)