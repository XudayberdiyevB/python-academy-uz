# Generated by Django 3.1.7 on 2021-03-15 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210315_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 15, 14, 33, 31, 772426)),
        ),
        migrations.AlterField(
            model_name='homemaqolamodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 15, 14, 33, 31, 776457)),
        ),
    ]
