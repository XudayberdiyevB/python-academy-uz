# Generated by Django 3.2 on 2021-05-05 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210505_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 8, 38, 48, 640096)),
        ),
        migrations.AlterField(
            model_name='blogusermodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 8, 38, 48, 645499)),
        ),
    ]
