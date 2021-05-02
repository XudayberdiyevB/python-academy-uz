# Generated by Django 3.2 on 2021-05-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problemmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemmodel',
            name='sequence_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problemmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
