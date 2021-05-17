# Generated by Django 3.2 on 2021-05-07 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0005_alter_problemanswermodeluser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_problem', models.IntegerField(default=0)),
                ('rating_ball', models.IntegerField(default=0)),
                ('problems', models.ManyToManyField(to='problems.ProblemAnswerModelUser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]