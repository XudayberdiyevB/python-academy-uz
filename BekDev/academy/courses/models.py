from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from home.models import TagModel

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
    image = models.ImageField(upload_to='img')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_kurs = models.DateField(default=datetime.now())
    number_of_video = models.IntegerField()
    hour_of_kurs = models.IntegerField()
    minute_of_kurs = models.IntegerField()
    number_of_saw = models.IntegerField()
    number_of_comment = models.IntegerField()
    tag = models.ManyToManyField(TagModel, verbose_name='tag_list')

    def __str__(self):
        return self.kurs_name

class CourseVideoModel(models.Model):
    name = models.ForeignKey(CourseListModel, on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True,upload_to='video_course')
    video_name = models.CharField(max_length=100)
    video_time = models.DateTimeField()

    def __str__(self):
        return str(self.name)

class CourseDetailModel(models.Model):    
    course_detail_name = models.ForeignKey(CourseListModel,on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return str(self.course_detail_name)

#################### comment part ###################

class CommentCourse(models.Model):
    course=models.ForeignKey(CourseDetailModel,on_delete=models.CASCADE,related_name='comment')
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now())

    def add_coment(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)

class ReplyCommentCourse(models.Model):
    reply_comment=models.ForeignKey(CommentCourse,on_delete=models.CASCADE,related_name='reply_comment')
    text=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def add_coment_reply(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)