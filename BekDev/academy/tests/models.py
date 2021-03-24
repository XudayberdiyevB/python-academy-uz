from django.db import models


# Create your models here.
from django.utils import timezone

from home.models import TagModel


class Exam(models.Model):
    """
    Exam's model, works as a wrapper for the questions
    """
    name = models.CharField(max_length=64, verbose_name=u'Exam name', )
    date = models.DateField(default=timezone.now())
    tag = models.ManyToManyField(TagModel)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField(verbose_name='Savol')
    is_published = models.BooleanField(default=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return "{content} - {published}".format(content=self.question_text, published=self.is_published)


class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    text = models.TextField(verbose_name='Javob')
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text