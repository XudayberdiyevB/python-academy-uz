# Generated by Django 3.2 on 2021-05-01 11:16

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('create_date', models.DateField(default=datetime.datetime(2021, 5, 1, 16, 16, 43, 100224))),
                ('count_of_view', models.IntegerField(default=0)),
                ('count_of_comment', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='home.TagModel', verbose_name='list_tag')),
            ],
        ),
        migrations.CreateModel(
            name='CommentBlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_blog', to='blogs.blogmodel')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ReplyCommentBlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment_blog', to='blogs.commentblogmodel')),
            ],
        ),
    ]
