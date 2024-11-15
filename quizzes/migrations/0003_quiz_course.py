# Generated by Django 5.1.1 on 2024-11-11 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_id_alter_enrollment_id'),
        ('quizzes', '0002_rename_options_choices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='courses.course'),
        ),
    ]
