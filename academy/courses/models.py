from django.contrib.humanize.templatetags import humanize
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from home.models import TagModel
from .video_title import video_name, video_duration

# Create your models here.
class CourseModel(models.Model):    
    course_name = models.CharField(max_length=50)
    course_info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.course_name

class CourseListModel(models.Model):
    course = models.ManyToManyField(CourseModel)
    kurs_name = models.CharField(max_length=100)
    kurs_info = models.CharField(max_length=1000)
    content = models.TextField()
    image = models.ImageField(upload_to='img')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_kurs = models.DateField(default=datetime.now())
    number_of_view = models.IntegerField(default=0)
    hour_of_course = models.IntegerField(default=0)
    minut_of_course = models.IntegerField(default=0)
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.kurs_name

class CourseVideoModel(models.Model):
    name = models.ForeignKey(CourseListModel, on_delete=models.CASCADE,related_name="course_video")
    video_url = models.URLField(default="https://www.youtube.com/embed/")
    video_title = models.CharField(max_length=1000, blank=True, null=True)
    video_time = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.video_title = video_name(self.video_url)
        self.video_time = video_duration(self.video_url)
        super(CourseVideoModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

#################### comment part ###################

class CommentCourse(models.Model):
    course=models.ForeignKey(CourseListModel,on_delete=models.CASCADE,related_name='comment')
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    #qancha vaqt oldin
    # def get_date(self):
    #     time = datetime.now()
    #     if self.created_date.day == time.day:
    #         return str(time.hour - self.created_date.hour) + " soat oldin"
    #     else:
    #         if self.created_date.month == time.month:
    #             return str(time.day - self.created_date.day) + " kun oldin"
    #         else:
    #             if self.created_date.year == time.year:
    #                 return str(time.month - self.created_date.month) + " oy oldin"
    #     print(self.created_date.day)
    #     return self.created_date

    class Meta:
        ordering=['-created_date']
    #created_date=models.DateTimeField(default=timezone.now())
    #def add_coment(self):
    #    self.created_date = timezone.now()
    #    self.save()

    def __str__(self):
        return str(self.author) + ":" + self.text


class ReplyCommentCourse(models.Model):
    reply_comment=models.ForeignKey(CommentCourse,on_delete=models.CASCADE,related_name='reply_comment')
    text=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ':' + self.text