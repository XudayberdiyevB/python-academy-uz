# Generated by Django 3.1.7 on 2021-04-06 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210402_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 751944)),
        ),
        migrations.AlterField(
            model_name='commentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 757055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='replycommentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 52, 22, 758827, tzinfo=utc)),
        ),
    ]