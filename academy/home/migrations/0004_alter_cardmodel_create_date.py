# Generated by Django 3.2 on 2021-05-05 03:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_cardmodel_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 8, 31, 46, 369818)),
        ),
    ]
