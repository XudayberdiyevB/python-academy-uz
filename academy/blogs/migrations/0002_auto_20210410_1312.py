# Generated by Django 3.1.7 on 2021-04-10 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentblogmodel',
            old_name='course',
            new_name='blog',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 13, 12, 47, 863380)),
        ),
        migrations.AlterField(
            model_name='commentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 8, 12, 47, 866206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='replycommentblogmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 8, 12, 47, 867349, tzinfo=utc)),
        ),
    ]