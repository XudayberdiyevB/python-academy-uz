from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
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
    course_name=models.ForeignKey(CourseListModel,on_delete=models.CASCADE)
    video_name=models.CharField(max_length=1000)
    video=models.FileField(blank=True,null=True, upload_to='videos')
    video_time=models.BigIntegerField(max_length=999)

    def __str__(self):
        return str(self.course_name)

class CourseDetailModel(models.Model):
    content = models.CharField(max_length=1000)
    video = models.ManyToManyField(CourseVideoModel)  
    # comment section
    user = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='user images')
    text = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now())

