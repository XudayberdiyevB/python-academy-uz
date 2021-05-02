from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse

class ProblemModel(models.Model):
    sequence_number = models.CharField(max_length=10)
    name = models.CharField(max_length=1000)
    content = RichTextUploadingField(config_name='question-post', blank=True, null=True)
    difficulty = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('problem_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)