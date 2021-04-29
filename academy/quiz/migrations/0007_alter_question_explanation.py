# Generated by Django 3.2 on 2021-04-29 12:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_question_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Explanation to be shown after the question has been answered.', verbose_name='Explanation'),
        ),
    ]
