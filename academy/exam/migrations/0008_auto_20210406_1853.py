# Generated by Django 3.1.7 on 2021-04-06 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20210406_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 18, 53, 43, 559202, tzinfo=utc)),
        ),
    ]