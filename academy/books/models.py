from django.db import models

from home.models import TagModel


class BookModel(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    file = models.FileField(blank=True, null=True, upload_to='books')
    image = models.ImageField(blank=True, null=True)
    tag = models.ManyToManyField(TagModel)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name