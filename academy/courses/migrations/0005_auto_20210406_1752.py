# Generated by Django 3.1.7 on 2021-04-06 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210402_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursevideomodel',
            name='video_duration',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='commentcourse',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 747499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courselistmodel',
            name='date_of_kurs',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 735379)),
        ),
        migrations.AlterField(
            model_name='replycommentcourse',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 748765, tzinfo=utc)),
        ),
    ]